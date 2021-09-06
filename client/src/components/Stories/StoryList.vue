<template>
  <div class="image-post">
    <span class="section-header">Stories</span>
    <StoryCircle v-for="author in authors" :key="author" :author="author" @changeVisibility="changeVisibility" @openStory="openStory"></StoryCircle>
    <StoryContent v-if="state.show_story" @changeVisibility="changeVisibility" @changeStory="changeStory" :story="state.story" :test="state.show_story"></StoryContent>
  </div>
</template>

<script lang="ts">
import { reactive, defineComponent, computed, watch } from "vue";
import StoryCircle from "./StoryCircle.vue";
import StoryContent from "./StoryContent.vue";
import { Story } from "../../store/state"

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
      current_story_author: '',
      story: computed(() => props.stories.find((story: Story) => story.user == state.current_story_author))
    });

    // Extract the authors
    let authors:Array<string> = [];
    
    const updateAuthors = (list: Array<string>, stories: Array<Story>) => {
      stories.forEach((story: Story) => {
        if(!list.includes(story.user)){
          list.push(story.user);
        }
      });
    }

    // Get the initial line of authors
    updateAuthors(authors, props.stories);

    // Watch for the change of the stories and update the authors if needed
    watch(() => props.stories, (first, second) => {
      // If the story changes, change to the first image of the new story
      updateAuthors(authors, props.stories);
    });

    // Select a story to show
    const openStory = (author:string) => {
      state.current_story_author = author
    }

   // Toggle the story card
    const changeVisibility = () => {
        state.show_story = !state.show_story;
    }

    const changeStory = (amount:number) => {
      // Find the index of the current story in the array
      const curr_index = props.stories.findIndex((story: Story) => story.user == state.current_story_author)

      const stories_len = props.stories.length;
      // Go to the next or previous story, if does not exist move to the last or first story respectively
      if(curr_index == stories_len - 1 && amount == 1 && stories_len > 1){
        state.current_story_author = props.stories[0].user
      }
      else if(curr_index == 0 && amount == -1 && stories_len > 1){
        state.current_story_author = props.stories[stories_len - 1].user
      }
      else if(stories_len == 0){
        // Close the modal if we viewed the only story there and have nothing to loop
        changeVisibility();
      }
      else{
        // Otherwise change the story
        state.current_story_author = props.stories[curr_index + amount].user
      }
    }

    // Make the property acessible before render so vue doesn't get angry
    return { state, changeVisibility, openStory, authors, changeStory }
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