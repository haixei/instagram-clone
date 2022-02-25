<template>
    <div class="image">
        <div class="img-box">
            <img src="@/assets/icons/not-found.svg" v-if="!state.imageFound" class="not-found">
            <img :src="image" @error="notFound" v-if="state.imageFound" class="found-image">
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, reactive } from "vue";
import Avatar from "../../User/Avatar.vue"

export default defineComponent({
  name: "ImagePost",
  props: ["image"],
  setup(){
    const state = reactive({
        imageFound: true
    });

    const notFound = () => {
        state.imageFound = false;
    }

    return { notFound, state }
  }
})
</script>
<style scoped lang="scss">
@import "@/assets/scss/main.scss";

.image{
    width: 100%;
    margin: 0 40px 0 0;
    background-color: #dfdfdf;
    border-radius: $radius $radius 10px 10px;
    position: relative;
}

.img-box{
    height: 550px;
    display: flex;
    align-items: center;
    justify-content: center;
}


.found-image{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: $radius;
}

.not-found{
    width: 40px;
}
</style>