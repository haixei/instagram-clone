import { GetterTree } from 'vuex'
import { State } from './state'

export type Getters = {
    counterValue(state: State): number
}


export const getters: GetterTree<State, State> & Getters = {
    counterValue(state) {
      return state.counter
    },
}