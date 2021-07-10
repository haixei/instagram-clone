<template>
  <div class="home">
    <HelloWorld msg="Hello! This is the main page." />
    <ImagePost v-for="image in images" v-bind:key="image" v-bind:image="image" />
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";
import HelloWorld from "../components/HelloWorld.vue";
import ImagePost from "../components/ImagePost.vue";

export default defineComponent({
  name: "Home",
  data(){
    return{
      images: []
    }
  },
  components: {
    HelloWorld,
    ImagePost,
  },
  mounted () {
    axios
      .get("/api/postedimages")
      .then((res) => this.images = res.data)
      .catch(error => console.log(error))
  }
});
</script>
