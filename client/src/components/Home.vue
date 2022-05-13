<template>
  <div class="container">
    <label for="exampleDataList" class="form-label">Datalist example</label>
    <input class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Type to search...">
    <datalist id="datalistOptions">
      <option value="San Francisco"></option>
      <option value="New York"></option>
      <option value="Seattle"></option>
      <option value="Los Angeles"></option>
      <option value="Chicago"></option>
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
