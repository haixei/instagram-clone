<template>
  <div class="circle" @click="toggleModal" v-bind:class="{ read: state.isRead }">
    <Avatar :user="author"></Avatar>
  </div>
</template>

<script lang="ts">
import { defineComponent, watch, reactive } from "vue";
import Avatar from "../User/Avatar.vue";
import { useStore } from "../../store/index";
import { MutationTypes } from "../../store/mutations";

export default defineComponent({
  name: "StoryCircle",
  props: ["author", "read"],
  components: {
    Avatar
  },
  setup(props, { emit }){
    const store = useStore();

    function toggleModal(){
      store.commit(MutationTypes.UpdateStory, props.author)
      emit('openStory', props.author)
      emit('changeVisibility', true)
    }

    const state = reactive({
      isRead: props.read
    });

    watch(() => props.read, (first, second) => {
      state.isRead = first;
      console.log(first, second)
    });

    // Change the read state to true

    return { toggleModal, state}
  }
});
</script>

<style scoped lang='scss'>
@import "@/assets/scss/main.scss";

.circle{
    width: 40px;
    height: 40px;
    border-radius: 50vw;
    background-color: transparent;
    cursor: pointer;
    margin-right: 15px;
    border: 1px solid $link;
    transition: all 0.5s;
    padding: 2px;
}

.read{
  border-color: #e6e6e6;
}
</style>