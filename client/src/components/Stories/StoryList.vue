<template>
  <div class="image-post">
    <span class="section-header">Stories</span>
    <StoryCircle v-for="author in authors" :key="author" :author="author" @changeVisibility="changeVisibility" @openStory="openStory"></StoryCircle>
    <StoryContent v-if="state.show_story" @changeVisibility="changeVisibility" @changeStory="changeStory" :story="getStory(state.current_story_author)"></StoryContent>
  </div>
</template>

<script lang="ts">
import { reactive, defineComponent, computed } from "vue";
import StoryCircle from "./StoryCircle.vue";
import StoryContent from "./StoryContent.vue";
import { Story } from "../../interfaces/data"

export default defineComponent({
  name: "ImagePost",
  props: ["stories"],
  components: {
      StoryCircle,
      StoryContent
  },
  setup(props){
    // Create the state
    const state = reactive({
      show_story: false,
      current_story_author: ''
    });

    // Extract the authors
    let authors:Array<string> = [];
    props.stories.forEach((story: Story) => {
      if(!authors.includes(story.user)){
        authors.push(story.user);
      }
    });

    // Select a story to show
    const openStory = (author:string) => {
      state.current_story_author = author
    }

    // Retrieve the story content from the array of them
    const getStory = (author:string) => {
      console.log(author);
      return props.stories.find((story: Story) => story.user == state.current_story_author);
    }

   // Toggle the story card
    const changeVisibility = () => {
        state.show_story = !state.show_story;
    }

    const changeStory = (amount:number) => {
      // Find the index of the current story in the array

      // Go to the next or previous story, if does not exist move to the last or first story respectively
    }

    // Make the property acessible before render so vue doesn't get angry
    return { state, changeVisibility, openStory, authors, getStory, changeStory }
  }
});
</script>

<style scoped lang="scss">
@import "@/assets/scss/main.scss";

.image-post{
    display: flex;
    flex-direction: row;
    align-items: center;
    border-bottom: 1px solid $line;
    height: 70px;
}

.section-header{
    margin-right: 20px;
}
</style>