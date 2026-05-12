# News Feed Architecture Diagrams

This document contains visual representations of the News Feed architecture described in the [README.md](./readme.md).

## 1. High-Level System Architecture

The system is divided into four distinct layers to ensure separation of concerns and scalability.

```mermaid
graph TD
    subgraph "View Layer (React/Browser)"
        A[Feed Page] --> B[Post Component]
        A --> C[Composer]
        B --> D[Reactions/Comments]
    end

    subgraph "Store Layer (State Management)"
        E[(Normalized Store)]
        E -->|Provides Data| A
        E -->|Provides Data| B
    end

    subgraph "Data Access Layer (DAL)"
        F[Request Coalescing]
        G[HTTP Caching / ETags]
        H[Offline Outbox / IndexedDB]
        I[Pagination Logic]
        
        C -->|Action| H
        H -->|Sync| F
        A -->|Fetch| I
        I --> F
        F --> G
    end

    subgraph "Server Layer"
        J[API Gateway]
        K[Feed Service]
        L[Post Service]
        M[Media Storage / CDN]
        
        G -->|Network| J
        J --> K
        J --> L
        C -->|Media Upload| M
    end

    %% Styling
    style A fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style B fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style C fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style E fill:#fff9c4,stroke:#fbc02d,stroke-width:2px
    style H fill:#f8bbd0,stroke:#c2185b,stroke-width:2px
    style J fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style K fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style L fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```
![High Level System Architecture](highlevel.png)
---

## 2. Post Creation Flow (with Media & Optimistic UI)

This sequence shows how the system handles media uploads and provides immediate feedback to the user.

```mermaid
sequenceDiagram
    participant U as User
    participant V as View Layer
    participant S as Store Layer
    participant D as Data Access Layer
    participant API as Server API
    participant CDN as Media CDN

    U->>V: Clicks "Post" (with Image)
    V->>D: Initiate Media Upload
    D->>CDN: Upload Binary
    CDN-->>D: Return mediaId
    
    V->>S: Apply Optimistic Update (Pending State)
    S-->>V: Render "Pending" Post
    
    V->>D: Create Post (body + mediaId)
    D->>API: POST /posts (with Idempotency Key)
    
    alt Success
        API-->>D: Return Created Post
        D->>S: Commit Post (Clear Pending)
        S-->>V: Update UI (Success)
    else Failure (Network Error)
        D->>D: Store in Offline Outbox (IndexedDB)
        V->>V: Show "Retry" Affordance
    end
```
![Post Creation Flow](postflow.png)
---

## 3. Offline Outbox Pattern (Resilient Writes)

Ensures user actions (likes, comments, posts) are never lost during poor connectivity.

```mermaid
flowchart LR
    Start([User Action]) --> OptUI[Apply Optimistic UI]
    OptUI --> StoreDB[(Save to IndexedDB)]
    StoreDB --> NetCheck{Network Available?}
    
    NetCheck -- Yes --> Send[Send Request]
    NetCheck -- No --> Wait[Wait / Listen for 'online']
    
    Send --> Success{Success?}
    Success -- Yes --> Delete[Remove from IndexedDB]
    Success -- No (Retryable) --> Backoff[Exponential Backoff + Jitter]
    Backoff --> Send
    Success -- No (Fatal) --> Error[Notify User / Clear Outbox]
    
    Wait --> NetCheck

    style StoreDB fill:#f8bbd0,stroke:#c2185b
    style OptUI fill:#e1f5fe,stroke:#01579b
```

![Offline Outbox Pattern](outbox.png)

---

## 4. Data-Driven Dependency Loading

How the application avoids shipping 50+ post renderers by lazy-loading based on GraphQL metadata.

```mermaid
graph TD
    A[Fetch Feed Data] --> B{GraphQL Response}
    B -->|TextPostFragment| C[Load TextComponent.js]
    B -->|ImagePostFragment| D[Load ImageComponent.js]
    B -->|VideoPostFragment| E[Load VideoComponent.js]
    
    C --> F[Render Post]
    D --> F
    E --> F
    
    subgraph "Tiered Loading"
        T1[Tier 1: App Shell]
        T2[Tier 2: Above-the-fold Renderers]
        T3[Tier 3: Interaction-triggered Chunks]
    end
```
![Data Driven Dependency Loading](data-driven.png)
---

## 5. Optimized Feed Fetching (ETags & Deduplication)

```mermaid
sequenceDiagram
    participant V as View Layer
    participant D as Data Access Layer
    participant API as Server API

    Note over V, D: Multiple components request same Feed
    V->>D: Fetch Feed
    V->>D: Fetch Feed (Simultaneous)
    
    D->>D: Coalesce Requests (Single Promise)
    
    D->>API: GET /feed (If-None-Match: "v123")
    
    alt 304 Not Modified
        API-->>D: 304 Not Modified
        D->>D: Read from Local Cache
    else 200 OK
        API-->>D: 200 OK (New Data + New ETag)
        D->>D: Update Local Cache
    end
    
    D-->>V: Return Feed Data
    D-->>V: Return Feed Data (Shared Promise)
```
![Optimized Feed Fetching](feed-fetching.png)