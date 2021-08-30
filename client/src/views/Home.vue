<template>
  <div class="home">
    <StoryList :stories="stories"></StoryList>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import StoryList from "../components/Stories/StoryList.vue";
import { Story } from "../interfaces/data"

export default defineComponent({
  name: "Home",
  components: {
    StoryList,
  },
  setup(){
    // Create an interface for the story object

    const stories:Array<Story> = [
      {
        user: 'user1',
        stories: ['story1', 'story2'],
        read: false
      }
    ]

    return { stories }
  }
});
</script>
