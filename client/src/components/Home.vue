<template>
  <div class="container">
    <label for="input-with-list">Pick a city</label>
    <b-form-input list="input-list" id="input-with-list"></b-form-input>
    <b-form-datalist id="input-list" :options="options"></b-form-datalist>
    <button type="submit" class="btn btn-primary" id="searchButton">View Calendar</button>
  </div>
</template>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
#searchButton {
  margin-top: 0.6rem;
}
</style>
<script>
export default {
  data() {
    return {
      options: ['Nashville', 'Chicago', 'Miami', 'Washington, D.C.', 'New York'],
    };
  },
};
</script>
