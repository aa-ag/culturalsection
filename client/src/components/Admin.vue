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
          v-model="addMissionForm.homecountry"
          required
          placeholder="Enter your mission's home country">
      </b-form-input>
      </b-form-group>
      <b-form-group
        id="form-destinationcity-group"
        label="Destination city"
        label-for="form-destinationcity-input">
          <b-form-input
            id="form-destinationcity-input"
            type="text"
            v-model="addMissionForm.destinationcity"
            required
            placeholder="Enter your mission's destination city">
          </b-form-input>
        </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
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
      addMissionForm: {
        homecountry: '',
        destinationcity: '',
      },
    };
  },
  methods: {
    addMission(payload) {
      const path = 'http://localhost:5000/admin';
      axios.post(path, payload)
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    initForm() {
      this.addMissionForm.homecountry = '';
      this.addMissionForm.destinationcity = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        homecountry: this.addMissionForm.homecountry,
        destinationcity: this.addMissionForm.destinationcity,
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
