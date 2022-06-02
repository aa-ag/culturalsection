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
    <div>{{ missions }}</div>
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
  name: 'Directory',
  data() {
    return {
      missions: '',
    };
  },
  methods: {
    getMission(payload) {
      const path = 'http://localhost:5000/directory';
      axios.get(path, payload)
        .then((res) => {
          this.missions = res.data.missions;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        });
    },
    initForm() {
      this.getMissionForm.homecountry = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        homecountry: this.getMissionForm.homecountry,
      };
      this.addMission(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
  },
};
</script>
