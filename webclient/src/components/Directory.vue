<template>
  <div class="container">
    <b-form @submit="onSubmit" @reset="onReset" class="inline">
      <b-form-group
        id="form-homecountry-group"
        label="Embassy or Consulate of"
        label-for="form-homecountry-input">
        <b-form-input
          id="form-homecountry-input"
          type="text"
          v-model="getMissionForm.home_country"
          required
          placeholder="Home country">
      </b-form-input>
    </b-form-group>
    <b-form-group
      id="form-destination_city-group"
      label="In"
      label-for="form-destination_city-input">
      <b-form-input
        id="form-destination_city-input"
        type="text"
        v-model="getMissionForm.destination_city"
        required
        placeholder="Destination city">
      </b-form-input>
    </b-form-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-form-text id="directory-helper">
      Example:
      search for US consulates in Spain's capital by entering "USA" and "Madrid"
    </b-form-text>
    </b-form>
    <p>Alternatively, <a href="#">browse manually</a> or using our <a href="#">diplomap</a></p>
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
        destination_city: '',
      },
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
      this.getMissionForm.destination_city = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        home_country: this.getMissionForm.home_country,
        destination_city: this.getMissionForm.destination_city,
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
