import { GetterTree } from 'vuex'
import { State, User } from './state'

// This module serves the purpose of retrieving the data from the store,
// it's like a "computed" property but for a store
export type Getters = {
    user_data(state: State): User | null
}

export const getters: GetterTree<State, State> & Getters = {
    user_data(state){
      return state.user
    }
}