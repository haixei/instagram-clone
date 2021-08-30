<template>
  <div class="actions-nav flying-wrapper">
      <img src="@/assets/icons/ig-black.svg">
      <div class="button-wrapper">
        <button class="button button--main">Post</button>
        <button class="button button--white">Log Out</button>
      </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ActionsNav",
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/main.scss";

.actions-nav{
    position: fixed;
    top: 0;
    width: 20vw;
    height: 55px;
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
}
</style>