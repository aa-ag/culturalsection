<template>
  <div class="container">
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group
        id="form-homecountry-group"
        label="Home country"
        label-for="form-homecountry-input">
        <b-form-input
          id="form-homecountry-input"
          type="text"
          v-model="getMissionForm.homecountry"
          required
          placeholder="Enter your mission's home country">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Search</b-button>
    </b-form>
    <div>
      {{ hc }}
    </div>
  </div>
</template>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
</style>
<script>
const axios = require('axios');

axios.get('http://localhost:5000/calendar').then(resp => {

    console.log(resp.data);
});
</script>
