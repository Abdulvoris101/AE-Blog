<template>
    <nav class="nav">
       <div class="container">
           <div class="sub-nav">
                <div class="logo">
                    <a href="#">AE-Blog</a>
                </div>
                <ul class="nav-items d-flex ">
                    <li v-for="(item, index) in navItems" :key="index"><a href="#" >{{ item }}</a></li>
                    <li class="dropdown">
                        <div class="dropdown-link">
                            <a class="" href="#" @click="isDropdownVisible = !isDropdownVisible">
                                Tillar 
                                <i class="pi pi-arrow-circle-down"></i>
                            </a>
                        </div>
                       <ul class="dropdown-menu" v-show="isDropdownVisible">
                            <li v-for="item in navLanguages" :key="item.id"><a class="" href="#">{{ item.name }}</a></li>
                        </ul>
                    </li>
                    
                </ul>
           </div>
       </div>
    </nav>
</template>

<script>
import axios from 'axios'
export default {
    name: 'NavBar',
    data() {
        return {
            isDropdownVisible: false,
            navItems: ['Bosh sahifa', 'Mashhur', 'Yangi'],
            navLanguages: []
        }
    },
    mounted() {
        this.getCategories()
    },
    methods: {
       async getCategories() {
           try{
               const res = await axios.get('http://localhost:8000/api/v1/categories/');
               this.navLanguages = res.data;
           } catch(error) {
               console.error(error);
           }

       }

    }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap');

.nav {
    width: 100%;
    background: #242424;
    font-family: 'Poppins', sans-serif;
}
.sub-nav {
    display: flex;
    justify-content: space-between;
    padding-top: 15px;
}
.nav-items {
    li {
        list-style: none;
        a {
            color: #fff;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
        }
        a:first-of-type {
            padding-left: 0;
        }
        i {
            font-size: 12px;
        }
        
        padding-left: 30px;
        
    }
    .dropdown  {
        .dropdown-link {
            border: 1px solid #333;
            padding: 7px 24px;
            background-color: transparent;
        }
        .dropdown-menu {
            display: block;
            color: #fff;
            background-color: #242424;
            min-width: 6.6rem;
            border-radius: 1px !important;
        }
    }
    li:not(:last-of-type) {
        padding-top: 7px;
    }
}
.logo {
    a {
        display: block;
        color: #fff;
        text-decoration: none;
        font-weight: 600;
        font-size: 18px;
        padding-top: 8px;
    }
    a:hover {
        color: #fff;
    }
}

</style>

