<template>
  <form>
  <div class="form-group">
    <label for="exampleFormControlSelect1">Select a City</label>
    <select class="form-control" id="exampleFormControlSelect1">
      <option>Nashville, TN</option>
      <option>Chicago, IL</option>
      <option>Tampa, FL</option>
    </select>
  </div>
</form>
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