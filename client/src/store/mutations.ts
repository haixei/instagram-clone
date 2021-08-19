import { MutationTree } from "vuex";
import { State, User } from "./state"

// Changing values of the information, must be synchronous!
export enum MutationType {
    UpdateUser = "UPDATE_USER"
}

export type Mutations = {
    [MutationType.UpdateUser](state: State, value: User | null):void
}

export const mutations: MutationTree<State> & Mutations = {
    [MutationType.UpdateUser](state, value){
        state.user = value
    }
}
