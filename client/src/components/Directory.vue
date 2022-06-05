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
          v-model="getMissionForm.home_country"
          required
          placeholder="Enter your mission's home country">
      </b-form-input>
    </b-form-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
    <div class="mt-2">{{ result }}</div>
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
      result: '',
    };
  },
  methods: {
    getMission(payload) {
      const path = 'http://localhost:5000/directory';
      axios.get(path, payload)
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
