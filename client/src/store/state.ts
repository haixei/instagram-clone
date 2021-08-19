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

export type State = {
    // Allow the user to not be present
    user: User | null
}

export const state: State = {
    user: null
}
