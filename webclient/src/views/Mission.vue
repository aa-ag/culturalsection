<template>
  <div class="container">
    <h1>{{ country }}</h1>
    <!-- {{ cities }} -->
    <b-button
    @click="$router.go(-1)"
    variant="primary"
    >
     Back
    </b-button>
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
      cities: [],
    };
  },
  methods: {
    getCities() {
      const path = 'http://localhost:5000/mission';
      axios.get(path)
        .then((res) => {
          this.cities = res.data.cities;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getCities();
  },
};
</script>
