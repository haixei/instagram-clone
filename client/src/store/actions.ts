import { ActionContext, ActionTree } from 'vuex'
import { Mutations, MutationTypes } from './mutations'
import { State, User } from './state'
import axios from 'axios';


// This module allows you to create actions, actions are similar to mutations but they,
// instead of mutating the state, commit the mutations and can contain arbitrary
// asynchronous operations
export enum ActionTypes {
    UpdateUser = 'UPDATE_USER',
    UpdateStory = 'UPDATE_STORY'
}

type ActionAugments = Omit<ActionContext<State, State>, 'commit'> & {
    commit<K extends keyof Mutations>(
      key: K,
      payload: Parameters<Mutations[K]>[1]
    ): ReturnType<Mutations[K]>
}

export type Actions = {
    [ActionTypes.UpdateUser](context: ActionAugments): void,
}

export const actions: ActionTree<State, State> & Actions = {
    async [ActionTypes.UpdateUser]({ commit }){
        const user = await axios.get('/api/profiles/me')
        .then((res) => {
            return res.data;
        })
        .catch(() => {
            return null;
        });
        
        commit(MutationTypes.UpdateUser, user);
        return user;
    }
}