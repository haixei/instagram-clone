<template>
  <div id="app">
    <!-- v-if statement hides the navigation on the log in page -->
    <ActionsNav id="nav" v-if="['LogIn'].indexOf($route.name) == -1">
    </ActionsNav>
    <router-view>
    </router-view>
  </div>
</template>

<script lang="ts">
import ActionsNav from "./components/Navigation/ActionsNav.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "App",
  components: {
    ActionsNav
  }
});
</script>
<style lang="scss" scoped>
footer{
  height: 150px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  p{
    color: #a1a1a1;
  }
}
</style>