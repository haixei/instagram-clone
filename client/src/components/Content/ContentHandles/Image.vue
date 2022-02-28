<template>
    <div class="image">
        <img src="@/assets/icons/like.svg" class="like" v-bind:class="{ visible: liked && stateChanged}">
        <img src="@/assets/icons/unlike.svg" class="like" v-bind:class="{ visible: !liked && stateChanged}">
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
  props: ["image", "liked", "stateChanged"],
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
    display: flex;
    justify-content: center;
    align-items: center;
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

// Style the heart
.like{
    width: 70px;
    position: absolute;
    opacity: 0;
}

.visible{
    animation: pop 0.7s;
}


@keyframes pop {
  0% {
    opacity: 0;
    transform: scale(1);
  }

  30% {
    opacity: 1;
    transform: scale(1.3);
  }

  80% {
    opacity: 1;
    transform: scale(1.2);
  }

  100% {
    opacity: 0;
    transform: scale(1);
  }
}
</style>