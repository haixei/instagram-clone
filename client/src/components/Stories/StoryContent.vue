<template>
    <div class="story-content">
        <div class="image">
            <img src="@/assets/icons/arrow.svg" alt="backwards" class="arrow" @click="changeImage(-1)">
            <img src="@/assets/icons/arrow.svg" alt="forward" class="arrow" @click="changeImage(1)">
            <div class="info-bar">
                <span class="author">@clean_9349</span>
                <img src="@/assets/icons/close.svg" alt="close" @click="toggleModal" class="close">
            </div>
            <span>{{ state.current_image }}</span>
        </div>
    </div>
</template>

<script lang="ts">
import { reactive, defineComponent, watch } from "vue";

export default defineComponent({
  name: "StoryContent",
  props: ["story"],
  setup(props, { emit }){
    const state = reactive({
      current_image: props.story.stories[0]
    });

    watch(() => props.story, (first, second) => {
      // If the story changes, change to the first image of the new story
      state.current_image = props.story.stories[0];
    });

    function toggleModal(){
      emit('changeVisibility')
    }

    // Close the modal if there is no images in the story
    if (!state.current_image) toggleModal();

    // Let the user navigate between the images and stories
    // If the next or previous image does not exist, the user will go to another story
    // in an appropriate direction.
    // Otherwise if there is an image it is going to be displayed.
    const changeImage = (amount:number) => {
        const current_index = props.story.stories.indexOf(state.current_image)
        const new_index = current_index + amount;

        if (new_index < 0){
            // If there is no more images backwards, switch to the previous story
            emit('changeStory', -1)
        }
        else if(new_index > props.story.stories.length - 1){
            // .. or the next one if going forward
            emit('changeStory', 1)
        }
        else{
            // If there is an image, display it
            state.current_image = props.story.stories[new_index]
        }
    }
    
    return { toggleModal, changeImage, state }
  }
});
</script>

<style scoped lang="scss">
@import "@/assets/scss/main.scss";

.story-content{
    width: 100%;
    height: 100vh;
    background-color: #2c2c2c48;
    position: fixed;
    top:0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.image{
    position: fixed;
    width: 340px;
    height: 600px;
    padding: 15px;
    box-sizing: border-box;
    background-color: #2c2c2c;
    border: none;
    border-radius: $radius;
    display: flex;
    flex-direction: column;
}

.info-bar{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

.close{
    opacity: 0.6;
}

img{
    cursor: pointer;
    transition: 0.3s;
    width: 13px;
}

img:hover{
    opacity: 1;
}

.arrow{
    opacity: 0.3;
    position: absolute;
    top: 50%;
    transform: translateY(-50%) rotate(180deg);
}

.arrow:last-of-type{
    right: 0;
    transform: translateY(-50%) rotate(0deg);
    margin-right: 15px;
}
</style>