<template>
  <div class="container">
    <b-list-group>
      <b-list-group-item
      v-for="(mission, index) in missions" :key="index"
      >
        {{ mission }}
      </b-list-group-item>
    </b-list-group>
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
