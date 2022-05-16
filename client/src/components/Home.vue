<template>
  <div class="container" id="datalistContainer">
    <label for="homeDataList" class="form-label">Select a City</label>
    <input class="form-control"
      list="datalistOptions"
      id="homeDataList"
      placeholder="Type to search...">
    <datalist id="datalistOptions">
      <option value="Washington, D.C."></option>
      <option value="Chicago"></option>
      <option value="Nashville"></option>
    </datalist>
    <div class="form-check">
      <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" checked>
      <label class="form-check-label" for="flexRadioDefault1">
        Cultural Events Calendar
      </label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2">
      <label class="form-check-label" for="flexRadioDefault2">
        Embassies &amp; Consulates Directory
      </label>
    </div>
  
    <button type="submit" class="btn btn-primary">Search</button>
  </div>
</template>
<style>
</style>

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
