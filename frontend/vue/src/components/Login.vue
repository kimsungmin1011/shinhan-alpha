<template>
    <div>
      <h2 v-if="isLoginForm">Login</h2>
      <h2 v-else>Sign Up</h2>
      <form @submit.prevent="handleSubmit">
        <label>
          Email:
          <input type="email" v-model="email" required />
        </label>
        <br />
        <label>
          Password:
          <input type="password" v-model="password" required />
        </label>
        <br />
        <button type="submit">{{ isLoginForm ? 'Login' : 'Sign Up' }}</button>
      </form>
      <div v-if="errorMessage">{{ errorMessage }}</div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        password: '',
        isLoginForm: true,
        errorMessage: '',
      };
    },
    methods: {
      handleSubmit() {
        if (this.isLoginForm) {
          // Login logic goes here
        } else {
          // Sign up logic goes here
        }
      },
    },
  };
  </script>
  