<template>
  <div class="circle" @click="toggleModal" v-bind:class="{ read: true }">
    <Avatar :user="author"></Avatar>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive } from "vue";
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

    return { toggleModal}
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
    border: 2px solid #7803e6;
}

.read{
  border-color: #797979;
}
</style>