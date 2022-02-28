<template>
  <div class="comments">
      <div class="comment-list">
         <Comment v-for="comment in comments" :key="comment.id" :comment="comment"></Comment>
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
import { defineComponent } from "vue";
import Comment from "../ContentHandles/CommentList.vue"

export default defineComponent({
  name: "Comments",
  props: ["comments", "liked"],
  components: {
      Comment
  }
})
</script>
<style scoped lang="scss">
@import "@/assets/scss/main.scss";

.comments{
    width: 100%;
    height: 100% auto;
    box-sizing: border-box;
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

button{
    img{
        margin: 0 0 1px -5px;
        width: 10px;
    }
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