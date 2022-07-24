<template>
    <div id="register">
        <div class="container">
           <form>
                <h3>Register Here</h3>

                <label for="username">Username</label>
                <input type="text" placeholder="Username" id="username">

                <label for="email">Email</label>
                <input type="text" placeholder="Email " id="username">

                <label for="password">Password</label>
                <input type="password" placeholder="Password" id="password">
                <div class="buttons">
                    <button class="blob-btn">
                        Register
                        <span class="blob-btn__inner">
                        <span class="blob-btn__blobs">
                            <span class="blob-btn__blob"></span>
                            <span class="blob-btn__blob"></span>
                            <span class="blob-btn__blob"></span>
                            <span class="blob-btn__blob"></span>
                        </span>
                        </span>
                    </button>
                    <br>
                    <a href="#" @click="changeLoginStatus" class="register-to-login">
                      Sizda  xisob bormi? Login
                    </a>
                    <svg xmlns="http://www.w3.org/2000/svg" version="1.1">
                    <defs>
                        <filter id="goo">
                        <feGaussianBlur in="SourceGraphic" result="blur" stdDeviation="10"></feGaussianBlur>
                        <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 21 -7" result="goo"></feColorMatrix>
                        <feBlend in2="goo" in="SourceGraphic" result="mix"></feBlend>
                        </filter>
                    </defs>
                    </svg>
                    
                </div>
                 
            </form>
           
        </div>
    </div>
</template>

<script>

export default {
    name: 'Login',
    data() {
        return {

        }
    },
    methods: {
      changeLoginStatus() {
            this.$store.state.registerStatus = false
            this.$store.state.loginStatus = true
      },
    }

}
</script>

<style lang="scss" scoped>
$cyan: #0505A9;
$dark: #FFFFFF;
$borderW: 2px;
$btncolor: #b761f2;

          *,
*:before,
*:after{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
body{
    background-color: #080710;
}

.register-to-login {
  padding-top: 12px;
  display: block;
  font-size: 13px;
  color: #f0f0f0;
  text-decoration: none;
}
.register-to-login:hover {
  color: #fff;

  text-decoration: underline;
}
.background{
    width: 430px;
    height: 450px;
    position: absolute;
    z-index: 1000;
    transform: translate(-50%,-50%);
    left: 50%;
    top: 50%;
}
.background .shape{
    height: 200px;
    width: 200px;
    position: absolute;
    border-radius: 50%;
}
.shape:first-child{
    background: linear-gradient(
        #1845ad,
        #23a2f6
    );
    left: -80px;
    top: -80px;
}
.shape:last-child{
    background: linear-gradient(
        to right,
        #ff512f,
        #f09819
    );
    right: -30px;
    bottom: -80px;
}
form{
    height: 480px;
    width: 430px;
    background-color: #3f3f3f;
    position: absolute;
    z-index: 1000;
    transform: translate(-50%,-50%);
    top: 49%;
    left: 50%;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 20px 35px;
}
form *{
    font-family: 'Poppins',sans-serif;
    color: #ffffff;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
}
form h3{
    font-size: 32px;
    font-weight: 500;
    line-height: 42px;
    text-align: center;
}

label{
    display: block;
    margin-top: 18px;
    font-size: 13px;
    font-weight: 500;
}
input{
    display: block;
    height: 43px;
    width: 100%;
    background-color: rgba(255,255,255,0.07);
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 300;
}
::placeholder{
    color: #e5e5e5;
}
// button{
//     margin-top: 30px;
//     width: 100%;
//     background-color: #ffffff;
//     color: #080710;
//     padding: 15px 0;
//     font-size: 18px;
//     font-weight: 600;
//     border-radius: 5px;
//     cursor: pointer;
// }
.social{
  margin-top: 30px;
  display: flex;
}
.social div{
  background: red;
  width: 150px;
  border-radius: 3px;
  padding: 5px 10px 10px 5px;
  background-color: rgba(255,255,255,0.27);
  color: #eaf0fb;
  text-align: center;
}
.social div:hover{
  background-color: rgba(255,255,255,0.47);
}
.social .fb{
  margin-left: 25px;
}
.social i{
  margin-right: 4px;
}


.blob-btn {
    margin-top: 25px;
    width: 100%;
    background-color: #ffffff;
    color: #080710;
    padding: 15px 0;
    font-weight: 600;
    border-radius: 5px;
    $numOfBlobs: 4;
    z-index: 1;
    position: relative;
    text-align: center;
    text-transform: uppercase;
    color: rgb(26, 26, 26);
    font-size: 18px;
    background-color: transparent;
    outline: none;
    border: none;
    transition: color 0.5s;
    cursor: pointer;
  
  &:before {
    content: "";
    z-index: 1;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    border: $borderW solid #ccc;
    border-radius:30px;
  }
  
  &:after {
    content: "";
    z-index: -2;
    position: absolute;
    left: $borderW*1.5;
    top: $borderW*1.5;
    width: 100%;
    height: 100%;

    transition: all 0.3s 0.2s;
    border-radius:30px;
  }
  
  &:hover {
    color: $dark;
    border-radius:30px;
    &:before {
        border-color: $btncolor;
    }
    &:after {
      transition: all 0.3s;
      left: 0;
      top: 0;
      border-radius:30px;
    }
  }
  
  &__inner {
    z-index: -1;
    overflow: hidden;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    border-radius:30px;
    background:#ffffff;
  }
  
  // additional container created, because in FF blobs are breaking overflow:hidden of element with svg gooey filter
  &__blobs {
    position: relative;
    display: block;
    height: 100%;
    filter: url('#goo');
  }
  
  &__blob {
    position: absolute;
    top: $borderW;
    width: 100% / $numOfBlobs;
    height: 100%;
    background: $btncolor;
    border-radius: 100%;
    transform: translate3d(0,150%,0) scale(1.7);
    transition: transform 0.45s;
    
    @supports(filter: url('#goo')) {
      transform: translate3d(0,150%,0) scale(1.4);
    }
    
    @for $i from 1 through $numOfBlobs {
      &:nth-child(#{$i}) {
        left: ($i - 1) * (120% / $numOfBlobs);
        transition-delay: ($i - 1) * 0.08s;
      }
    }
    
    .blob-btn:hover & {
      transform: translateZ(0) scale(1.7);
      
      @supports(filter: url('#goo')) {
        transform: translateZ(0) scale(1.4);
      }
    }
  }
  
}
</style>