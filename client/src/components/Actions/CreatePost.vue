<template>
    <div class="create-post-wrapper dark-bg">
        <div class="flying-wrapper create-post">
            <div class="upload-picture">
                <img src="@/assets/icons/picture.svg" alt="Upload icon">
                <span>Upload Image</span>
            </div>
            <div class="picture-info">
                <span class="form-title">Upload a new image</span>
                <form>
                    <input placeholder="Title" maxlength="30">
                    <input placeholder="Tags (max. 4)" v-model="theModel.newTag"
                    v-on:update:title="theModel.newTag = $event"
                    v-on:keydown.enter.prevent="addTag()"
                    :disabled="tagsDisabled"
                    maxlength="10">
                    <textarea placeholder="Description" maxlength="120"></textarea>
                    <div class="right-bottom-box">
                        <div class="tags-wrapper">
                            <a class="tag" v-for="tag in tags" :key="tag" v-on:click="removeTag(tag)"><span>#</span>{{ tag }}</a>
                        </div>
                        <div class="button-wrapper">
                            <button class="button button--black"><img src="@/assets/icons/send.svg"> Post</button>
                            <button class="button button--red" v-on:click.prevent="$emit('closeModal')">Cancel</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import { defineComponent, ref, computed, defineEmit } from "vue";

export default defineComponent({
  name: "CreatePost",
  props: {
    modelValue: {
      type: Object,
      default: () => ({}),
    },
  },
  setup(props, { emit }){
    const theModel = computed({
      get: () => props.modelValue,
      set: (value) => emit('update:modelValue', value),
    }
    );

    let tags = ref(['test']);

    // Returns a decision on whether the tags field
    // should be disabled
    let tagsDisabled = computed(() => {
        console.log(tags.value.length)
        if(tags.value.length >= 4){
            return true;
        }
        else{
            return false;
        }
    });

    // Operations on the tags
    function removeTag(tagToRemove){
        tags.value = tags.value.filter(tag => tag != tagToRemove)
    }

    function addTag(){
        // Add a catch when the tag exists already
        tags.value.push(props.modelValue.newTag);
        theModel.value.newTag = '';
    }


    return { tags, removeTag, addTag, theModel, tagsDisabled }
  }
});
</script>
<style scoped lang="scss">
@import "@/assets/scss/main.scss";

.create-post{
    width: 800px;
    height: 300px;
    background-color: #fff;
    left: 50%;
    transform: translate(-50%, 150px);
    position: absolute;
    border-radius: $radius;
    padding: 15px;
    display: flex;
    flex-direction: row;
}

.create-post-wrapper{
    width: 100%;
    height: 100vh;
    position: fixed;
    z-index: 99;
}

.upload-picture{
    width: 40%;
    height: 100%;
    background-color: #f0f0f0;
    border-radius: $radius;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    img{
        width: 30px;
    }
    span{
        color: #858585;
        font-size: 0.9rem;
        margin-top: 15px;
    }
}

.form-title{
    margin-left: 20px;
    font-size: 1.2rem;
}

form{
    width: 60%;
    height: 100%;
    padding: 20px;
    box-sizing: border-box;
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 0.2fr 0.8fr;
    textarea{
        resize: none;
        height: 100%;
    }
    input{
        height: 40px;
        border-radius: 4px;
        box-sizing: border-box;
    }
    input:first-of-type, textarea{
        margin-right: 10px;
    }
    textarea, input{
        box-sizing: border-box;
        padding: 15px;
        border: 1px solid #c5c5c5;
        border-radius: 4px;
        background-color: #f8f8f8;
    }
    input:focus, textarea:focus{
        border-color: $link;
        outline: 0 none;
        background-color: #fff;
    }
}

.right-bottom-box{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
}

.tags-wrapper{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    box-sizing: border-box;
    width: 200px;
}

.tag{
    display: block;
    width: auto;
    margin: 0 5px 5px 0;
}

.tag:hover{
    text-decoration: line-through;
}

.button-wrapper{
    display: flex;
    flex-direction: row;
    align-items: flex-start;
}

input:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

input:disabled:focus{
    border-color: #c5c5c5;
}

.input--error{
    border-color: #fc5a5a;
}
</style>
