<template>
  <form>
    <div class="form-group">
      <input type="input" class="form-control" id="homeSearch" aria-describedby="homeSearchHelp" placeholder="Enter a City">
      <small id="homeSearchHelp" class="form-text text-muted">Only US cities for now.</small>
    </div>
    <button type="submit" class="btn btn-primary">Search</button>
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
  props: {
    suggestions: {
      type: Array,
      required: true,
    },
    selection: {
      type: String,
      required: true,
      twoWay: true,
    }
  }
};
</script>