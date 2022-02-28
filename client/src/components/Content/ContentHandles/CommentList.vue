<template>
    <div class="comment">
        <div class="avatar-cont--small">
            <Avatar :user="comment.user"></Avatar>
        </div>
        <p>{{ comment.content }}</p>
        <div class="likes">
            <Like @click="changeLikeState" :liked="liked" :likes="comment.likes"></Like>
        </div>
    </div>
</template>
<script>
import { ref } from "vue";
import Avatar from "../../User/Avatar.vue";
import Like from "../ContentBlocks/Like.vue";

export default {
    props: ["comment"],
    components: {
        Avatar,
        Like
    },
    setup(){
        let liked = ref(false);

        function changeLikeState(){
            liked.value = !liked.value;
        }

        return { liked, changeLikeState }
    }
}
</script>
<style scoped lang="scss">
@import "@/assets/scss/main.scss";

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
</style>