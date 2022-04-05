<template>
    <nav class="nav mb-3 bg-gray-800">
       <div class="container">
           <div class="sub-nav">

                <div class="logo">
                    <router-link :to="{ name: 'index' }">AE-Blog</router-link>
                </div>

                <ul class="nav-items d-flex">

                    <li class="search-form">
                        <div class="search-input-block">
                            <input type="text" placeholder="Qidirish..">
                            <a href="">
                                <i class="pi pi-search"></i>
                            </a>
                        </div>
                    </li>

                    <li class="d-flex nav-right-items">
                        <div class="dropdown">

                            <div class="dropdown-link">
                                <a class="" href="#" @click="isDropdownVisible = !isDropdownVisible">
                                    Dasturlash Tillari 
                                    <i class="pi pi-arrow-circle-down"></i>
                                </a>
                            </div>
                            
                            <ul class="dropdown-menu" v-show="isDropdownVisible">
                                <li v-for="item in navLanguages" :key="item.id"><a class="" href="#">{{ item.name }}</a></li>
                            </ul>
                        </div>

                        <ul class="d-flex ul-icons">
                            <li v-for="(item, index) in navIconItems" :key="index">
                                <a href="" >
                                    <i :class="item.class" class=" icon-menu" ></i>
                                    {{ item.name }}
                                </a>
                            </li>
                        </ul>
                    </li>
                </ul>

           </div>
       </div>
    </nav>
</template>

<script>
import axios from 'axios'

import InputText from 'primevue/inputtext';

export default {
    name: 'NavBar',
    components: [
        InputText
    ],
    data() {
        return {
            isDropdownVisible: false,
            value: '',
            navDefaultItems: [
                {
                    label: 'Bosh sahifa',
                    name: 'index'
                }, 
                {
                    label: 'Mashhur',
                    name: ''
                }, 
                {
                    label: 'Yangi',
                    name: ''
                },
                
            ],
            navIconItems: [
                {
                    class: 'pi-pencil pi',
                    to: '/',
                    name: 'Post yozish'
                }, 
                {
                    class: 'pi pi-user',
                    name: 'Kirish',
                    to: '/'
                },
            ],
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

.icon-menu{
    padding-top: 4px;
    font-size: 15px !important;
}
.nav {
   background: rgb(32,32,37);
   box-shadow: 2px 2px 6px #333;
    background: linear-gradient(93deg, rgba(32,32,37,0.8379726890756303) 0%, rgba(22,22,22,1) 100%);
    width: 100%;
    border-bottom: 1px solid #333;
    font-family: 'Poppins', sans-serif;
}
.sub-nav {
    display: flex;
    justify-content: space-between;
    padding-top: 15px;
}
.nav-items {
    justify-content: space-between;
    width: 70%;
    padding-top: 4px;
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
            min-width: 12.5rem;
            border-radius: 1px !important;
        }
        .dropdown-menu a {
            padding: 3px 0;
        }
    }
}
.logo {
    margin-top: 4px;
    a {
        padding-top: 3px;
        display: block;
        color: #fff;
        text-decoration: none;
        font-weight: 600;
        font-size: 18px;
    }
    a:hover {
        color: #fff;
    }
}
.dropdown {
    margin-top: -6px;
}

.ul-icons {
    margin-left: 0;
    padding-left: 0;
}

// search 
.search-form {
    padding-left: 0 !important;
    margin-top: -4px;

}
.search-input-block {
    display: flex;

    align-items: center;
}
.search-input-block i {
    font-size: 17px !important;
    color:#fff;
    padding-left: 10px;

}

.search-input-block input {
    border-radius: 5px;
    font-size: 15px;
    background: #333;
    padding: 6px 10px;
    border:1px solid #333;
    outline: none;
    color:rgb(238, 238, 238);
}
.search-input-block input:focus {
    border-color: rgb(231, 231, 231);
}


</style>

