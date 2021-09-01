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

export type State = {
    // Allow the user to not be present
    user: User | null,
    stories: Array<Story> | null
}

export const state: State = {
    user: null,
    stories: [{
        user: 'user1',
        stories: ['story1', 'story2'],
        read: false
      },
      {
        user: 'user2',
        stories: ['story3', 'story4'],
        read: false
      }]
}
