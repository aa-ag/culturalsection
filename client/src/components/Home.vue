<template>
  <div class="container">
    <label for="homeDataList" class="form-label">Select a City</label>
    <input class="form-control" list="datalistOptions" id="homeDataList" placeholder="Type to search...">
    <datalist id="datalistOptions">
      <option value="Chicago"></option>
      <option value="San Francisco"></option>
      <option value="New York"></option>
      <option value="Nashville"></option>
      <option value="Miami"></option>
      <option value="Washington, D.C."></option>
    </datalist>
  </div>
</template>

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
