import { MutationTree } from "vuex";
import { State, User, Story } from "./state"

// Changing values of the information, must be synchronous!
export enum MutationTypes {
    UpdateUser = "UPDATE_USER",
    UpdateStory = "UPDATE_STORY"
}

export type Mutations = {
    [MutationTypes.UpdateUser](state: State, value: User | null):void,
    [MutationTypes.UpdateStory](state: State, username: string):void
}

export const mutations: MutationTree<State> & Mutations = {
    [MutationTypes.UpdateUser](state, value){
        state.user = value
    },
    [MutationTypes.UpdateStory](state, username){
        // Find the story and change its "read" value to true
        if(state.stories != null){
            const storyIdx = state.stories.findIndex((story: Story) => story.user.username == username)
            console.log(storyIdx)
            state.stories[storyIdx].read = true;
            console.log(state.stories[storyIdx].read)
        }
    }
}
