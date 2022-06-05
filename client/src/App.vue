<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="/">Cultural Section</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/help">Help</b-nav-item>
          <b-nav-item href="/contact">Contact</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item href="/missions" right>Diplomatic Missions</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div class="divider"></div>
    <router-view/>
    <div class="divider"></div>
    <footer class="fixed-bottom">
      <div class="p-2">
        <div class="text-center p3">&copy; 2022</div>
        <div class="text-center p3 muted"><a href="/legal">Legal</a></div>
        <div class="text-center p3 muted"><a href="/about">About</a></div>
      </div>
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
.divider {
  height: 1.1rem;
  background-color: rgba(0, 0, 0, .1);
  border: solid rgba(0, 0, 0, .15);
  border-width: 1px 0;
  box-shadow: inset 0 0.5em 1.5em rgb(0 0 0 / 10%), inset 0 0.125em 0.5em rgb(0 0 0 / 15%);
}
</style>
