## [News Feed](https://www.greatfrontend.com/interviews/study/gfe75/questions/system-design/news-feed-facebook)

### Requirements

#### What are the core features to be supported?

1. Creating and publishing new posts
2. Browse feeds of user and their friends
3. Liking and Reacting to posts

#### What kind of posts are supported?

Primarily text and image-based posts.

#### What pagination UX should be used for the feed?

Infinite scrolling, meaning more posts will be added when the user reaches the end of their feed. For long-lived sessions, it is also worth discussing how newer posts are surfaced at the top without silently disrupting what the user is reading.

#### Will the application be used on mobile devices?

Not a priority, but a good mobile experience would be nice. The architecture discussion can stay web-first unless the interviewer explicitly wants to focus on mobile-specific interaction patterns.

---

### Architecture / High-Level Design

A well-structured front-end architecture separates concerns across distinct layers, each responsible for a specific set of tasks.

#### Rendering Approach

1. **CSR (Client-Side Rendering)**
2. **SSR (Server-Side Rendering)**
3. **Hybrid**

For a personalized signed-in feed, the main benefit of rendering on the server is performance, not SEO. The content is already personalized, so search indexing is much less important than keeping the session interactive and responsive.

That makes **CSR** the best default answer for the home feed. The feed is highly interactive, heavily personalized, and benefits from keeping state alive in the browser over a long-lived session. This is a long-session state-management tradeoff, not a claim that CSR has the fastest cold start.

#### Navigation Approach

1. **Single-Page Application (SPA)**: The app loads once, then uses JavaScript to update the URL, fetch data, and update the DOM without a full page reload.
2. **Multi-Page Application (MPA)**: Each route is a separate HTML page, and navigation triggers a full page reload.
3. **Recommendation**: For a feed product, SPA is the stronger default. The biggest reason is shared client state. Most users open a post from the feed itself. In an SPA, the main post details such as text, media, and author data may already be in the store, so navigation to the post detail page can feel nearly instant, and only replies or comments need to be fetched after navigation.

*In an MPA, navigation tears down the current page state and rebuilds it from scratch.*

#### Architecture Layers

