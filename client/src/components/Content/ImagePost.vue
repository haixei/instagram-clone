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
          <div class="tag-box">
            <a class="tag" v-for="tag in post.tags" :key="tag">#{{ tag }}</a>
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
  flex-direction: row;
  align-items: flex-start;
  justify-content: space-between;
}

.tag-box{
  width: 100%;
  display: flex;
  flex-wrap: wrap;
    .tag{
      margin-right: 10px;
      color: $link;
      line-height: 1.6em;
      font-size: 0.88em;
      padding: 3px 20px;
      border-radius: 50vw;
      background-color: #e3e3f1;
    }
}

.tags-comments-column{
  width: 100%;
}


.desc{
    margin: 20px 0;
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