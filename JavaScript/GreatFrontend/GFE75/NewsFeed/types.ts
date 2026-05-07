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
    id: number;
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
    id: number;
    username: string;
    relationShipMapper: RelationShipMapper;
    isVerified: boolean;
    profilePhotoUrl: string;
};

export type Feed = {
    posts: string[];
    id: number;
    prevCursor?: string | null; // A robust cursor is usually an encoded string (often Base64) that contains multiple pieces of metadata to ensure a stable sort i.e timestamp_lastSeenID
    newCursor?: string | null;
    hasOlder: boolean;
    hasNewer: boolean;
};
