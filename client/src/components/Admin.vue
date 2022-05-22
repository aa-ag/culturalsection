<template>
  <div class="container">
    <!-- 
      bring elements from db:
      - flag
      - team
      - address
      - services
      - faqs
      - social channels
      - contact
     -->
    <form>
      <div class="mb-3">
        <label for="missionInfo" class="form-label">Team</label>
        <input type="email" class="form-control" id="missionInfo" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="missionInfo" class="form-label">Address</label>
        <input type="email" class="form-control" id="missionInfo" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="missionInfo" class="form-label">Contact</label>
        <input type="email" class="form-control" id="missionInfo" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="missionInfo" class="form-label">Services</label>
        <input type="password" class="form-control" id="missionInfo">
      </div>
      <div class="mb-3">
        <label for="missionInfo" class="form-label">FAQs</label>
        <input type="password" class="form-control" id="missionInfo">
      </div>
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