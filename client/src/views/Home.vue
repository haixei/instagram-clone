<template>
  <div class="home">
    <StoryList></StoryList>
    <imagePost v-for="post in feed" :key="post.id" :post="post"></imagePost>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import StoryList from "../components/Stories/StoryList.vue";
import ImagePost from "../components/Content/ImagePost.vue";
import { useStore } from "../store/index"

export default defineComponent({
  name: "Home",
  components: {
    StoryList,
    ImagePost
  },
  setup(){
    const store = useStore();
    const stories = store.getters.stories_data;
    const feed = store.getters.feed_data;
    
    return { stories, feed }
  }
});
</script>
<style scoped>
.home{
  margin-bottom: 40px;
}
</style>