![Architecture layers](https://www.gfecdn.net/img/questions/news-feed-facebook/news-feed-architecture.png)

- **View Layer**: The direct interface for user interaction (e.g., feed pages, post details, and composers). This layer is responsible for rendering data provided by the Store and triggering user actions like reactions or post creation.
- **Store Layer**: Functions as the "Single Source of Truth" for the client-side state. It manages normalized data including posts, users, and feed ordering, while also handling optimistic updates and freshness states to keep the UI responsive.
- **Data Access Layer**: An abstraction layer that manages all backend communication. Its responsibilities include handling network requests, parsing responses, implementing pagination (like cursor-based logic), managing retries, and transforming raw API data into structures optimized for the store.
- **Server Layer**: The external boundary that exposes HTTP endpoints for core functionality. This includes fetching feed data, creating new posts, uploading media, and recording user engagement actions like shares or reactions.

*This separation allows you to "harden" each part of the system independently—for example, updating your Data Access caching policy without disrupting your View components.*

---

### Data Entities

You can find them in the attached [types.ts](./types.ts) file.

---

### Feed Pagination

1. **Offset-based pagination**: Relies on numerical offsets to determine which results to fetch next. For example, a request might specify `?offset=20&limit=10` to get the next ten posts after the first twenty. This is why offset-based pagination is a better fit for relatively static lists such as search results, where jumping to a specific page matters more than handling real-time inserts cleanly.
2. **Cursor-based pagination**: Uses a unique identifier such as a post ID or timestamp as a cursor that marks the boundary between pages. Instead of asking for "the next 10 results after offset 20", the client requests "the next 10 results after post ID X." Cursor-based pagination is more stable and efficient because it does not depend on the dataset's size or ordering at query time. It works well in environments where data is frequently updated, such as a news feed where new posts appear constantly and older posts can be deleted, re-ranked, or refreshed.

#### Dynamic Loading Count

Whichever pagination style is used, the feed API typically exposes a configurable count or limit parameter alongside the cursor. We can use that flexibility to adapt how many posts to load based on the browser viewport height.

- If the first feed request is initiated on the client in a CSR flow, the app can read `window.innerHeight` before requesting data and size the initial page more accurately.
- If the initial feed response is rendered on the server, the server does not know the viewport height ahead of time, so it usually overfetches slightly. Subsequent fetches can then adapt based on the measured viewport height.

---

### HTTP Caching, Deduplication, and Idempotency

#### 1. HTTP Caching (ETags & 304 Not Modified)

Instead of downloading the same feed data repeatedly, the Data Access Layer uses ETags (entity tags) as a digital fingerprint for your data.

- **How it works**: When you fetch your feed, the server sends the data along with an ETag: `"v123"`. The next time you fetch, the client sends `If-None-Match: "v123"`.
- **The Result**: If no new posts have arrived, the server simply returns a `304 Not Modified` status.
- **Benefit**: You save bandwidth and battery by not re-downloading data you already have.
- **Lightweight Fingerprint**: Instead of hashing the complete data, a hardened server generates a "Lightweight Fingerprint" using Metadata.
  - **Version-Based Hashing**: The server combines the id of the last post in the feed with its `updatedAt` timestamp and the current `viewerReaction` state.
  - **The Algorithm**: These small metadata strings are concatenated and passed through a fast hashing algorithm like MurmurHash or SHA-1.
  - **The Result**: A short, 8–32 character string (e.g., `"34jrfp2"`) that represents the state of the entire feed.

#### 2. Request Coalescing (Deduplication)

This prevents "Self-inflicted DDoS" where multiple parts of your UI accidentally fire identical requests.

- **Example**: Imagine your News Feed has a "Post Detail" sidebar and a "Main Feed." Both components need data for `Post_ABC` at the same time.

```javascript
function createCoalescedFetch() {
  // Persistent Cache to track active, in-flight promises
  const inFlightRequests = new Map();

  return async function (url, options = {}) {
    // 1. The Check: Does this specific request already exist in the map?
    if (inFlightRequests.has(url)) {
      console.log(`Coalescing: Returning existing promise for ${url}`);
      // 2. The Coalesce: Return the stored promise so callers share the same trigger
      return inFlightRequests.get(url);
    }

    // 3. The New Request: Create the promise and store it in the map
    const fetchPromise = fetch(url, options)
      .then((res) => res.json())
      .finally(() => {
        // 4. The Cleanup: Remove from map once settled to allow fresh data later
        inFlightRequests.delete(url);
      });

    inFlightRequests.set(url, fetchPromise);
    return fetchPromise;
  };
}

// Usage Example
const coalescedFetch = createCoalescedFetch();

// Firing three identical requests simultaneously
coalescedFetch('/api/news-feed');
coalescedFetch('/api/news-feed');
coalescedFetch('/api/news-feed');
// Result: Only ONE network request is actually triggered.
```

#### 3. AbortController

When a user navigates away or triggers rapid-fire actions (like repeated clicks on a reaction button), the layer uses `AbortController` to cancel superseded or obsolete requests.

#### 4. Idempotency for Robust Writes

Idempotency ensures that retrying a write operation (like liking a post or submitting a comment) doesn't result in duplicate data on the server.

- **How it works**: The client generates a unique key (such as a UUID) at the moment of user submission. This key is attached to the request via a header or the request body.
- **Stable Retries**: If a network error occurs, the client (or a service worker) can retry the request using the same key. The server recognizes the duplicate key and returns the original successful result instead of creating a second "like" or post.

---

### API Endpoints

| Endpoint | Purpose |
| :--- | :--- |
| `GET /posts/{postId}` | Fetch a single post surface or permalink page. |
| `PUT /posts/{postId}/reaction` | Set or change the viewer's reaction. |
| `DELETE /posts/{postId}/reaction` | Remove the viewer's reaction. |

#### Create Post

This HTTP method is for users to create a new post, which will be shown in their own feed as well as the feeds of others they are friends with.

| Field | Value |
| :--- | :--- |
| **HTTP Method** | `POST` |
| **Path** | `/posts` |
| **Description** | Creates a new post. |
| **Parameters** | `{ body: '...', mediaIds: [...] }` |

**Upload media binaries first, then create the post by mediaId:**
For posts with attachments, upload the binary first, get a `mediaId` back, then include that ID when creating the post. In production, the upload step often involves getting a presigned URL so the client uploads directly to blob storage, keeping large uploads off the application server and letting post creation stay a small JSON request.

**Response Format**: The response format can be just the single post and the client can write it straight into the normalized store:

```json
{
  "post": {
    "id": "124",
    "authorId": "456",
    "body": { "text": "Hello world", "entities": [] },
    "mediaIds": ["m_1"],
    "engagementSummary": {
      "reactions": { "like": 20, "haha": 15 },
      "totalReactions": 35,
      "commentCount": 0,
      "shareCount": 0
    },
    "viewerReaction": null,
    "viewerHasShared": false,
    "createdAt": 1620639583
  },
  "users": [{ "id": "456", "name": "John Doe" }],
  "media": [
    {
      "id": "m_1",
      "src": "https://www.example.com/feed-images.jpg",
      "alt": "An image alt",
      "width": 1200,
      "height": 800
    }
  ]
}
```

![Post creation flow](image.png)
*Post creation flow with media upload and optimistic UI*

---

### Optimizations and Deep Dive

#### 1. Feed List

##### **Virtualized Lists**

With infinite scrolling, the feed lives in one long-lived scroll container. As the user scrolls further down, more posts are appended to the DOM, and with feed posts having complex DOM structure (lots of details to render), the DOM size rapidly increases.

A virtualized list renders only the posts in the viewport plus a small overscan window. In practice, Facebook replaces the contents of off-screen feed posts with spacer `<div>`s whose inline height (e.g. `style="height: 300px"`) matches the measured height of the real content, so scroll position is preserved while the heavy subtree is removed from the DOM. This improves rendering performance in terms of:

- **Browser painting**: Fewer DOM nodes to render and fewer layout computations to be made.
- **Virtual DOM reconciliation**: In frameworks that use a virtual DOM (e.g. React), a simpler empty subtree makes diffing against the previous tree cheaper and produces a smaller set of real DOM mutations.
  - **Stable Keys**: Each virtualized item must have a unique, permanent identifier (like a `postId`) to help the reconciliation engine track it even as it moves in and out of the DOM.
  - **Measurement Cache**: The system maintains an internal dictionary that stores the measured height of every rendered item. If "Post A" is measured at 450px, that value is cached. When the user scrolls away and then back, the virtualizer uses that 450px to instantly set a spacer element, preventing "jumpy" scroll behavior (Layout Shift).
  - **Handling Async Media**: Since images and videos load asynchronously, their initial height might be 0px, expanding only after the asset arrives.

```jsx
import React, { useRef, useEffect } from 'react';

/**
 * A "Smart" Feed Item that reports its own height changes.
 * This handles async images, text wrapping, and window resizing.
 */
const VirtualizedFeedItem = ({ postId, children, onHeightChange }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // 1. Initialize ResizeObserver to watch for DOM size changes
    const resizeObserver = new ResizeObserver((entries) => {
      for (const entry of entries) {
        // 2. Get the actual observed height
        const newHeight = entry.contentRect.height;

        // 3. Trigger the cache update in the parent Virtualizer
        onHeightChange(postId, newHeight);
      }
    });

    // 4. Start observing the container
    resizeObserver.observe(containerRef.current);

    // 5. Cleanup to prevent memory leaks
    return () => resizeObserver.disconnect();
  }, [postId, onHeightChange]);

  return (
    <div
      ref={containerRef}
      className="feed-item-container"
      style={{ overflow: 'hidden' }} // Prevents margin collapse issues in measurement
    >
      {children}
    </div>
  );
};

export default VirtualizedFeedItem;
```

##### **Infinite Scrolling**

There are two popular ways to implement infinite scroll. Both involve rendering a marker element at the bottom of the feed:

1. **Listen for the scroll event**: Add a scroll event listener (ideally throttled) to the page or a timer (via `setInterval`) that checks whether the position of the marker element is within a certain threshold from the bottom of the page. The position of the marker element can be obtained using `Element.getBoundingClientRect`.
2. **Intersection Observer API**: Use the Intersection Observer API to monitor when the marker element is entering or exiting another element or intersecting by a specified amount. *This is a native browser API and is preferred over `Element.getBoundingClientRect()`.*

#### 2. Loading Indicators

A lightweight shimmer loading effect can be layered on top, but the important part is reserving the expected layout so the real content can swap in with minimal visual jump.

#### 3. Preserving Scroll Position on Remounting

Feed scroll positions should be preserved if users navigate to another page and back to the feed. This can be achieved in single-page applications if the feed list data is cached within the client store along with the scroll position. When the user goes back to the feed page, since the data is already on the client, the feed list can be read from the client store and immediately presented on the screen with the previous scroll position; no server round-trip is needed.

#### 4. Stale Feeds

Avoid silently prepending new posts while the user is reading. A banner such as "New posts available" is usually safer because it preserves reading position and lets the user choose when to merge newer content.

- **i. Server-Driven Invalidation: Beyond Timers**
  While standard caching relies on "Time-based staleness" (e.g., refreshing every 60 seconds), viral content requires Server-Driven Invalidation.
  - **Version/High-Water Mark**: The server pushes a lightweight "Current Version" ID to the client via a live channel (like WebSockets). If the client’s version is lower, it knows it’s out of date and triggers a refresh.
  - **Direct Entity Updates**: For extremely high-velocity items (like a post gaining thousands of reactions per second), the server pushes the specific update directly into the client's store, bypassing the need for a full feed refresh.

- **ii. Cross-Tab Consistency: The Mirror Problem**
  A user reacting to a post in one tab leaves all other open tabs showing "stale" data. To "harden" this, the Data Access Layer must synchronize these disparate views.
  - **BroadcastChannel**: This browser API allows tabs to talk to each other. When Tab A performs a mutation (like a "Like"), it broadcasts the update. Tab B listens, identifies the affected `postId`, and updates its own Normalized Store.
  - **Web Locks API & Tab Leadership**: To prevent "Self-inflicted DDoS," multiple tabs should not all poll the server simultaneously. Using the Web Locks API, the tabs "elect a leader". Only the leader tab maintains the live socket/polling connection; follower tabs simply read the updates from shared storage like IndexedDB.

- **iii. Optimistic Updates + Invalidation Signals**
  Optimistic updates make the UI feel instant in the current tab, but they do not automatically fix other tabs.
  - **The Workflow**:
        1. User clicks "Like" in Tab A.
        2. Tab A performs an Optimistic Update locally.
        3. Tab A sends a signal via `BroadcastChannel`.
        4. Tab B receives the signal and updates its UI to match, ensuring both "mirrors" are consistent.

---

### Feed Post Optimizations

#### Delivering data-driven dependencies only when needed

News feed posts can come in many different formats (text, image, videos, polls, etc.), and each post requires custom rendering code. In reality, the Facebook feed supports over 50 different post formats!

If only we could lazy load components depending on the data received! That's already possible but requires an extra network round-trip to lazy load the components after the data is fetched and we know the type of posts to be rendered.

Facebook fetches data from the server using **Relay**, which is a JavaScript-based GraphQL client. Relay couples React components with GraphQL to allow React components to declare exactly which data fields are needed, and Relay will fetch them via GraphQL and provide the components with data. Relay has a feature called **data-driven dependencies** via the `@match` and `@module` GraphQL directives. The GraphQL payload can include metadata describing which renderer module matches the returned data, and the client then loads that module dynamically. This avoids shipping every renderer upfront and reduces the need for a separate render-time discovery step after the data shape is known.

```graphql
# Sample GraphQL query to demonstrate data-driven dependencies.
... on Post {
  content @match {
    ...TextPostFragment @module(name: "TextComponent.react")
    ...ImagePostFragment @module(name: "ImageComponent.react")
  }
}
```

![flow](image-1.png)

#### Rendering Mentions/Hashtags

**Entity ranges (recommended)**: Store the plaintext once and attach metadata describing which character ranges correspond to mentions, hashtags, or links.

```json
{
  "text": "Check out @greatfrontend at https://www.greatfrontend.com #webdev",
  "entities": [
    {
      "type": "mention",
      "start": 10,
      "end": 24,
      "userId": "u_99"
    },
    {
      "type": "link",
      "start": 28,
      "end": 57,
      "url": "https://www.greatfrontend.com"
    },
    {
      "type": "hashtag",
      "start": 58,
      "end": 65
    }
  ]
}
```

*In the example above, `start` is inclusive and `end` is exclusive.*
This is a half-open range matching `String.prototype.slice` semantics. Stating the convention explicitly matters because an off-by-one here silently breaks mention and link boundaries at render time.

**1. What is Custom Syntax?**

- Custom syntax involves embedding metadata directly into the raw text string. Instead of a separate array of objects with start and end indices, the text itself contains the instructions for the renderer.
- **The Format**: A common example is `[[entityId:displayName]]`. For instance, `[[#1234:HBO Max]]` tells the system that the ID for the entity is 1234 and the text to show the user is HBO Max.
- **The Benefit**: It is a "Single Source of Truth" within the string itself. You don't need to synchronize indices if the text is edited or truncated.

**2. Why Hashtags are Unique**

- Hashtags often require no explicit encoding or custom syntax.
- **Regex Rendering**: Because a hashtag is simply `#` followed by a word, the frontend can use a Regex at render time to find all occurrences and turn them into links.
- **No Metadata Needed**: Unlike a mention (which needs a `userId`) or a link (which needs a `url`), a hashtag is self-contained. The text is the data.

#### Rich text editor format (reference)

Editor frameworks like Lexical, TipTap, and Slate define their own serialization, typically as blocks of text plus a side table of entities keyed by ID. Meta's older Draft.js is now deprecated but still a useful reference for the shape: `RawDraftContentState` is an array of blocks (raw text plus entity ranges pointing into character offsets) together with a separate `entityMap`. These formats extend naturally to more entity types but are more verbose than entity ranges on the wire, which is why compact entity ranges are usually preferable for the server/client contract even when the editor itself is tree-based.

#### HTML format (anti-pattern)

The naive option is to store the already-rendered HTML. This is the **wrong default**. Rendering server-stored HTML is a direct XSS vector, it couples the API to web-specific markup so it is harder to reuse on iOS, Android, or any non-web client, and it makes it harder to re-decorate mentions or hashtags later.

---

### Rendering Rich Text Safely

Structured entity-range payloads close the storage-level XSS door but do not close all the render-time doors. A feed product renders user-supplied text, user-supplied link URLs, and sometimes user-supplied media captions, and each of those is a potential vector.

- **Output encode the plaintext**: Modern frameworks (React, Vue, Svelte) escape text interpolation by default. The only way to reintroduce the XSS risk is to opt into `dangerouslySetInnerHTML` or equivalent — don't, unless the content has already passed through a sanitizer like DOMPurify and the allowed tag list is explicit.
- **Validate href URL schemes**: A mention or link entity can carry a `javascript:`, `data:`, or `vbscript:` URL that executes script when the user clicks. Before rendering an `<a href>`, check the URL scheme against an allowlist of `http`, `https`, and `mailto`, and reject or strip everything else.
- **Harden outbound links**: Use `rel="noopener noreferrer"` on every link that opens a new tab to prevent `window.opener` tab-nabbing, and use `target="_blank"` only when the UX genuinely benefits.
- **Set a Content Security Policy (CSP)**: A CSP with `default-src 'self'`, a tight `script-src`, and an `img-src` allowlist that includes only the product's media CDN is the defence-in-depth layer that catches what passes the other controls. Restrictive CSPs are especially important for feed products because they render links, images, and embeds from arbitrary third-party sources.

---

### Rendering Images

Since there can be images in a feed post, we can also briefly discuss some image optimization techniques:

- **Content Delivery Network (CDN)**: Use a CDN to host and serve images for faster loading performance.
- **Modern Image Formats**: Use modern image formats such as AVIF and WebP for significantly better compression than JPEG or PNG. AVIF typically produces the smallest files at a given quality but has slightly narrower browser support than WebP, so pair them with a `<picture>` fallback chain (`AVIF` → `WebP` → `JPEG/PNG`).
- **Proper Alt Text**: `<img>`s should use proper alt text. Facebook provides alt text for user-uploaded images by using Machine Learning and Computer Vision to process the images and generate a description. Generative AI models are also very good at doing that these days.
- **Lazy Loading**: Use `loading="lazy"` as a good default for feed images. Use `IntersectionObserver` when you want more control and want to start loading slightly before the media enters the viewport.
- **Device-Based Loading**: Send the browser dimensions in the feed list requests so that the server can decide what image size to return. Use `srcset` or `<picture>` if there are image processing (resizing) capabilities to load the most suitable image file for the current viewport.
- **Reserve Space Before Load**: Include image dimensions in the payload so the UI can reserve aspect ratio ahead of time and reduce **Cumulative Layout Shift (CLS)**. `width` and `height` attributes on the `<img>` element (or the CSS `aspect-ratio` property) let the browser compute the layout box before the bytes arrive.
- **Adaptive Loading**:
  - **Good Connectivity**: Prefetch offscreen images that are not in the viewport yet but about to enter viewport.
  - **Poor Connectivity**: Render a low-resolution placeholder image and require users to explicitly click on them to load the high-resolution image.
- **Progressive Placeholders**: Use blurred previews or LQIP/BlurHash-style placeholders so users get immediate feedback that media is loading.
- **Upload Side Optimizations**: The composer should do two things before the bytes leave the device:
    1. **Strip EXIF metadata**: User photos often carry GPS coordinates, camera serial numbers, and timestamps. Re-encode the image through a `<canvas>` to drop the EXIF block, or pipe the bytes through a small library that rewrites it.
    2. **Honor EXIF Orientation**: Honor the EXIF orientation flag before re-encoding so portrait photos from iOS do not render sideways.
    3. **Client-Side Resizing**: Resize to the largest size the product actually displays to reduce upload bandwidth on mobile networks and remove a class of server-side rescale work.
