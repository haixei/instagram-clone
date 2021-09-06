<template>
    <div class="image">
        <div class="img-box">
            <img src="@/assets/icons/not-found.svg" v-if="!state.imageFound" class="not-found">
            <img :src="image" @error="notFound" v-if="state.imageFound" class="found-image">
        </div>
        <div class="info">
            <p class="desc">{{ desc }}</p>
            <div class="author-info">
                <div class="avatar"></div>
                <a href="">@{{ user }}</a>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, reactive } from "vue";

export default defineComponent({
  name: "ImagePost",
  props: ["image", "user", "desc"],
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
    margin: 0 40px;
    height: 500px;
    background-color: #dfdfdf;
    border-radius: $radius $radius 10px 10px;
    position: relative;
}

.info{
    width: 100%;
    height: 25%;
    background-color: #fff;
    border-radius: 0px 0px $radius $radius;
    box-sizing: border-box;
    padding: 20px;
    position: relative;
}

.desc{
    color: $gray;
    font-size: 0.93em;
    margin: 0;
    line-height: 1.25em;
}

.author-info{
    display: flex;
    flex-direction: row;
    align-items: center;
    position: absolute;
    bottom: 0;
    margin-bottom: 20px;
}

.avatar{
    width: 24px;
    height: 24px;
    background-color: $black;
    border-radius: 50vw;
    margin-right: 15px;
}

.not-found{
    width: 40px;
}

.img-box{
    height: 85%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.found-image{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: $radius $radius 0px 0px;
}
</style>