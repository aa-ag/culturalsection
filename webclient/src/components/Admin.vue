<template>
  <div class="container">
    <div id="addMissionModal">
      <b-button v-b-modal.modal-1>
        Add a new mission
      </b-button>

      <b-modal id="modal-1" title="addMission">
        <p class="my-4">Modal working!</p>
      </b-modal>
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
      addMissionForm: {
        home_country: '',
        destination_city: '',
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
      this.addMissionForm.home_country = '';
      this.addMissionForm.destination_city = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        home_country: this.addMissionForm.home_country,
        destination_city: this.addMissionForm.destination_city,
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
