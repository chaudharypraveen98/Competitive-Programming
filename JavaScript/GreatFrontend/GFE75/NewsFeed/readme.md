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

### Architecture / high-level design

A well-structured front-end architecture separates concerns across distinct layers, each responsible for a specific set of tasks

#### Rendering approach

1. CSR
2. SSR
3. Hybrid

For a personalized signed-in feed, the main benefit of rendering on the server is performance, not SEO. The content is already personalized, so search indexing is much less important than keeping the session interactive and responsive.

That makes CSR the best default answer for the home feed. The feed is highly interactive, heavily personalized, and benefits from keeping state alive in the browser over a long-lived session. This is a long-session state-management tradeoff, not a claim that CSR has the fastest cold start.

#### Navigation approach

1. Single-page application (SPA): The app loads once, then uses JavaScript to update the URL, fetch data, and update the DOM without a full page reload.
2. Multi-page application (MPA): Each route is a separate HTML page, and navigation triggers a full page reload.
3. For a feed product, SPA is the stronger default. The biggest reason is shared client state. Most users open a post from the feed itself. In an SPA, the main post details such as text, media, and author data may already be in the store, so navigation to the post detail page can feel nearly instant, and only replies or comments need to be fetched after navigation.

In an MPA, navigation tears down the current page state and rebuilds it from scratch.

#### Architecture layers

