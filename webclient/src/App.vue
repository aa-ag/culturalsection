<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-toggle class="mr-auto" target="nav-collapse"></b-navbar-toggle>
      <b-navbar-brand href="/">Cultural Section</b-navbar-brand>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/help">Help</b-nav-item>
          <b-nav-item href="/browse">Browse</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item href="/missions" right>Diplomatic Missions</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div class="divider"></div>
    <router-view/>
    <!-- <div class="divider"></div>
    <footer class="flex-shrink-0 py-4 bg-light">
        <div class="text-center small" id="copyright">&copy; 2022</div>
        <div class="text-center small" id="more">
          <a href="/legal">Legal</a>
          <small>|</small>
          <a href="/about">About</a>
      </div>
    </footer> -->
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
#copyright {
  margin-top: 0.8rem;
}
#more > * {
  padding: 0.25rem;
  color: rgba(166, 166, 166, 0.871);
}
</style>
