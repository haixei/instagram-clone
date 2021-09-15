<template>
  <div class="image-post">
    <span class="section-header">Stories</span>
    <StoryCircle v-for="story in state.stories" :key="story.user.username" :author="story.user.username" :read="story.read" @changeVisibility="changeVisibility" @openStory="openStory"></StoryCircle>
    <StoryContent v-if="state.show_story" @changeVisibility="changeVisibility" @changeStory="changeStory" :story="state.story" :test="state.show_story"></StoryContent>
  </div>
</template>

<script lang="ts">
import { reactive, defineComponent, computed, watch } from "vue";
import StoryCircle from "./StoryCircle.vue";
import StoryContent from "./StoryContent.vue";
import { Story } from "../../store/state"
import { useStore } from "../../store/index"

export default defineComponent({
  name: "ImagePost",
  components: {
      StoryCircle,
      StoryContent
  },
  setup(props){
    // Create the state
    const store = useStore();

    interface storyState {
      stories: Array<Story>,
      show_story: boolean,
      current_story_author: string,
      story: Story | undefined
    }

    const state:storyState = reactive({
      stories: store.getters.stories_data || [],
      show_story: false,
      current_story_author: '',
      story: computed(() => state.stories.find((story: Story) => story.user.username == state.current_story_author))
    });

    // Select a story to show
    const openStory = (author:string) => {
      state.current_story_author = author
    }

    // Toggle the story card
    const changeVisibility = (option: boolean) => {
        state.show_story = option;
    }

    const changeStory = (amount:number) => {
      // Find the index of the current story in the array
      const curr_index = state.stories.findIndex((story: Story) => story.user.username == state.current_story_author)

      const stories_len = state.stories.length;
      // Go to the next or previous story, if does not exist move to the last or first story respectively
      if(curr_index == stories_len - 1 && amount == 1 && stories_len > 1){
        state.current_story_author = state.stories[0].user.username
      }
      else if(curr_index == 0 && amount == -1 && stories_len > 1){
        state.current_story_author = state.stories[stories_len - 1].user.username
      }
      else if(stories_len == 1){
        // Close the modal if we viewed the only story there and have nothing to loop
        changeVisibility(false);
      }
      else{
        // Otherwise change the story
        state.current_story_author = state.stories[curr_index + amount].user.username
      }
    }

    // Make the property acessible before render so vue doesn't get angry
    return { state, changeVisibility, openStory, changeStory }
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
    height: 80px;
}

.section-header{
    margin-right: 20px;
}
</style>