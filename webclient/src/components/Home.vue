<template>
  <div class="container">
    <b-card-group deck>
      <b-card header="Foreing diplomatic missions in the United States">
        <b-list-group class="col-md-8 mx-auto">
          <b-list-group-item
          class="d-flex justify-content-between align-items-center"
          v-for="(count, country, index) in missions" :key="index"
          >
          <a :href="'/mission'" v-on:click="getClickData(country)">{{ country }}</a>
          <b-badge variant="primary" pill>{{ count }}</b-badge>
        </b-list-group-item>
        </b-list-group>
      </b-card>
    </b-card-group>
  </div>
</template>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
.list-group {
  max-width: 450px;
  left: auto;
}
</style>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      missions: [],
    };
  },
  methods: {
    getMissions() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.missions = res.data.missions;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getClickData(country) {
      // eslint-disable-next-line
      console.error(country);
    },
  },
  created() {
    this.getMissions();
  },
};
</script>
