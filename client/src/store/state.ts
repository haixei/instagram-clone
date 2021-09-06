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
    user: string,
    stories: Array<string>,
    read: boolean
}

export interface Comment {
    user: string,
    content: string,
    likes: number
}

export interface ImagePost {
    user: string,
    comments: Array<Comment> | null,
    image: string,
    tags: Array<string> | null,
    desc: string
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
        user: 'user1',
        stories: ['story1', 'story2', 'story3'],
        read: false
      },
      {
        user: 'user2',
        stories: ['story4'],
        read: false
      }],
    feed: [{
        user: 'user1',
        comments: null,
        image: 'someimage.png',
        tags: ['coolbeach', 'ilikethesun'],
        desc: 'Have you ever seen a sunset that beautiful? And with rockets in the background? Wild stuff!'
    }]
}
