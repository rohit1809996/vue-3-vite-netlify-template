<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> 
    <!-- <router-link to="/Prediction"> Prediction </router-link> -->
  </nav>
  <router-view/>
</template>

<style>
body {
  background-image: 'Homepage bg1.png' 
   style="width:100%" ;
  /* background-size: cover; */
  background-attachment: fixed;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-weight: bold;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0b59a6;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  font-size:40;
  color: #296aab;
}

nav a.router-link-exact-active {
  color: #0b0ea6;
}
</style>
