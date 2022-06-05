<template>
  <div class="container">
    <p>Directory</p>
    <b-form-input v-model="country" placeholder="Enter a country"></b-form-input>
    <div class="mt-2">{{ result }}</div>
  </div>
</template>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
</style>
<script>
export default {
  name: 'Directory',
  data() {
    return {
      country: '',
      result: '',
    };
  },
};
</script>
