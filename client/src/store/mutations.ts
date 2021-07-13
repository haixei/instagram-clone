import { MutationTree } from "vuex";
import { State } from "./state"

export enum MutationType {
    ChangeCounter = "CHANGE_COUNTER"
}

export type Mutations = {
    [MutationType.ChangeCounter](state: State, value: number):void
}

export const mutations: MutationTree<State> & Mutations = {
    [MutationType.ChangeCounter](state, value){
        state.counter = value
    }
}
