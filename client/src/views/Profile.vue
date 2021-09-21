<template>
  <div class="profile">
    <div class="error" v-if="user == null">
      <img src="@/assets/icons/warning.svg">
      <span>User of this username does not exist.</span>
    </div>
    <div class="profile-cont" v-else>
      <div class="user-info">
        <div class="user-info__about">
          <div class="avatar-cont--big">
            <Avatar></Avatar>
          </div>
          <div class="about-content">
            <span class="username">@{{ user.username }}</span>
            <p>{{user.bio}}</p>
          </div>
        </div>
        <div class="user-info__following">
          <div class="following-cont">
            <span class="following">{{ user.following.length }}<span class="following__type">Following</span></span>
            <span class="following">{{ user.following.length }}<span class="following__type">Followers</span></span>
          </div>
          <button class="button button--lined" v-on:click="followUser" v-if="state.isFollowed == false">Follow</button>
          <button class="button button--black" v-on:click="unfollowUser" v-else>Unfollow</button>
        </div>
      </div>
      <p class="no-posts" v-if="user_feed.length == 0">This user did not post anything yet.</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import Avatar from "../components/User/Avatar.vue";
import { useStore } from "../store/index";
import { useRoute } from "vue-router";
import { ImagePost } from "../store/state";

export default defineComponent({
  name: "Home",
  components: {
    Avatar
  },
  setup(){
    const state = reactive({
      isFollowed: false
    });

    const store = useStore();
    const username = useRoute().params.username;

    // If username not specified, get current user, if user is not logged in, they
    // will be automatically redirected to the login page because of the rotue guardian
    // that is set up in routes/index.ts
    let user = null;
    let user_feed: Array<ImagePost> = [];

    if(!username){
      user = store.getters.user_data;
      // The feed will be loaded from the API if the user is logged in,
      // if not, the user doesnt exist error will appear
      // (...)
    }else{
      // If the username exists, load their page using the API
      // (...)
    }

    const followUser = () => {
      // Forward to the login page if the user is not logged in,
      // otheriwse add the new user to the following list and send a post request
      state.isFollowed = true;
    }

    const unfollowUser = () => {
      state.isFollowed = false;
    }

    return { user, user_feed, state, followUser, unfollowUser }
  }
});
</script>

<style scoped lang="scss">
@import "../assets/scss/main.scss";

.error{
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 60vh;
  justify-content: center;
  img{
    width: 30px;
    margin-bottom: 20px;
  }
}

.user-info__about, .user-info__following, .user-info{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}

.following-cont, .profile-cont{
  display: flex;
  flex-direction: column;
}

.profile-cont, .user-info{
  justify-content: space-between;
}

.following-cont{
  margin-right: 20px;
}

.about-content{
  margin-left: 25px;
  span{
    color: $black;
    font-size: 1.1em;
  }
  p{
    color: $gray;
    font-size: 0.9em;
    width: 50%;
    margin-top: 10px 0 0 0;
  }
}

.following{
  color: $black;
  span{
    margin-left: 5px;
    font-size: 0.9em;
  }
}

.following:first-of-type{
  margin-bottom: 5px;
}

.following__type{
  color: $gray;
}

.user-info{
  border-bottom: 1px solid $mediumgray;
  padding-bottom: 25px;
}

.no-posts{
  width: 100%;
  text-align: center;
  margin: 25px 0 0 0;
  color: $mediumgray;
}
</style>