![Architecture layers](https://www.gfecdn.net/img/questions/news-feed-facebook/news-feed-architecture.png)

**View Layer**: The direct interface for user interaction (e.g., feed pages, post details, and composers). This layer is responsible for rendering data provided by the Store and triggering user actions like reactions or post creation.

**Store Layer**: Functions as the "Single Source of Truth" for the client-side state. It manages normalized data including posts, users, and feed ordering, while also handling optimistic updates and freshness states to keep the UI responsive.

**Data Access Layer**: An abstraction layer that manages all backend communication. Its responsibilities include handling network requests, parsing responses, implementing pagination (like cursor-based logic), managing retries, and transforming raw API data into structures optimized for the store.

**Server Layer**: The external boundary that exposes HTTP endpoints for core functionality. This includes fetching feed data, creating new posts, uploading media, and recording user engagement actions like shares or reactions.

This separation allows you to "harden" each part of the system independently—for example, updating your Data Access caching policy without disrupting your View components.

### Data Entities

You can find in attached [file](./types.ts).

### Feed pagination

1. Offset-based pagination : relies on numerical offsets to determine which results to fetch next. For example, a request might specify ?offset=20&limit=10 to get the next ten posts after the first twenty This is why offset-based pagination is a better fit for relatively static lists such as search results, where jumping to a specific page matters more than handling real-time inserts cleanly.
2. Cursor-based pagination uses a unique identifier such as a post ID or timestamp as a cursor that marks the boundary between pages. Instead of asking for "the next 10 results after offset 20", the client requests "the next 10 results after post ID X." Cursor-based pagination is more stable and efficient because it does not depend on the dataset's size or ordering at query time. It works well in environments where data is frequently updated, such as a news feed where new posts appear constantly and older posts can be deleted, re-ranked, or refreshed.

### Dynamic loading count

Whichever pagination style is used, the feed API typically exposes a configurable count or limit parameter alongside the cursor. We can use that flexibility to adapt how many posts to load based on the browser viewport height.

If the first feed request is initiated on the client in a CSR flow, the app can read window.innerHeight before requesting data and size the initial page more accurately. If the initial feed response is rendered on the server, the server does not know the viewport height ahead of time, so it usually overfetches slightly. Subsequent fetches can then adapt based on the measured viewport height.

### HTTP caching, deduplication, and idempotency

1. HTTP Caching (ETags & 304 Not Modified)
    1. Instead of downloading the same feed data repeatedly, the Data Access Layer uses ETags (entity tags) as a digital fingerprint for your data.How it works: When you fetch your feed, the server sends the data along with an ETag: "v123". The next time you fetch, the client sends **If-None-Match**: "v123".
    2. The Result: If no new posts have arrived, the server simply returns a 304 Not Modified status.
    3. Benefit: You save bandwidth and battery by not re-downloading data you already have.
    4. Hash --> Instead of hashing the complete data, a hardened server generates a "Lightweight Fingerprint" using Metadata.
        1. Version-Based Hashing: The server combines the id of the last post in the feed with its updatedAt timestamp and the current viewerReaction state.
        2. The Algorithm: These small metadata strings are concatenated and passed through a fast hashing algorithm like MurmurHash or SHA-1.
        3. The Result: A short, 8–32 character string (e.g., "34jrfp2") that represents the state of the entire feed.
2. Request Coalescing (Deduplication)
    1. This prevents "Self-inflicted DDoS" where multiple parts of your UI accidentally fire identical requests.
    2. Example: Imagine your News Feed has a "Post Detail" sidebar and a "Main Feed." Both components need data for Post_ABC at the same time.
    3. ```
       function createCoalescedFetch() {
         // Persistent Cache to track active, in-flight promises [cite: 813]
         const inFlightRequests = new Map();

         return async function (url, options = {}) {
           // 1. The Check: Does this specific request already exist in the map? [cite: 814]
           if (inFlightRequests.has(url)) {
             console.log(`Coalescing: Returning existing promise for ${url}`);
             // 2. The Coalesce: Return the stored promise so callers share the same trigger [cite: 806, 815]
             return inFlightRequests.get(url);
           }

           // 3. The New Request: Create the promise and store it in the map [cite: 813]
           const fetchPromise = fetch(url, options)
             .then((res) => res.json())
             .finally(() => {
               // 4. The Cleanup: Remove from map once settled to allow fresh data later [cite: 816]
               inFlightRequests.delete(url);
             });

           inFlightRequests.set(url, fetchPromise);
           return fetchPromise;
         };
       }

       // Usage Example
       const coalescedFetch = createCoalescedFetch();

       // Firing three identical requests simultaneously [cite: 700, 713, 811]
       coalescedFetch('/api/news-feed');
       coalescedFetch('/api/news-feed');
       coalescedFetch('/api/news-feed');
       // Result: Only ONE network request is actually triggered.
       ```

3. **AbortController**: When a user navigates away or triggers rapid-fire actions (like repeated clicks on a reaction button), the layer uses AbortController to cancel superseded or obsolete requests.
4. **Idempotency for Robust Writes** : Idempotency ensures that retrying a write operation (like liking a post or submitting a comment) doesn't result in duplicate data on the server.
    1. The client generates a unique key (such as a UUID) at the moment of user submission. This key is attached to the request via a header or the request body.
    2. Stable Retries: If a network error occurs, the client (or a service worker) can retry the request using the same key. The server recognizes the duplicate key and returns the original successful result instead of creating a second "like" or post.

### API endpoints

| Endpoint                        | Purpose                                        |
| ------------------------------- | ---------------------------------------------- |
| GET /posts/{postId}             | Fetch a single post surface or permalink page. |
| PUT /posts/{postId}/reaction    | Set or change the viewer's reaction.           |
| DELETE /posts/{postId}/reaction | Remove the viewer's reaction.                  |

This HTTP method is for users to create a new post, which will be shown in their own feed as well as the feeds of others they are friends with.

| Field       | Value                            |
| ----------- | -------------------------------- |
| HTTP Method | POST                             |
| Path        | /posts                           |
| Description | Creates a new post.              |
| Parameters  | { body: '...', mediaIds: [...] } |

**Upload media binaries first**, then create the post by mediaId
For posts with attachments, upload the binary first, get a mediaId back, then include that ID when creating the post. In production, the upload step often involves getting a presigned URL so the client uploads directly to blob storage, keeping large uploads off the application server and letting post creation stay a small JSON request.

The response format can be just the single post and the client can write it straight into the normalized store:

```
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
Post creation flow with media upload and optimistic UI

### Optimizations and deep dive

1. **Feed list**
    1. **Virtualized lists** : With infinite scrolling, the feed lives in one long-lived scroll container. As the user scrolls further down, more posts are appended to the DOM, and with feed posts having complex DOM structure (lots of details to render), the DOM size rapidly increases. <br> <br> A virtualized list renders only the posts in the viewport plus a small overscan window. In practice, Facebook replaces the contents of off-screen feed posts with spacer <div>s whose inline height (e.g. style="height: 300px") matches the measured height of the real content, so scroll position is preserved while the heavy subtree is removed from the DOM. This improves rendering performance in terms of:
    1. **Browser painting**: Fewer DOM nodes to render and fewer layout computations to be made.
    1. **Virtual DOM reconciliation** : In frameworks that use a virtual DOM (e.g. React, which Facebook uses to render the feed), a simpler empty subtree makes diffing against the previous tree cheaper and produces a smaller set of real DOM mutations.
        1. Stable Keys: Each virtualized item must have a unique, permanent identifier (like a postId) to help React's reconciliation engine track it even as it moves in and out of the DOM.
        2. Measurement Cache: The system maintains an internal dictionary that stores the measured height of every rendered item.
           Example: If "Post A" is measured at 450px, that value is cached. When the user scrolls away and then back, the virtualizer uses that 450px to instantly set a spacer element, preventing the "jumpy" scroll behavior known as Layout Shift.
        3. Handling Async Media: Since images and videos load asynchronously, their initial height might be 0px, expanding only after the asset arrives.

    ```
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

    2.**Infinite scrolling** :There are two popular ways to implement infinite scroll. Both involve rendering a marker element at the bottom of the feed:
    1. Listen for the scroll event: Add a scroll event listener (ideally throttled) to the page or a timer (via setInterval) that checks whether the position of the marker element is within a certain threshold from the bottom of the page. The position of the marker element can be obtained using Element.getBoundingClientRect.
    2. Intersection Observer API: Use the Intersection Observer API to monitor when the marker element is entering or exiting another element or intersecting by a specified amount.
       The Intersection Observer API is a native browser API and is preferred over Element.getBoundingClientRect().

2. **Loading indicators** : A lightweight shimmer loading effect can be layered on top, but the important part is reserving the expected layout so the real content can swap in with minimal visual jump.

3. **Preserving scroll position on remounting** : Feed scroll positions should be preserved if users navigate to another page and back to the feed. This can be achieved in single-page applications if the feed list data is cached within the client store along with the scroll position. When the user goes back to the feed page, since the data is already on the client, the feed list can be read from the client store and immediately presented on the screen with the previous scroll position; no server round-trip is needed.

4. **Stale feeds** : Avoid silently prepending new posts while the user is reading. A banner such as "New posts available" is usually safer because it preserves reading position and lets the user choose when to merge newer content.
i. **Server-Driven Invalidation: Beyond Timers**
While standard caching relies on "Time-based staleness" (e.g., refreshing every 60 seconds), viral content requires Server-Driven Invalidation.


Version/High-Water Mark: The server pushes a lightweight "Current Version" ID to the client via a live channel (like WebSockets). If the client’s version is lower, it knows it’s out of date and triggers a refresh.


Direct Entity Updates: For extremely high-velocity items (like a post gaining thousands of reactions per second), the server pushes the specific update directly into the client's store, bypassing the need for a full feed refresh.

ii. **Cross-Tab Consistency: The Mirror Problem**
A user reacting to a post in one tab leaves all other open tabs showing "stale" data. To "harden" this, the Data Access Layer must synchronize these disparate views.

BroadcastChannel: This browser API allows tabs to talk to each other. When Tab A performs a mutation (like a "Like"), it broadcasts the update. Tab B listens, identifies the affected postId, and updates its own Normalized Store.


Web Locks API & Tab Leadership: To prevent "Self-inflicted DDoS," multiple tabs should not all poll the server simultaneously. Using the Web Locks API, the tabs "elect a leader". Only the leader tab maintains the live socket/polling connection; follower tabs simply read the updates from shared storage like IndexedDB.

ii. **Optimistic Updates + Invalidation Signals**
Optimistic updates make the UI feel instant in the current tab, but they do not automatically fix other tabs.

The Workflow:

User clicks "Like" in Tab A.

Tab A performs an Optimistic Update locally.

Tab A sends a signal via BroadcastChannel.

Tab B receives the signal and updates its UI to match, ensuring both "mirrors" are consistent.
