<template>
  <div class="container">
    <div>{{ count }}</div>
    <div>{{ missions }}</div>
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
  name: 'Calendar',
  data() {
    return {
      missions: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/calendar';
      axios.get(path)
        .then((res) => {
          this.count = res.data.count;
          this.missions = res.data.missions;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
