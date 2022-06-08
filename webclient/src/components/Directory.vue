<template>
  <div class="container">
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-input list="countries-list"></b-form-input>
      <datalist id="countries-list">
        <option v-for="country in countries" v-bind:key="country.name">
          {{ country }}
        </option>
      </datalist>
    <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
    <div>{{ count }}</div>
    <div v-for="mission in missions" v-bind:key="mission.id">
      <div>{{ mission }}</div>
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
import axios from 'axios';

export default {
  data() {
    return {
      getMissionForm: {
        home_country: '',
      },
      countries: ['USA', 'France', 'Belgium', 'Argentina'],
      count: '',
      missions: '',
    };
  },
  methods: {
    getMission(payload) {
      const path = 'http://localhost:5000/directory';
      axios.post(path, payload)
        .then((res) => {
          this.count = res.data.count;
          this.missions = res.data.missions;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    initForm() {
      this.getMissionForm.home_country = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        home_country: this.getMissionForm.home_country,
      };
      this.getMission(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
  },
};
</script>
