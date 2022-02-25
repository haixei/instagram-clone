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
            username: 'cosmokr',
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
            content: 'Cosmo really hit us hard this time, perfect choice for a new years cover. Love you Sana!',
            likes: 41,
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
            content: 'The purple fits you so well!! Cannot wait to see more omg! I should get the same hair color..',
            likes: 20,
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
            content: 'You look lovely in this.. and with cosmo??? You are killing it.. that is it. Please do one with Jihyo in spring, she would fit so well!',
            likes: 32,
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
            content: 'This is super cute!',
            likes: 22,
            id: '012'
        }],
        image: 'https://images.unsplash.com/photo-1580273916550-e323be2ae537?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80',
        tags: ['coolbeach', 'ilikethesun'],
        desc: 'Celebrate New Years Eve with Cosmopolitan and beautiful Sana from Twice! We are ready to put all the glitter on, are you?',
        id: '032',
    }, {
        user: {
            user: 39,
            username: 'karina00',
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
            content: 'Better than ever before, period.',
            likes: 120,
            id: '012'
        }],
        image: 'https://1409791524.rsc.cdn77.org/data/images/full/591301/aespa-giselle.jpg',
        tags: ['staycute'],
        desc: 'Just summer.',
        id: '032'
    },]
}
