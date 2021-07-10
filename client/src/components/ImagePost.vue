<template>
  <div class="hello">
    <h1>{{ image.image }}</h1>
    <p>With 0.0.0.0:8000</p>
    <div class="img" v-bind:style="{ backgroundImage: 'url(' + 'http://0.0.0.0:8000/api/media/images/yoksel-zok-zAG0Q23ubeo-unsplash_2GyxDwE.jpg' + ')' }"></div>

    <p>With server:8000</p>
    <div class="img" v-bind:style="{ backgroundImage: 'url(' + image.image }"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ImagePost",
  props: {
    image: Object,
  },
});
</script>

<style lang="scss" scoped>

.img{
    width: 200px;
    height: 350px;
    background-size: cover;
    margin: 0 auto;
    background-color: lightgray;
}
</style>