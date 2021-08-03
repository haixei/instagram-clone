<template>
  <div class="home">
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
import ImagePost from "../components/Content/ContentHandles/ImagePost.vue";

// Import from the Composition API
import { onMounted, computed } from 'vue'

export default defineComponent({
  name: "Home",
  components: {
    ImagePost,
  },
  setup: () => {
    // Testing the store, it returns totalCount that can be used in the markup right away
    // To be deleted in the near future :)
    const store = useStore()
    onMounted(() => store.dispatch(ActionTypes.GetCounter))
    const totalCount = computed(() => store.getters.counterValue)
    return { totalCount }
  }
});
</script>
