import { ActionContext, ActionTree } from 'vuex'
import { Mutations, MutationType } from './mutations'
import { State } from './state'

// This module allows you to create actions, actions are similar to mutations but they,
// instead of mutating the state, commit the mutations and can contain arbitrary
// asynchronous operations
export enum ActionTypes {
    UpdateUser = 'UPDATE_USER'
}

type ActionAugments = Omit<ActionContext<State, State>, 'commit'> & {
    commit<K extends keyof Mutations>(
      key: K,
      payload: Parameters<Mutations[K]>[1]
    ): ReturnType<Mutations[K]>
}

export type Actions = {
    [ActionTypes.UpdateUser](context: ActionAugments): void
}

export const actions: ActionTree<State, State> & Actions = {
    async [ActionTypes.UpdateUser]({ commit }){
        const user = {
            "user": 1,
            "followers": [],
            "following": [],
            "username": 'testuser',
            "bio": 'my bio',
            "created": '22/22/1000',
            "avatar": null
        }
        commit(MutationType.UpdateUser, user);
    }
}