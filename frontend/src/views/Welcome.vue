<template>
    <div class="snap-container">
        <div class="welcome-container">
            <div class="direct-welcome">
                <h1 class="app-name">Walkley</h1>
                <p class="app-name-sh mb-3">Your GPX manager</p>
                <div class="button-container">
                    <button class="btn-primary me-1" @click="registerNewAccount">Register</button>
                    <button class="btn-secondary-white ms-1" @click="alreadyHaveAccount">Login</button>
                </div>
            </div>
        </div>
        <div class="pitch-container">
            <div class="container pitch-grid-container">
                <div class="pitch-grid">
                    <div class="pitch-box p-5">
                        <div class="d-flex flex-row align-items-center"><img src="../assets/activity_icon.svg" alt="Activity Icon"/><span class="feature-name">Activity Center</span></div>
                        <p class="large-pitch-text">Manage and visualize your activities</p>
                    </div>
                    <div class="pitch-box p-5">
                        <div class="d-flex flex-row align-items-center"><img src="../assets/upload_icon.svg" alt="Upload icon"><span class="feature-name">Upload</span></div>
                        <p class="large-pitch-text">Upload your trails to the cloud</p>
                    </div>
                    <div class="pitch-box p-5">
                        <div class="d-flex flex-row align-items-center"><img src="../assets/community_icon.svg" alt="Community icon"><span class="feature-name">Community</span></div>
                        <p class="large-pitch-text">Share your activities and view your friends' activities</p>
                    </div>
                    <div class="pitch-box p-5 d-flex align-items-center">
                        <div class="d-flex flex-column align-items-end">
                            <p class="mega-large-pitch-text">Starting £1.99</p>
                            <p class="small-pitch-text clearMargin">/week</p>
                        </div>
                    </div>
                    <div class="buy-box p-5 d-flex flex-column align-items-start">
                        <p class="giga-large-pitch-text me-3">Convinced?</p>
                        <button class="btn-primary" @click="registerNewAccount">Register now</button>
                    </div>
                </div>
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

/* SM */
@media screen and (max-width: 576px) {
    .welcome-container {
        background-image: url('../assets/render_square.jpg');
    }

    .direct-welcome {
        align-items: center;
        justify-content: center;
        height: 100%;
    }

    .app-name {
        font-size: 4rem;
    }

    .pitch-container {
        height: auto;   
    }

    .pitch-grid-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding-top: 5rem;
        padding-bottom: 5rem;
    }
    
    .pitch-grid{
        grid-template-rows: 1fr;
        gap: 20px;
    }

}

/* MD */
@media screen and (max-width: 768px) and (min-width: 577px) {
    .welcome-container {
        background-image: url('../assets/render_square.jpg');
    }

    .direct-welcome {
        align-items: center;
        justify-content: center;
        height: 100%;
    }

    .app-name {
        font-size: 4rem;
    }

    .pitch-container {
        height: auto;   
    }

    .pitch-grid-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding-top: 5rem;
        padding-bottom: 5rem;
    }
    
    .pitch-grid{
        grid-template-rows: 1fr;
        gap: 20px;
    }
}

/* LG */
@media screen and (max-width: 992px) and (min-width: 769px) {
    .welcome-container {
        background-image: url('../assets/render_square.jpg');
    }

    .direct-welcome {
        align-items: center;
        justify-content: center;
        height: 100%;
    }

    .app-name{
        font-size: 4rem;
    }

    .pitch-container {
        height: auto;   
    }

    .pitch-grid-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding-top: 5rem;
        padding-bottom: 5rem;
    }
    
    .pitch-grid{
        grid-template-rows: 1fr;
        gap: 20px;
    }
    
}

/* XL */
@media screen and (max-width: 1200px) and (min-width: 993px) {
    .welcome-container {
        background-image: url('../assets/render_blur.jpg');
    }

    .direct-welcome {
        position: relative;
        top: 50%;
        left: 55%;
    }

    .app-name{
        font-size: 5rem;
    }

    .pitch-container {
        height: auto;   
    }

    .pitch-grid-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding-top: 5rem;
        padding-bottom: 5rem;
    }
    
    .pitch-grid{
        grid-template-rows: 1fr;
        gap: 20px;
    }
}

/* XXL */
@media screen and (min-width: 1201px) {
    .snap-container {
        scroll-snap-type: y mandatory;
    }

    .welcome-container {
        background-image: url('../assets/render_blur.jpg');
    }

    .direct-welcome {
        position: relative;
        top: 50%;
        left: 55%;
    }

    .app-name{
        font-size: 5rem;
    }

    .pitch-container {
        height: 100vh;
    }

    .pitch-grid-container {
        display: flex;
        align-items: center;
    }

    .pitch-grid{      
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-template-rows: 1fr;
        gap: 20px;
    }
    
}

img {
    height: 2rem;

}

.snap-container {
    overflow-y: scroll;
    height: 100vh;
}

.welcome-container {
    background-size: cover;
    background-position: center;
    height: 100vh;
    overflow: hidden;

    scroll-snap-align: start;
    scroll-snap-type: y mandatory;
}

.direct-welcome {
    display: flex;
    flex-direction: column;
}

.app-name {
    color: #FFFFFF;
    margin-bottom: 0;
}

.app-name-sh {
    color: #FFFFFF;
}

.pitch-grid-container {
    height: 100%;
}

.pitch-container{
    scroll-snap-align: start;
    scroll-snap-type: y mandatory;
    background-color: #000000;
}

.pitch-grid {
    display: grid;
}

.pitch-box {
    background-color: #FFFFFF;
    border-radius: var(--border-radius);
}

.buy-box {
    background-color: #232323;
    border-radius: var(--border-radius);
    grid-column: 1 / -1;
}

.feature-name {
    font-weight: bold;
    margin: 0;
    margin-left: 1rem;
}

.large-pitch-text {
    font-weight: bold;
    font-size:1.8rem;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.mega-large-pitch-text {
    font-weight: bold;
    font-size: 2rem;
    color: #000000;
    margin: 0;
}

.clearMargin {
    margin: 0;
}

.giga-large-pitch-text {
    font-weight: bold;
    font-size: 2.5rem;
    color: #FFFFFF;
    margin: 0;
}
</style>
