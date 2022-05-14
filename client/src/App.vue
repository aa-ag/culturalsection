<template>
  <nav class="navbar navbar-expand-md navbar-light bg-light">
    <a class="navbar-brand" href="#">Cultural Section</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#">Help</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Contact</a>
        </li>
      </ul>
      <ul class="navbar-nav flex-row flex-wrap ms-md-auto">
        <a class="btn btn-dark" href="#" role="button">Diplomatic Missions</a>
      </ul>
    </div>
  </nav>
  <div class="divider"></div>
  <router-view/>
  <div class="divider"></div>
  <div class="container mt-auto" id="footer">
    <footer class="d-flex flex-wrap justify-content-between align-items-center py-1 my-2">
      <p class="col-md-4 mb-0 text-muted">&copy; 2022</p>
      <ul class="nav col-md-4 justify-content-end">
        <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">About</a></li>
        <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">Legal</a></li>
      </ul>
    </footer>
  </div>
</template>

<style>
.navbar {
  padding-top: 0.6rem;
  padding-bottom: 0.6rem;
  padding-right: 0.5rem;
}
.navbar-brand {
  margin-left: 1rem;
}
</style>
