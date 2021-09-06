<template>
  <div class="circle" @click="toggleModal">
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "StoryCircle",
  props: ["author"],
  setup(props, { emit }){

    function toggleModal(){
      emit('openStory', props.author)
      emit('changeVisibility')
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