<template>
  <div class="circle" @click="toggleModal">
    <Avatar :user="author"></Avatar>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Avatar from "../User/Avatar.vue"

export default defineComponent({
  name: "StoryCircle",
  props: ["author"],
  components: {
    Avatar
  },
  setup(props, { emit }){

    function toggleModal(){
      emit('openStory', props.author)
      emit('changeVisibility', true)
    }

    return { toggleModal }
  }
});
</script>

<style scoped lang='scss'>
.circle{
    width: 40px;
    height: 40px;
    border-radius: 100vw;
    background-color: #2c2c2c;
    cursor: pointer;
    margin-right: 15px;
}
</style>