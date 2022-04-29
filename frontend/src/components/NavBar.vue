<template>
    <nav class="nav mb-3 bg-gray-800">
        
        <div class="bg-navbar" v-if="isSearchVisible" @click="isSearchVisible = false,  searchValue = '' ">

        </div>
       <div class="container">
           <div class="sub-nav">

                <div class="logo">
                    <router-link :to="{ name: 'index' }" @click="refreshWindow">AE-Blog</router-link>
                </div>

                <ul class="nav-items d-flex">

                    <li class="search-form">
                        <div class="search-input-block">
                            <input type="text" placeholder="Qidirish.." v-model="searchValue" @input="searchFunc">
                            <a href="">
                                <i class="pi pi-search"></i>
                            </a>
                        </div>
                        <div class="card search-card" v-show="isSearchVisible">
                            <router-link :to="{name: 'postView', params: {slug: post.slug} }" @click="isSearchVisible = false, searchValue = '' "  v-for="post in myposts" :key="post.id">
                                <article class="card-body">
                                        <div class="search-res-image">
                                        <img :src="post.image" width="80" alt="">
                                    </div>
                                    <div class="search-res-text">
                                        <h6>{{ post.title }}</h6>
                                        <p class="post-content-search">
                                            {{ post.content }} 
                                        </p>
                                    </div>
                                    
                                </article>
                            </router-link>
                            <article class="card-body other-results" v-show="otherResults">
                                <a href="" class="d-flex">
                                    <h6>
                                    <i class="pi-search pi"></i>
                                </h6>
                                <div class="search-res-text" >
                                    <h6 >Other Results</h6>
                                </div>
                                </a>
                            </article>
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
    props: ['posts'],
    components: [
        InputText,
    ],
    data() {
        return {
            isDropdownVisible: false,
            isSearchVisible: false,
            value: '',
            searchValue: '',
            myposts: [],
            otherResults: false,
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
               const res = await axios.get('http://localhost:8000/api/v1/languages/');
               this.navLanguages = res.data;
           } catch(error) {
               console.error(error);
           }

       },
       refreshWindow() {
           if (window.location == 'http://localhost:8080/') {
                window.location.reload();
           }
           
        },
        searchFunc() {
            if (this.searchValue.length >= 1) {
                this.isSearchVisible = true
            } else {
                this.isSearchVisible = false
            }
            this.myposts = this.posts.filter(post => {
                return post.title.toLowerCase().includes(this.searchValue) || post.content.toLowerCase().includes(this.searchValue)
            })
            if (this.myposts.length > 3) {
                this.otherResults = true
            } else {
                this.otherResults = false
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
.bg-navbar {
    position: absolute;
    z-index: 50;
    background: #000;
    width: 100%;
    height: 100vh;
    left: 0;
    opacity: .1;

}
.sub-nav {
    display: flex;
    justify-content: space-between;
    padding-top: 15px;
}
.nav-items {
    position: relative;
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


// search card

.search-card {
    position: absolute !important;
    background: #333 !important;
    color:#fff;
    width: 300px;
    left:-12px;
    top: 50px;
    z-index: 100;
    article:first-of-type {
        padding-top: 8px;
    }
    article {
        height: 70px;
        padding: 10px;
        padding-bottom: 0;

        border-bottom: 1px solid #bdbdbd;
        padding-top: 5px;
        padding-bottom: 0;
        display:flex;
        margin-bottom: 0;

        img {
            padding-top: 4px;
        }

        
    }
    .other-results {
        height: 40px;
        h6 {
            padding-top: 5px;
        }
        i {
            font-size: 16px;
            padding-left: 12px;
        }
    }
    .search-res-text {
        padding: 5px 10px;
        padding-top: 0;
        p {
            font-size: 13px;
            line-height: 1.3;
            padding: 0;
        }
        h6 {
            padding-bottom: 0;
            font-size: 15px;
            display: -webkit-box;
            -webkit-line-clamp: 1;
            -webkit-box-orient: vertical;
            overflow: hidden;
            margin-bottom: 0;
        }
    }
}

.post-content-search {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;

}
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/

</style>

