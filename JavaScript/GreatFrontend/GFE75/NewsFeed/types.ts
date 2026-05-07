export type ReactionType = "like" | "heart" | "sad" | "excited";

export type Engagement = {
    totalReactions: number;
    shareCount: number;
    commentCount: number;
    reactions: Record<ReactionType, number>;
};
export type PostBody = {
    text: string;
    entities: Array<{
        type: "mention" | "hashtag" | "link";
        start: number;
        end: number;
        userId?: number;
        url?: string;
    }>;
};
export type Post = {
    body: PostBody;
    engagement: Engagement;
    authorId: string;
    id: string;
    createdAt: number;
    mediaIds: string[];
    // these two are separate because all the others data are generalised and this is only personlaized
    viewerReaction: ReactionType | null;
    viewerHasShared: boolean;
};

export type RelationShipMapper = {
    isFollowing: boolean;
    isBlocked: boolean;
    isFriend: boolean;
    isMuted: boolean;
};

export type User = {
    name: string;
    id: string;
    username: string;
    relationShipMapper: RelationShipMapper;
    isVerified: boolean;
    profilePhotoUrl: string;
};

export type Feed = {
    posts: string[];
    id: string;
    prevCursor?: string | null; // A robust cursor is usually an encoded string (often Base64) that contains multiple pieces of metadata to ensure a stable sort i.e timestamp_lastSeenID
    newCursor?: string | null;
    hasOlder: boolean;
    hasNewer: boolean;
};

export type Media = {
    id: string;
    src: string;
    height: number;
    width: number;
    alt: string;
};

export type ComposerDraft = {
    body: PostBody;
    mediaIds: string[];
    uploadStatus: "idle" | "uploading" | "failed";
    submitState: "idle" | "submitting" | "submitted" | "failed";
};

export type Store = {
    feedsByID: Record<string, Feed>;
    usersByID: Record<string, User>;
    mediaByID: Record<string, Media>;
    postsByID: Record<string, Post>;
    composerDraft: ComposerDraft;
};

// Sample store for understanding
const sampleStore = {
    // 1. Feeds: Only store the "Ordering" (IDs)
    feedsById: {
        "home-feed": {
            id: "home-feed",
            postIds: ["post_001", "post_002"], // Pointers to the postsById
            olderCursor: "ts_1715123400",
            newerCursor: "ts_1715125600",
            hasOlder: true,
            hasNewer: false,
            lastFetchedAt: 1715123456789,
        },
    },

    // 2. Posts: The "Source of Truth" for content
    postsById: {
        post_001: {
            id: "post_001",
            authorId: "user_99", // Pointer to usersById
            body: {
                text: "Check out #React and @JohnDoe's new tutorial!",
                entities: [
                    { type: "hashtag", start: 10, end: 16 },
                    { type: "mention", start: 21, end: 29, userId: "user_99" },
                ],
            },
            mediaIds: ["img_55"], // Pointer to mediaById
            engagementSummary: {
                reactions: {
                    like: 120,
                    love: 45,
                    haha: 2,
                    wow: 0,
                    sad: 0,
                    angry: 0,
                },
                totalReactions: 167,
                commentCount: 12,
                shareCount: 5,
            },
            viewerReaction: "like",
            viewerHasShared: false,
            createdAt: 1715123400000,
        },
    },

    // 3. Users: Shared across many posts
    usersById: {
        user_99: {
            id: "user_99",
            name: "John Doe",
            username: "johndoe",
            avatarUrl: "https://cdn.com/jdoe.jpg",
        },
    },

    // 4. Media: Heavy data stored separately
    mediaById: {
        img_55: {
            id: "img_55",
            type: "image",
            url: "https://cdn.com/posts/photo1.jpg",
            width: 1080,
            height: 1350,
        },
    },

    // 5. Composer: Current local UI state
    composerDraft: {
        body: {
            text: "Drafting a new post...",
            entities: [],
        },
        mediaIds: [],
        uploadState: "idle",
        submitState: "idle",
    },
};