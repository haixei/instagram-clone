import { GetterTree } from 'vuex'
import { State, User, Story, ImagePost } from './state'

// This module serves the purpose of retrieving the data from the store,
// it's like a "computed" property but for a store
export type Getters = {
    user_data(state: State): User | null,
    stories_data(state: State): Array<Story> | null,
    feed_data(state: State): Array<ImagePost> | null
}

export const getters: GetterTree<State, State> & Getters = {
    user_data(state){
      return state.user
    },
    stories_data(state){
      return state.stories
    },
    feed_data(state){
      return state.feed
    }
}