<template>
  <div class="image-post">
    <Image :image="post.image" :liked="liked" :stateChanged="stateChanged" v-on:dblclick="changeLikeState"></Image>
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
      <div class="user-interactions">
        <div class="interactions-count">
          <div class="interaction-info">
            <img src="@/assets/icons/comment.svg">
            <span>22</span>
          </div>
          <Like :liked="liked" :likes="post.likes" class="interaction-info" @click="changeLikeState"></Like>
        </div>
        <Comments :comments="post.comments"></Comments>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from "vue";
import Image from "./ContentHandles/Image.vue";
import Comments from "./ContentBlocks/Comment.vue";
import Avatar from "../User/Avatar.vue";
import Like from "./ContentBlocks/Like.vue";

export default defineComponent({
  name: "ImagePost",
  props: ["post"],
  components: {
    Image,
    Comments,
    Avatar,
    Like
  },
  setup(){
    let liked = ref(false)
    let stateChanged = ref(false);

    function changeLikeState(){
      liked.value = !liked.value;
    }

    watch(liked, (value) => {
      // Run a like animation
      console.log(value);
      stateChanged.value = true;
      // If person changes the state of the like (likes/unlikes), 
      // make a call to the API to change the value in the db
    })

    return { liked, stateChanged, changeLikeState }
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


.interactions-count{
    display: flex;
    flex-direction: row;
    align-items: center;
    margin: 25px 0;
}

.interaction-info{
    margin-right: 15px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    span{
        color: $black;
        margin-left: 10px;
        font-size: 0.9rem;
    }
    img{
        width: 19px;
        opacity: 0.9;
    }
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