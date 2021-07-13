<template>
  <div id="app">
    <!-- v-if statement hides the navigation on the log in page -->
    <div id="nav" v-if="['LogIn'].indexOf($route.name) == -1">
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link>
    </div>
    <router-view>
    </router-view>
  </div>
</template>
