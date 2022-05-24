<template>
  <div class="container">
    <!-- <form>
      <div class="mb-2">
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
      </div>
      <button type="submit" class="btn btn-primary">Save</button>
    </form> -->
    <h3>Add a mission</h3>
    <b-form @submit="submit">
    <b-form-group id="input-group-1" label="Home country" label-for="input-1">
      <b-form-textarea
      id="input-1"
      type="text"
      v-model="dataentry.home_country"
      placeholder="Enter a home country here"
      ></b-form-textarea>
    </b-form-group>
    <b-form-group id="input-group-2" label="Destination City" label-for="input-2">
      <b-form-textarea
      id="input-2"
      type="text"
      v-model="dataentry.destination_city"
      placeholder="Type a destination city here">
      </b-form-textarea>
    </b-form-group>
    <b-button pill v-on:Click="submit" id="button-1" type="submit" variant="dark">Submit</b-button>
    </b-form>
  </div>
</template>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
</style>