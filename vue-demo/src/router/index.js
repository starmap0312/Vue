import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/HelloWorld/:segment',
      name: 'HelloWorld',
      component: HelloWorld,
      props: (route) => ({ prop1: route.params.segment })
    }
  ]
})
