<template>
    <div class="like">
        <img src="@/assets/icons/heart-outlined.svg" class="post-likes" v-if="!liked">
        <img src="@/assets/icons/heart.svg" class="post-likes" v-if="liked">
        <span>{{ likes }}</span>
    </div>
</template>
<script>
export default {
    props: ["liked", "likes"]
}
</script>
<style scoped>
.like{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}

img{
    width: 19px;
    opacity: 0.9;
    width: 20px;
    margin-right: 10px;
    margin-bottom: 2px;
}

span{
    font-size: 0.9rem;
}
</style>