<template>
  <div class="container">
    <label for="homeDataList" class="form-label">Select a City</label>
    <input class="form-control"
      list="datalistOptions"
      id="homeDataList"
      placeholder="Type to search...">
    <datalist id="datalistOptions">
      <option value="Chicago"></option>
      <option value="San Francisco"></option>
      <option value="New York"></option>
      <option value="Nashville"></option>
      <option value="Miami"></option>
      <option value="Washington, D.C."></option>
    </datalist>
  </div>
  <div class="container">
    <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4">
      <p class="col-md-4 mb-0 text-muted">&copy; 2022 Cultural Section, Inc</p>

      <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
        <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
      </a>

      <ul class="nav col-md-4 justify-content-end">
        <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">About</a></li>
        <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">Legal</a></li>
      </ul>
    </footer>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
        example_cities: [],
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/";
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
