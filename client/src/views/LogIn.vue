<template>
  <div class="login">
      <img src="@/assets/icons/ig-white.svg" class="insta-logo login-icon">
      <div class="login-box">
          <h1>Welcome to Instagram.</h1>
          <span class="small-text">Choose any option below to log in or sign up.</span>
          <button class="login-option login-option--google">
              <img src="@/assets/icons/google.svg" class="sm-icon">
              Continue with Google
          </button>
          <button class="login-option login-option--twitter">
              <img src="@/assets/icons/twitter-white.svg" class="sm-icon">
              Continue with Twitter
          </button>
          <span class="small-text or-text">or..</span>
          <button class="login-option login-option--test">Use the test account</button>
      </div>
  </div>
</template>
<style lang="scss" scoped>
@import "../assets/scss/main.scss";

// Box in the center with all the content
.login-box{
    height: 500px;
    width: 500px;
    background-color: #fff;
    border-radius: $radius;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-sizing: border-box;
    padding: 60px;
}

// The main container
.login{
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

// Instagram logo in white
.login-icon{
    transform: translateY(-30px);    
}

// Font settings
h1{
    font-size: 1.41em;
    margin: 0 0 12px 0;
}

.small-text{
    font-size: 0.85em;
}

.small-text:nth-of-type(2){
    margin: 35px 0;
}


// Log in buttons
.login-option{
    width: 85%;
    height: 50px;
    margin: 10px 0;
    border: none;
    border-radius: $radius-button;
    font-size: 0.93em;
    position: relative;
    transition: background-color 0.15s;
}

.login-option--google{
    background-color: #f3f3f3;
}

.login-option--twitter{
    background-color: #6BB8FF;
    color: #fff;
}

.login-option--test{
    background-color: $black;
    color: #fff;
    transition: color 0.6s 0.5s;
}

.login-option:nth-of-type(1){
    margin-top: 40px;
}

// Proper sizing for social media icons
.sm-icon{
    height: 20px;
    position: absolute;
    left: 0;
    margin-left: 20px;
}

// Add hover animation
.login-option--google:hover{
    background-color: darken(#f3f3f3, 5%);
}

.login-option--twitter:hover{
    background-color: darken(#6BB8FF, 5%);
}

.login-option--test:hover{
    color: transparent;
}

.login-option--test:hover::before{
    opacity: 100;
    background-position: right center;
    color: rgb(255, 255, 255);
}

// Funsies
.login-option--test::before{
    content:"Let's begin";
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, #ffcc3e, #FF6948, #5D25FC);
    position: absolute;
    left: 0;
    top: 0;
    border: none;
    border-radius: $radius-button;
    opacity: 0;
    transition: opacity 0.5s, background-color 0.5s 0.5s, color 0.6s 0.5s ease-in-out;
    background-size: 150% auto;
    display: flex;
    justify-content: center;
    align-items: center;
    color: rgba(255, 255, 255, 0);
    box-sizing: border-box;
    padding-top: 0.3em;
}
</style>