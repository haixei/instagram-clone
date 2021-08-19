<template>
  <div class="home">
    <ImagePost v-for="image in images" v-bind:key="image" v-bind:image="image" />
  </div>
</template>

<script lang="ts">
// Import libraries & tools
import { defineComponent } from "vue";
// Import Components
import ImagePost from "../components/Content/ContentHandles/ImagePost.vue";

export default defineComponent({
  name: "Home",
  components: {
    ImagePost,
  }
});
</script>
