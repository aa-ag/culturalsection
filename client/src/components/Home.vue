<template>
  <div class="container">
    <!-- <div v-for="(city, index) in example_cities" :key="index">
      <b>{{ city.name }}</b>
      <p>{{ city.consulate }}</p>
    </div> -->
    <div class="search-container">
      <form class="search-form">
        <input id="home-search-bar" type="search" placeholder="Enter a City">
      </form>
    </div>
  </div>
</template>
<style>
 .container {
    margin-top: 60px
 }
 .search-container .search-form {
    width: 75%;
    text-align: center;
 }
 #home-search-bar {
    width: 100%;
 }
</style>
<script>
import axios from 'axios'
export default {
  name: 'Home',
  data() {
    return {
        example_cities: [],
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.example_cities = res.data.example_cities;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>