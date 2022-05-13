<template>
    <div style="position:relative" v-bind:class="{'open':openSuggestion}">
    <input class="form-control" type="text" v-model="selection"/>
    <ul class="dropdown-menu" style="width:100%">
        <li v-for="suggestion in matches">
            <a href="#">{{ suggestion }}</a>
        </li>
    </ul>
</div>
</template>
<script>
export default {
  props: {
    suggestions: {
        type: Array,
        required: true
    },
    selection: {
        type: String,
        required: true,
        twoWay: true
    }
  },
  data: {
    return() {
        open: false,
        current: 0
    }
  },
  computed: {
    matches() {
        return this.suggestions.filter((str) => {
            return str.indexOf(this.selection) >= 0;
        });
    },
    openSuggestion() {
        return this.selection !== "" &&
                this.matches.length != 0 &&
                this.open === true;
    }
  }
}
</script>
