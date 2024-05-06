<template>
  <div class="container-fluid welcome-container">
    <div class="content p-3">
      <div class="header">
        <img src="../assets/Logo.svg" alt="Logo" class="logo" />
        <h1>Welcome to Walkley</h1>
      </div>
      <p class="mb-4">
        Track your progress and join a community of fitness enthusiasts in 3
        steps.
      </p>
      <div class="steps-container mb-4">
        <div class="row icon-row">
          <div class="col-4">
            <img
              src="../assets/membership_icon.svg"
              alt="Membership Icon"
              class="step-icon"
            />
          </div>
          <div class="col-4">
            <img
              src="../assets/tracks_icon.svg"
              alt="Trail Icon"
              class="step-icon"
            />
          </div>
          <div class="col-4">
            <img
              src="../assets/activity_icon.svg"
              alt="Activity Icon"
              class="step-icon"
            />
          </div>
        </div>
        <div class="row step-row">
          <div class="col-12 col-md-4 step">
            <h3>1. Sign up and choose a payment plan</h3>
          </div>
          <div class="col-12 col-md-4 step">
            <h3>2. Upload your GPX trail data</h3>
          </div>
          <div class="col-12 col-md-4 step">
            <h3>3. View your trail or your friends trails!</h3>
          </div>
        </div>
      </div>
      <button class="btn btn-primary register-btn" @click="registerNewAccount">
        Register
      </button>
      <div class="form-field go-to-login">
        <span>Already have an account?</span>&nbsp;
        <a href="#" @click="alreadyHaveAccount">Login</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WelcomePage',
  methods: {
    registerNewAccount() {
      this.$router.push('/register')
    },
    alreadyHaveAccount() {
      this.$router.push('/login')
    },
  }
}
</script>
  
<style scoped>
.welcome-container {
  background-image: url('../assets/brian-erickson-XFneC_rHR48-unsplash.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  
}

.content {
  text-align: center;
  background-color: rgba(255, 255, 255);
  border-radius: var(--border-radius);
  padding: 20px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
  position: relative;
  z-index: 1;
  max-width: 800px;
}

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
}

.register-btn {
    background-color: var(--app-green);
    color: var(--l1-color);
    padding: var(--button-padding-vertical) var(--button-padding-horizontal);
    border: none;
    border-radius: var(--border-radius);
    cursor: pointer;
    transition: background-color var(--transition-speed) ease;
}

.register-btn:hover {
    background-color: var(--app-green-hover);
}

.register-btn:active {
    background-color: var(--app-green-pressed);
}

.mb-4 {
  margin-bottom: 1rem;
}

.steps-container {
  border-radius: var(--border-radius);
  padding: 20px;
}

.step {
  padding: 10px;
  text-align: center;
}

.step-icon {
  max-width: 50px;
  max-height: 50px;
}

.logo {
  max-width: 100px;
  margin-right: 1rem;
}

.go-to-login {
  margin-top: 1rem;
}


</style>
