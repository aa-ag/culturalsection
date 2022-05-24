<template>
  <div class="container">
    
  </div>
</template>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
</style>
<script>
import axios from "axios";
export default{
  data(){
    return {
      add: {
       home_country: "",
       destination_city: "",
      },
    };
  },
  methods: {
    submit:function() {
      const path = 'http://127.0.0.1:5000/add'
      axios.post(path, {
        name: this.add.home_country,
        department: this.add.destination_city,
        }
      )
      .then(response => {
        console.log(response);
      })
      .catch(err =>{
        console.log(err);
      });
    },
  }
}
</script>