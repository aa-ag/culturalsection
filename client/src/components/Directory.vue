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
          v-model="getMissionsForm.homecountry"
          required
          placeholder="Enter your mission's home country">
        </b-form-input>
      </b-form-group>
      <b-button type="search" variant="primary">Search</b-button>
    </b-form>
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
      getMissionsForm: {
        homecountry: '',
      },
    };
  },
  methods: {
    getMissions(payload) {
      const path = 'http://localhost:5000/directory';
      axios.get(path, payload)
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    initForm() {
      this.getMissionsForm.homecountry = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        homecountry: this.getMissionsForm.homecountry,
      };
      this.getMissions(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
  },
};
</script>
