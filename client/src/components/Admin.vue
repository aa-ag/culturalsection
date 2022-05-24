<template>
  <div class="container">
    <form>
      <div class="mb-2">
        <label for="homeCountry" class="form-label">Home Country</label>
        <input type="email" class="form-control" id="homeCountry">
      </div>
      <div class="mb-2">
        <label for="destinationCity" class="form-label">Destination City</label>
        <input type="email" class="form-control" id="destinationCity">
      </div>
      <!-- <div class="mb-2">
        <label for="missionInfo" class="form-label">Team</label>
        <input type="email" class="form-control" id="missionInfo" aria-describedby="emailHelp">
      </div>
      <div class="mb-2">
        <label for="missionInfo" class="form-label">Address</label>
        <input type="email" class="form-control" id="missionInfo" aria-describedby="emailHelp">
      </div>
      <div class="mb-2">
        <label for="missionInfo" class="form-label">Contact</label>
        <input type="email" class="form-control" id="missionInfo" aria-describedby="emailHelp">
      </div>
      <div class="mb-2">
        <label for="missionInfo" class="form-label">Services</label>
        <input type="password" class="form-control" id="missionInfo">
      </div>
      <div class="mb-2">
        <label for="missionInfo" class="form-label">FAQs</label>
        <input type="password" class="form-control" id="missionInfo">
      </div> -->
      <button type="submit" class="btn btn-primary">Save</button>
    </form>
  </div>
</template>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
</style>
<script>
import axios from "axios";
export default{
  data(){
    return {
      add: {
       home_country: "",
       destination_city: "",
      },
    };
  },
  methods: {
    submit:function() {
      const path = 'http://127.0.0.1:5000/add'
      axios.post(path, {
        name: this.add.home_country,
        department: this.add.destination_city,
        }
      )
      .then(response => {
        console.log(response);
      })
      .catch(err =>{
        console.log(err);
      });
    },
  }
}
</script>