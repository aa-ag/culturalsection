<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
    <a class="navbar-brand" href="#">Cultural Section</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a router-link to="/info">Info</a>
        </li>
        <li class="nav-item">
          <a router-link to="/legal">Legal</a>
        </li>
      </ul>
    </div>
  </nav>
  <router-view />
</template>

<style>

</style>
