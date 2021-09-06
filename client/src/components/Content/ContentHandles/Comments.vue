<template>
  <div class="comments">
      <div class="comments-info">
          <img src="@/assets/icons/comment.svg">
          <span>{{ comments.length }}</span>
      </div>
      <div class="comment" v-for="comment in comments" :key="comment.id">
          <div class="avatar"></div>
          <p>{{ comment.content }}</p>
          <div class="likes">
              <span>{{ comment.likes }}</span>
              <img src="@/assets/icons/heart.svg">
          </div>
      </div>
      <button class="button button--black">
          <img src="@/assets/icons/pen.svg">
          Comment
      </button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Comments",
  props: ["comments"]
})
</script>
<style scoped lang="scss">
@import "@/assets/scss/main.scss";

.comments{
    width: 100%;
    max-height: 100%;
    box-sizing: border-box;
    padding: 0 0 0 20px;
}

.comments-info{
    display: flex;
    flex-direction: row;
    align-items: center;
    padding-bottom: 10px;
    border-bottom: 1px solid $line;
    span{
        color: $black;
        margin-left: 10px;
    }
    img{
        width: 25px;
    }
}

button{
  margin-top: 25px;
  img{
      margin-bottom: 2px;
  }
}

.comment{
    display: flex;
    flex-direction: row;
    margin-top: 15px;
    position: relative;
    p{
        max-width: 300px;
        width: 70%;
        margin: 0;
        font-size: 0.9em;
        line-height: 1.3em;
    }
}

.likes{
    display: flex;
    flex-direction: row;
    align-items: center;
    position: absolute;
    top: 0;
    right: 0;
    img{
        width: 18px;
        margin-left: 10px;
    }
    span{
        margin-top: 5px;
    }
}

.avatar{
    width: 24px;
    height: 24px;
    background-color: $black;
    border-radius: 50vw;
    margin-right: 15px;
}
</style>