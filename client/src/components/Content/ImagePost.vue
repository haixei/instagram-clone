<template>
  <div class="image-post">
    <div class="tag-box">
      <span class="tag" v-for="tag in post.tags" :key="tag">#{{ tag }}</span>
    </div>
    <Image :image="post.image" :user="post.user.username" :desc="post.desc"></Image>
    <Comments :comments="post.comments"></Comments>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Image from "./ContentHandles/Image.vue"
import Comments from "./ContentHandles/Comments.vue"

export default defineComponent({
  name: "ImagePost",
  props: ["post"],
  components: {
    Image,
    Comments
  }
})
</script>

<style lang="scss" scoped>
@import "@/assets/scss/main.scss";

.image-post{
  margin-top: 40px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: space-between;
}

.tag-box{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 20%;
}

.tag{
  width: 100%;
  color: $black;
}

</style>