<template>
  <div class="home">
    <p>{{ totalCount }}</p>
    <HelloWorld msg="Hello! This is the main page." />
    <ImagePost v-for="image in images" v-bind:key="image" v-bind:image="image" />
  </div>
</template>

<script lang="ts">
// Import libraries & tools
import axios from "axios";
import { defineComponent } from "vue";
import { useStore } from "../store/index"
import { ActionTypes } from '../store/actions'

// Import Components
import HelloWorld from "../components/HelloWorld.vue";
import ImagePost from "../components/ImagePost.vue";

// Import from the Composition API
import { onMounted, computed } from 'vue'

export default defineComponent({
  name: "Home",
  components: {
    HelloWorld,
    ImagePost,
  },
  setup: () => {
    const store = useStore()
    onMounted(() => store.dispatch(ActionTypes.GetCounter))
    const totalCount = computed(() => store.getters.counterValue)
    return { totalCount }
  }
});
</script>
