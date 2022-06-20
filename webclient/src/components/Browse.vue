<template>
  <div class="container">
    <b-list-group>
      <b-list-group-item class="d-flex justify-content-between align-items-center"
      v-for="(count, country, index) in missions" :key="index"
      >
        {{ country }}
        <b-badge variant="primary" pill>{{ count }}</b-badge>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
.list-group {
  max-width: 450px;
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
      const path = 'http://localhost:5000/browse';
      axios.get(path)
        .then((res) => {
          this.missions = res.data.missions;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMissions();
  },
};
</script>
