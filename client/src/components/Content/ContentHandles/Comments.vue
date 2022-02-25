<template>
  <div class="comments">
      <div class="comments-info">
          <img src="@/assets/icons/comment.svg">
          <span>{{ comments.length }}</span>
      </div>
      <div class="comment-list">
          <div class="comment" v-for="comment in comments" :key="comment.id">
            <div class="avatar-cont--small">
                <Avatar :user="comment.user"></Avatar>
            </div>
            <p>{{ comment.content }}</p>
            <div class="likes">
                <span>{{ comment.likes }}</span>
                <img src="@/assets/icons/heart.svg">
            </div>
        </div>
      </div>
      <div class="post-comment">
        <input type="text">
        <button class="button button--black">
            <img src="@/assets/icons/pen.svg">
            Post
        </button>
      </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
import Avatar from "../../User/Avatar.vue"

export default defineComponent({
  name: "Comments",
  props: ["comments"],
  components: {
      Avatar
  }
})
</script>
<style scoped lang="scss">
@import "@/assets/scss/main.scss";

.comments{
    width: 100%;
    height: 100% auto;
    box-sizing: border-box;
    margin-top: 60px;
}

.comment-list{
    max-height: 200px;
    overflow-y: auto;
    position: relative;
}

.comment-list::-webkit-scrollbar {
  width: 10px;
  transition: all 0.5s;
}

.comment-list::-webkit-scrollbar-track {
  background: $white;
}

.comment-list::-webkit-scrollbar-thumb {
  background: #b3b3b3;
  border-radius: 10px;
  border: 3px solid $white;
}

.comment-list::-webkit-scrollbar-thumb:hover {
    background: #9e9e9e;
}

.comments-info{
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 20px;
    span{
        color: $black;
        margin-left: 10px;
    }
    img{
        width: 19px;
    }
}

button{
    img{
        margin: 0 0 1px -5px;
        width: 10px;
    }
}

.comment{
    display: flex;
    flex-direction: row;
    margin-bottom: 25px;
    position: relative;
    p{
        max-width: 300px;
        width: 70%;
        margin: 0;
    }
}

.comment:last-of-type{
    margin-bottom: 0;
}

.likes{
    display: flex;
    flex-direction: row;
    align-items: center;
    position: absolute;
    top: 0;
    right: 15px;
    img{
        width: 15px;
        margin-left: 10px;
    }
    span{
        font-size: 0.9em;
        margin-top: 3px;
        color: #ff4f4f;
        font-family: 'HalveticaMed', sans-serif;
    }
}

.avatar-cont--small{
    margin-right: $avatar-margin;
}

// Post comment
.post-comment{
    display: flex;
    flex-direction: row;
    align-items: center;
    height: auto;
    margin-top: 20px;
    input{
        height: 40px;
        margin-right: 10px;
        padding: 0 20px;
        border: 1px solid #b6b6b6;
        background-color: $lightgray;
        border-radius: 4px;
        box-sizing: border-box;
    }
    input:focus{
        border-color: $link;
        outline: 0 none;
    }
}

@media(max-width: 1100px) {
    .comments{
        padding: 0;
    }
}
</style>