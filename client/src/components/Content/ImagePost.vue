<template>
  <div class="image-post">
    <Image :image="post.image" :user="post.user.username" :desc="post.desc"></Image>
    <div class="tags-comments-column">
      <div class="info">
          <div class="author-info">
              <div class="avatar-cont--small">
                  <Avatar :user="post.user.username"></Avatar>
              </div>
              <a href="">@{{ post.user.username }}</a>
          </div>
          <p class="desc">{{ post.desc }}</p>
          <div class="tag-box" v-if="post.tags.length > 0">
            <a class="tag" v-for="tag in post.tags" :key="tag"><span>#</span>{{ tag }}</a>
          </div>
      </div>
      <Comments :comments="post.comments"></Comments>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Image from "./ContentHandles/Image.vue"
import Comments from "./ContentHandles/Comments.vue"
import Avatar from "../User/Avatar.vue"

export default defineComponent({
  name: "ImagePost",
  props: ["post"],
  components: {
    Image,
    Comments,
    Avatar
  }
})
</script>

<style lang="scss" scoped>
@import "@/assets/scss/main.scss";

.image-post{
  margin-top: 70px;
  display: flex;
  flex-direction: row;transform: translateY(2px);
  align-items: flex-start;
  justify-content: space-between;
}

.tag-box{
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  margin-top: 20px;
}

.tags-comments-column{
  width: 100%;
  height: 550px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}


.desc{
    margin-top: 20px;
}

.author-info{
    display: flex;
    flex-direction: row;
    align-items: center;
    bottom: 0;
    margin-bottom: 20px;
    a{
        margin-bottom: -2px;
    }
}

.avatar-cont--small{
    margin-right: $avatar-margin;
}


@media(max-width: 1100px) {
    .image-post{
        width: 450px;
        flex-direction: column;
        margin: 40px auto 60px auto;
    }
    .info{
      margin-top: 20px;
    }
}
</style>