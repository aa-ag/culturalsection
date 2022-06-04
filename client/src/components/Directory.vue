<template>
  <div class="container">
    <p>Directory</p>
    <b-form-input v-model="text" placeholder="Enter a country"></b-form-input>
    <div class="mt-2">{{ text }}</div>
  </div>
</template>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
</style>
<script>
</script>
