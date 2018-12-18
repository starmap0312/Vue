<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h1>name: {{ this.$route.name }}</h1>
    <!-- http://localhost:8080/#/HelloWorld/somepath -->
    <h1>segment: {{ this.$route.params.segment }}</h1>
    <!-- http://localhost:8080/#/HelloWorld/somepath?param1=3 -->
    <h1>query: {{ this.$route.query.param1 }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Hello World'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-weight: normal;
}
</style>
