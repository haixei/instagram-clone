<template>
  <div class="home">
    <StoryList :stories="stories"></StoryList>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import StoryList from "../components/Stories/StoryList.vue";
import { useStore } from "../store/index"

export default defineComponent({
  name: "Home",
  components: {
    StoryList,
  },
  setup(){
    const store = useStore();
    const stories = store.getters.stories_data;
    
    return { stories }
  }
});
</script>
