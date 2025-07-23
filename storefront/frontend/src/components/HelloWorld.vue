<template>
  <div>
    <ul>
      <li v-for="collection in collections" :key="collection.id"> {{ collection.title }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: 'HelloWorld',
  data() {
    return {
      collections: []
    };
  },
  created() {
    axios.get('http://127.0.0.1:8000/collections/')
      .then(response => {
        this.collections = response.data;
      })
      .catch(error => {
        console.log(error);
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
