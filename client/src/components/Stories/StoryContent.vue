<template>
    <div class="story-content dark-bg">
        <div class="image">
            <img src="@/assets/icons/arrow.svg" alt="backwards" class="arrow" @click="changeImage(-1)">
            <img src="@/assets/icons/arrow.svg" alt="forward" class="arrow" @click="changeImage(1)">
            <div class="info-bar">
                <span class="author">@clean_9349</span>
                <img src="@/assets/icons/close.svg" alt="close" @click="toggleModal" class="close">
            </div>
            <div class="countdowns">
                <div class="count-line" v-for="image in story.stories" :key="image">
                    <div class="inside-line" v-bind:class="{ active: state.current_image == image}"></div>
                </div>
            </div>
            <!-- <span>{{ state.current_image }}</span> -->
        </div>
    </div>
</template>

<script lang="ts">
import { reactive, defineComponent, watch } from "vue";

export default defineComponent({
  name: "StoryContent",
  props: ["story", "test"],
  setup(props, { emit }){
    const state = reactive({
      current_image: props.story.stories[0],
      timer: 0
    });

    watch(() => props.story, (first, second) => {
      // If the story changes, change to the first image of the new story
      state.current_image = props.story.stories[0];
    });

    function toggleModal(){
      emit('changeVisibility', false)
    }

    // Close the modal if there is no images in the story
    if (!state.current_image) toggleModal();

    // Let the user navigate between the images and stories
    // If the next or previous image does not exist, the user will go to another story
    // in an appropriate direction.
    // Otherwise if there is an image it is going to be displayed.
    const changeImage = (amount:number) => {
        clearTimeout(state.timer)
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

    // Change image after a timeout
    const timeoutImage = () => {
        const timer = setTimeout(() => {
            changeImage(1)
        }, 2000)

        state.timer = timer
    }

    // Start the first timeout after the component is created
    timeoutImage()

    // Then start the next timeout after new image is displayed
    watch(() => state.current_image, (first, second) => {
      timeoutImage()
    });
    
    return { toggleModal, changeImage, state }
  }
});
</script>

<style scoped lang="scss">
@import "@/assets/scss/main.scss";

.story-content{
    width: 100%;
    height: 100vh;
    position: fixed;
    top:0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 999;
}

.image{
    position: fixed;
    width: 390px;
    height: 700px;
    padding: 15px;
    box-sizing: border-box;
    background-color: $black;
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

// Countdown
.countdowns{
    display: flex;
    flex-direction: row;
    margin: 10px 0 10px;
}

.count-line{
    width: 100%;
    height: 2px;
    background-color: #474747;
    margin-right: 10px;
    border-radius: 50vw;
}


.count-line:last-of-type{
    margin-right: 0px;
}

.inside-line{
    width: 0%;
    height: 100%;
    opacity: 0;
    background-color: #e9e9e9;
}

.active{
    animation: timeTransition 2s ease-in-out;
}

.author{
    color: $lightgray;
}

@keyframes timeTransition {
  from {
    width: 0%;
    opacity: 1;
  }

  to {
    width: 100%;
    opacity: 1;
  }
}
</style>