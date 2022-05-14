<template>
  <div class="container">
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Embassy or Consulate" aria-label="Embassy or Consulate">
      <span class="input-group-text">of</span>
      <input type="text" class="form-control" placeholder="Canada" aria-label="Canada">
      <span class="input-group-text">in</span>
      <input type="text" class="form-control" placeholder="the United States" aria-label="the United States">
      <button type="submit" class="btn btn-primary">Search</button>
    </div>
    <div id="directoryHelp" class="form-text">Embassy/Country/Country or Consulate/Country/City</div>
    <div id="directoryHelp" class="form-text">Embassy/Canada/Australia or Consulate/India/Chicago</div>
  </div>
</template>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
</style>