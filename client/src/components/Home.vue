<template>
  <div class="container">
    <div v-for="(city, index) in example_cities" :key="index">
      <b>{{ city.name }}</b>
      <p>{{ city.consulate }}</p>
    </div>
  </div>
</template>
<style>
 .container {
    margin-top: 60px
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