<template>
    <div class="avatar">
        <img src="@/assets/icons/default-avatar.svg" v-if="state.imageFound">
        <img :src="user.avatar" @error="notFound" v-if="!state.imageFound">
    </div>
</template>
<script lang="ts">
import { defineComponent, reactive } from "vue";

export default defineComponent({
  name: "Avatar",
  props: ["user"],
  setup(){
    const state = reactive({
        imageFound: true
    });

    const notFound = () => {
        state.imageFound = false;
    }

    return { state, notFound }
  }
})
</script>
<style scoped lang="scss">
@import "@/assets/scss/main.scss";

.avatar{
    width: 100%;
    height: 100%;
    border-radius: 50vw;
    overflow: hidden;
    img{
        width: 100%;
        height: 100%;
    }
}
</style>