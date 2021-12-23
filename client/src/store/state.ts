// This is where the information lives
// Create the interface for the user
export interface User {
    "user": number,
    "followers": Array<string>,
    "following": Array<string>,
    "username": string,
    "bio": string,
    "created": string,
    "avatar": string | null
}

export interface Story {
    user: User,
    stories: Array<string>,
    read: boolean
}

export interface Comment {
    user: User,
    content: string,
    likes: number,
    id: string
}

export interface ImagePost {
    user: User,
    comments: Array<Comment>
    image: string,
    tags: Array<string> | null,
    desc: string,
    id: string
}

export type State = {
    // Allow the user to not be present
    user: User | null,
    stories: Array<Story> | null,
    feed: Array<ImagePost> | null
}

export const state: State = {
    user: null,
    stories: [{
        user: {
            user: 39,
            username: 'user3',
            followers: [],
            following: [],
            bio: '',
            created: '22/22/2222',
            avatar: null
        },
        stories: ['story1', 'story2', 'story3'],
        read: false
    }],
    feed: [{
        user: {
            user: 39,
            username: 'user3',
            followers: [],
            following: [],
            bio: '',
            created: '22/22/2222',
            avatar: null
        },
        comments: [{
            user: {
                user: 33,
                username: 'user2',
                followers: [],
                following: [],
                bio: '',
                created: '22/22/2222',
                avatar: null
            },
            content: 'Some random comment. Have you ever seen a sunset that beautiful? And with rockets in the background? Wild stuff!',
            likes: 22,
            id: '012'
        },
        {
            user: {
                user: 33,
                username: 'user2',
                followers: [],
                following: [],
                bio: '',
                created: '22/22/2222',
                avatar: null
            },
            content: 'Some random comment. Have you ever seen a sunset that beautiful? And with rockets in the background? Wild stuff!',
            likes: 22,
            id: '012'
        },
        {
            user: {
                user: 33,
                username: 'user2',
                followers: [],
                following: [],
                bio: '',
                created: '22/22/2222',
                avatar: null
            },
            content: 'Some random comment. Have you ever seen a sunset that beautiful? And with rockets in the background? Wild stuff!',
            likes: 22,
            id: '012'
        },
        {
            user: {
                user: 33,
                username: 'user2',
                followers: [],
                following: [],
                bio: '',
                created: '22/22/2222',
                avatar: null
            },
            content: 'Some random comment. Have you ever seen a sunset that beautiful? And with rockets in the background? Wild stuff!',
            likes: 22,
            id: '012'
        }],
        image: 'https://1409791524.rsc.cdn77.org/data/images/full/597353/twice-sana-exudes-classy-visuals-on-cosmopolitan-korea-photoshoot.jpg?w=600?w=430',
        tags: ['coolbeach', 'ilikethesun'],
        desc: 'Have you ever seen a sunset that beautiful? And with rockets in the background? Wild stuff! Some random comment. Have you ever seen a sunset that beautiful? And with rockets in the background? Wild stuff!',
        id: '032'
    }, {
        user: {
            user: 39,
            username: 'user3',
            followers: [],
            following: [],
            bio: '',
            created: '22/22/2222',
            avatar: null
        },
        comments: [{
            user: {
                user: 33,
                username: 'user2',
                followers: [],
                following: [],
                bio: '',
                created: '22/22/2222',
                avatar: null
            },
            content: 'Some random comment. Have you ever seen a sunset that beautiful? And with rockets in the background? Wild stuff!',
            likes: 22,
            id: '012'
        }],
        image: 'https://images.unsplash.com/photo-15793371862546556456',
        tags: ['coolbeach', 'ilikethesun'],
        desc: 'Have you ever seen a sunset that beautiful? And with rockets in the background? Wild stuff!',
        id: '032'
    },]
}
