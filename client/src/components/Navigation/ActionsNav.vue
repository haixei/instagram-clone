<template>
  <div class="actions-nav-wrapper">
      <div class="actions-nav flying-wrapper">
        <a href="/">
          <img src="@/assets/icons/ig-black.svg" alt="Instagram logo">
        </a>
        <div class="button-wrapper">
          <button class="button button--main" v-on:click="changeVisibility">Post</button>
          <button class="button button--white">Log Out</button>
          <a class="profile" href="/profile">
            <Avatar class="profile-avatar"></Avatar>
          </a>
        </div>
      </div>
      <CreatePost v-if="visible" @closeModal="changeVisibility"></CreatePost>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Avatar from "../../components/User/Avatar.vue"
import CreatePost from "../../components/Actions/CreatePost.vue"

export default defineComponent({
  name: "ActionsNav",
  components: {
    Avatar,
    CreatePost
  },
  setup(){
    const visible = ref(false);

    const changeVisibility = () => {visible.value = !visible.value}

    return { visible, changeVisibility }
  }
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/main.scss";

.actions-nav{
    position: fixed;
    top: 0;
    width: 380px;
    height: 60px;
    border: none;
    border-radius: $radius;
    background-color: white;
    left: 0;
    right: 0;
    margin-left: auto;
    margin-right: auto;
    margin-top: 40px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    box-sizing: border-box;
    padding: 15px;
    z-index: 888;
}

.profile{
  width: 40px;
  height: 40px;
  background-color: grey;
  border-radius: 50vw;
  margin-left: 10px;
}

.profile-avatar{
  border-radius: $radius--btn;
}

a{
  display: flex;
  justify-content: center;
}
</style>