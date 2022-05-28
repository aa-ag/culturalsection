<template>
  <div id="app">
    <b-navbar toggleable="lg" type="navbar-dark bg-dark" variant="info">
      <b-navbar-brand href="/">Cultural Section</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Help</b-nav-item>
          <b-nav-item href="#">Contact</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item  right>
            Diplomatic Missions
          </b-nav-item >
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div class="divider"></div>
    <router-view/>
    <div class="divider"></div>
    <div class="footer" id="footer">
      <footer class="d-flex flex-wrap justify-content-between align-items-center">
        <p class="col-md-4 mb-0 text-muted">&copy; 2022</p>
        <ul class="nav col-md-4 justify-content-end">
          <li class="nav-item"><a href="about" class="nav-link px-2 text-muted">About</a></li>
          <li class="nav-item"><a href="legal" class="nav-link px-2 text-muted">Legal</a></li>
        </ul>
      </footer>
    </div>
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
footer {
  padding: 1rem;
}
.footer {
  font-size: small;
}
.divider {
  height: 1.1rem;
  background-color: rgba(0, 0, 0, .1);
  border: solid rgba(0, 0, 0, .15);
  border-width: 1px 0;
  box-shadow: inset 0 0.5em 1.5em rgb(0 0 0 / 10%), inset 0 0.125em 0.5em rgb(0 0 0 / 15%);
}
</style>
