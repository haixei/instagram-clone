<template>
  <div class="actions-nav flying-wrapper">
      <a href="/">
        <img src="@/assets/icons/ig-black.svg">
      </a>
      <div class="button-wrapper">
        <button class="button button--main">Post</button>
        <button class="button button--white">Log Out</button>
        <a class="profile" href="/profile">
          <Avatar class="profile-avatar"></Avatar>
        </a>
      </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Avatar from "../../components/User/Avatar.vue"

export default defineComponent({
  name: "ActionsNav",
  components: {
    Avatar
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
    left:0;
    right:0;
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