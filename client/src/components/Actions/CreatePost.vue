<template>
    <form class="create-post-wrapper dark-bg">
        <div class="flying-wrapper create-post">
            <div class="upload-picture">
                <img src="@/assets/icons/close-circle.svg" alt="Close" v-if="previewImage" class="remove-upload"
                @click="removeImage">
                <img :src="previewImage" alt="Uploaded image" class="upload-preview" v-if="previewImage">
                <label for="image-upload"><img src="@/assets/icons/picture.svg" alt="Upload icon"> Upload Image</label>
                <input id="image-upload" type="file" accept="image/png,image/jpeg" @change="addImage">
            </div>
            <div class="picture-info">
                <span class="form-title">Upload a new image</span>
                <div class="form-inputs-wrapper">
                    <input placeholder="Title" maxlength="30">
                    <input placeholder="Tags (max. 4)" v-model="tagin"
                    v-on:update:title="theModel.newTag = $event"
                    v-on:keydown.enter.prevent="addTag()"
                    :disabled="tagsDisabled"
                    maxlength="10"
                    v-bind:class="{ tagerr: tagError }">
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
                </div>
            </div>
        </div>
    </form>
</template>
<script>
import { defineComponent, ref, computed, watch } from "vue";

export default defineComponent({
  name: "CreatePost",
  setup(){
    let tags = ref(['test']);
    let previewImage = ref(null);
    let tagError = ref(false);
    let tagin = ref('')

    watch(tagin, (newTag) => {
        if(tags.value.includes(newTag)){
            tagError.value = true;
        }else{
            tagError.value = false;
        }
    });

    // Returns a decision on whether the tags field
    // should be disabled
    let tagsDisabled = computed(() => {
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
        // If the tag exists already show an error and don't add it
        // to the list, otherwise add and empty the input
        if(!tagError.value){
            tags.value.push(tagin.value);
            tagin.value = "";
        }
    }

    // Preview the files
    function addImage(event){
        let files = event.target.files
        // If the file exists, change the variable
        if (files && files[0]) {
            previewImage.value = URL.createObjectURL(files[0])
        }
    }

    function removeImage(){
        previewImage.value = null;
    }

    return { tags, removeTag, addTag, tagsDisabled, addImage, previewImage, removeImage, tagError, tagin }
  }
});
</script>
<style scoped lang="scss">
@import "@/assets/scss/main.scss";

.create-post{
    width: 800px;
    height: 300px;
    background-color: #fff;
    border-radius: $radius;
    padding: 15px;
    display: flex;
    flex-direction: row;
    transform: translateY(120px);
}

.create-post-wrapper{
    width: 100%;
    height: 100vh;
    position: fixed;
    display: flex;
    justify-content: center;
    z-index: 99;
}

.upload-picture{
    width: 40%;
    height: 100%;
    background-color: #f0f0f0;
    border-radius: $radius;
    transition: background-color 0.3s;
    position: relative;
    label{
        color: #acacac;
        font-size: 0.85rem;
        transition: color 0.3s;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        img{
            width: 24px;
            opacity: 0.6;
            transition: opacity 0.2s;
            margin-bottom: 15px;
        }
    }
    input[type="file"] {
        display: none;
    }
}

.upload-picture:hover{
    background-color: #e6e6e6;
    label img{
        opacity: 0.9;
    }
    label{
        color: #9b9b9b;
    }
}

.upload-preview{
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: $radius;
    z-index: 2;
    object-fit: cover;
}

.remove-upload{
    position: absolute;
    z-index: 3;
    margin: 15px;
    width: 24px;
    opacity: 0.5;
    cursor: pointer;
    transition: 0.2s;
}

.remove-upload:hover{
    opacity: 0.8;
}

// The form
.form-title{
    margin-left: 20px;
    font-size: 1.2rem;
}

.form-inputs-wrapper{
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

.tagerr:focus{
    border: 1px solid #ff4141!important;
    color: #c75151;
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
