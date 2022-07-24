<template>
    
    <div id="home" >
        <div class="login-bg" v-if="getLoginSt" @click="this.$store.state.loginStatus = false, this.$store.state.registerStatus = false"></div>
        <div class="register-bg" v-if="getRegisterSt" @click="this.$store.state.registerStatus = false, this.$store.state.registerStatus = false"></div>

        
        <div class="container">
            <LoginView v-show="getLoginSt" />
            <RegisterView v-show="getRegisterSt"  />
            

            <div class="post-filter mb-3 mt-3">
                <div class="left-filter-items">

                    <Button label="Filter" @click="postFilters" :class="{ 'btn-is-active' : obj_filter.activeFilter}" class="p-button-secondary btn-filter" icon="pi pi-filter" iconPos="left"  />  
                
                    <PrimeCard class="card-filter" :class="{'is-filter-active': obj_filter.activeFilter}">
                        <template #title >
                            <div class="filter-header">
                                Filter Posts
                                <button @click="applyFilter" v-if="obj_filter.activeApply" class=" button-filter-header">Apply</button>
                                <button @click="applyFilter" v-else class="button-filter-header button-filter-disabled" disabled>Apply</button>
                            </div>
                        </template>
                        <template #content class="primecard-content">
                            <div class="programming-langs">
                                <h6 class="d-flex sub-filter-title">
                                    <span class="material-icons code-icon">
                                        code
                                    </span>
                                    Programming languages
                                </h6>
                                <button class="filterbtn" v-for="(language, index) in obj_filter.languages" :data-id="language.id" :data-slug="language.slug" :ref="'btn' + index" :key="language.id" @click="langToFilter(index)"> {{ language.name }}</button>
                            </div>
                            <div class="themes">
                                <h6 class="sub-filter-title">
                                    <span class="material-icons">
                                        book
                                    </span>
                                    Themes
                                
                                </h6>
                                <button class="filterbtn filterThemeBtn" v-for="(theme, index) in obj_filter.themes" :data-id="theme.id" :data-slug="theme.slug" :ref="'theme' + index" :key="theme.id" @click="themeToFilter(index)"> {{ theme.name }}</button>
                            </div>
                        </template>
                    </PrimeCard>


                <div class="ordering-filter ">
                        <button @click="changeActivity(1)"
                        class="new-posts-btn " 
                        :class="{ 'btn-is-active' : activeBtn == 1 }"
                        >
                        <span>
                            <i class="pi-clock pi"></i>
                        </span>
                        <span class="pb-1">
                            Yangilari
                        </span>
                        </button>
                        <button @click="changeActivity(2)" 
                        class="popular-posts-btn" :class="{ 'btn-is-active' : activeBtn == 2 }">
                        <span>
                            <i class="pi-bolt pi"></i>
                        </span>
                        Mashhurlari
                        
                        </button>
                </div>
                </div>
            </div>
            <Spinner v-show="showSpinner" />
                <div class="grid" v-if="obj_posts.showPost"> 
                <div class="col-6 col-sm-12" v-for="post in obj_posts.filteredPosts" :key="post.id">
                    
                    <Card 
                    :title="post.title" 
                    :content="post.content" 
                    :date="post.created_at" 
                    :author="post.author"
                    :get_thumbnail="post.get_thumbnail"
                    :slug="post.slug"
                    :id="post.id"
                    :likes="post.likes"
                    :getPosts="getPosts"
                    />
                    
                </div>
            </div>
            <div v-else>
                <h2 class="text-white text-center">Sorry, No Posts.. </h2>
            </div>
        </div>
    </div>
</template>

           
<script>
import Button from 'primevue/button';
import axios from 'axios'
import Card from '../components/Card' 
import PrimeCard from 'primevue/card';
import Spinner from '../components/Spinner';
import LoginView from '../components/LoginView'
import RegisterView from '../components/RegisterView'
import { mapGetters } from 'vuex'


export default {
    name: 'Home',
    components: {
        Card,
        Button,
        PrimeCard,
        Spinner,
        RegisterView,
        LoginView,
    },
    data() {
        return {
            activeBtn: 1,
            showSpinner: true,
            obj_posts: {
                posts: [],
                filteredPosts: [],
                showPost: true,
            },
            obj_filter: {
                activeFilter: false,
                languages: [],
                filterLang: [],
                filterTheme: [],
                themes: [],
                activeApply: false,
            },
            
        }
    },
    created() {
        this.getPosts()
        this.getLangs()
        this.getThemes()

        
    },
    mounted() {
        this.$store.dispatch('get_user_info')

    },
    methods: {
        async getPosts() {
            try{
                const res = await axios.get('http://localhost:8000/api/v1/posts/');
                this.obj_posts.posts = res.data;
                this.obj_posts.filteredPosts = res.data;

            } catch(error) {
                console.log(error);
            }
        },
        
        async getLangs() {
            try {
                const res = await axios.get('http://localhost:8000/api/v1/languages/');
                this.obj_filter.languages = res.data;
            } catch (error) {
                console.log(error)
            }
        },
        async getThemes() {
            try {
                const res = await axios.get('http://localhost:8000/api/v1/themes/');
                this.obj_filter.themes = res.data;
            } catch (error) {
                console.log(error)
            }
        },
        async get_order_by(ordering) {
            try{
                const res = await axios.get(`http://localhost:8000/api/v1/posts/?order_by=${ordering}`)
                this.obj_posts.posts = res.data;
                this.obj_posts.filteredPosts = res.data;

            } catch(error) {
                console.log(error)
            }
        },

        
        changeActivity(id) {
           if (id == 2) {
                this.activeBtn = 2
                this.get_order_by('popular')
           } else {
                this.activeBtn = 1
                this.get_order_by('-created_at')
           }
        },  

        postFilters() {
            this.obj_filter.activeFilter = !this.obj_filter.activeFilter
        },
        langToFilter(id) {
            let item = this.$refs['btn' + id][0]

            if ('filterbtn filterbtn-is-active' == item.classList.value) {
                item.classList.value = 'filterbtn'
                this.obj_filter.filterLang = this.obj_filter.filterLang.filter(e => e !== item.dataset.slug)

            } else {
                item.classList.value += ' filterbtn-is-active'
                this.obj_filter.activeApply = true
                this.obj_filter.filterLang.push(item.dataset.slug)
            }
            this.activeLang = !this.activeLang
        },
        
        haveSomePosts() {
            if (this.obj_posts.filteredPosts.length < 1) {
                this.obj_posts.showPost = false
            } else {
                this.obj_posts.showPost = true
            }
        },
        themeToFilter(id) {
            let item = this.$refs['theme' + id][0]

            if ('filterbtn filterThemeBtn filterbtn-is-active' == item.classList.value) {
                item.classList.value = 'filterbtn filterThemeBtn'
                this.obj_filter.filterTheme = this.obj_filter.filterTheme.filter(e => e !== item.dataset.slug)
            } else {
                item.classList.value += ' filterbtn-is-active'
                this.obj_filter.activeApply = true
                this.obj_filter.filterTheme.push(item.dataset.slug)
            }
            this.activeLang = !this.activeLang
        },
        applyFilter() {
            if (this.obj_filter.filterLang.length >= 1) {
                if (this.obj_filter.filterTheme.length >= 1) {
                    axios.get(`http://localhost:8000/api/v1/posts?theme=${this.obj_filter.filterTheme.toString()}&language=${this.obj_filter.filterLang.toString()}`)
                    .then(response => {
                        this.obj_posts.filteredPosts = response.data;
                        this.haveSomePosts()
                        
                        setTimeout(() => {
                            this.obj_filter.activeFilter = false
                        }, 50)
                    })
                    .catch(error => {
                        console.log(error);
                    })
                } else {
                    axios.get(`http://localhost:8000/api/v1/posts?language=${this.obj_filter.filterLang.toString()}`)
                    .then(response => {
                        this.obj_posts.filteredPosts = response.data
                        this.haveSomePosts()
                        setTimeout(() => {
                            this.obj_filter.activeFilter = false
                        }, 50)
                    })
                    .catch(error => {
                        console.log(error);
                    })
                }
            } else if (this.obj_filter.filterTheme.length >= 1) {
                    axios.get(`http://localhost:8000/api/v1/posts?theme=${this.obj_filter.filterTheme.toString()}`)
                    .then(response => {
                        this.obj_posts.filteredPosts = response.data
                        this.haveSomePosts()
                        setTimeout(() => {
                            this.obj_filter.activeFilter = false
                        }, 50)
                    })
                    .catch(error => {
                        console.log(error);
                    })
            } else {
                window.location.reload()
            }
        } 

    },
    computed: {
        ...mapGetters({
            getLoginSt: 'getLoginStatus',
            getRegisterSt: 'getRegisterStatus'
        })
    },  
    watch: {
        'obj_posts.filteredPosts': function (val)  {
            if (val.length >= 1) {
                this.showSpinner = false
            }
        }
    }
    
}
</script>

<style>
    /* FIlter */
    .post-filter {
        display: flex;
        color:#fff;
    }
    @media only screen and (min-width:100px) and (max-width:414px) {
       .col-sm-12 {
           width: 100% !important;
       }
    }
    .btn-filter {
        color: rgb(202, 202, 202) !important;
        background-color: #494949 !important;
        border: 1px solid #333 !important;
        padding: 8px 19px !important;

    }
    .btn-filter:active {
        background-color: #222222 !important;
    }

    .left-filter-items {
        height: 50px;
        display: flex;
    }

    .ordering-filter {
        width: 250px;
        display: flex;
        background: #333;
        margin-left: 30px;
        border-radius: 10px !important;
    }
    .ordering-filter button {
        transition: all .1s linear;
        width: 50%;
        background: transparent;
        border: none !important;
        color: #f2f2ff;
    }
    .new-posts-btn {
        border-top-right-radius: 0 !important;
        border-bottom-right-radius: 0 !important;
    }
    .popular-posts-btn {
        border-top-left-radius: 0 !important;
        border-bottom-left-radius: 0 !important;

    }
    .btn-is-active {
        border-radius: 10px;
        background: rgb(31, 31, 31) !important;
    }


    .pi-clock {
        transform: translateY(1px);
    }
    .card-filter {
        visibility: hidden;
        opacity: 0;
        transition: visibility 0s, opacity .1s linear;
        position: absolute;
        z-index: 100;
        width: 350px;
        top: 150px;
        
    }
    .card-filter .p-card-content {
        height: 400px;
        overflow-y: scroll;
    }
    .card-filter .p-card-content::-webkit-scrollbar {
        width: 4px;
    }
    .card-filter .p-card-content::-webkit-scrollbar-track {
        border-radius: 10px;
    }
        
        /* Handle */
    .card-filter .p-card-content::-webkit-scrollbar-thumb {
        background: rgb(63, 63, 63); 
        border-radius: 10px;
    }

    /* Handle on hover */
    ::-webkit-scrollbar-thumb:hover {
        background: #b30000; 
    }

   .p-card-content {
       padding: 0 !important;
   }

   /* filter */

   .filter-header {
       display:flex;
       justify-content: space-between;
   }
   .filterbtn {
       padding: .3rem .7rem;
       border: 1px solid #333;
       background: #0d1212f1;
       border-radius: 5px;
       color:#fff;
       outline: none;
       margin-right: 5px;
       margin-bottom: 10px;
   }
   .filterThemeBtn {
       padding: .2rem .4rem;
   }
   .filterbtn:hover {
       color: #2aa5a0;
   }
   .filterbtn-is-active {
       background: #212828;
       color: #2aa5a0;
   }
   /* icons */

    .code-icon {
        padding: 0;
        padding-right: 3px;
        padding-bottom: 3px;
    }
    .sub-filter-title .material-icons {
        padding: 0;
        padding-right: 3px;
        padding-bottom: 3px;
    }
    .sub-filter-title {
        display: flex;
        align-items: center;

    }
    .button-filter-header {
        padding: .1rem .5rem;
        font-size: 17px !important;
        border: 1px solid #333; 
        background: #333;
        color:rgb(224, 224, 224);
        border-radius: 5px;
        transition: all .1s linear;
    }
    .button-filter-disabled {
        color:rgb(160, 159, 159);
    }
    
    .button-filter-header:focus {
        color: #f2f2ff;
        border-color: rgb(114, 114, 114);
        box-shadow: 0 0 0 0.20rem rgb(80, 80, 80);
    }

    .is-filter-active {
        visibility: visible;
        opacity: 1;
    }

    .bg-filter {
        width: 100%;
        height: 100vh;
        position: absolute;
        background: red;
    }

    /* LoginView */
    .overflow-yhidden {
        overflow-y: hidden;
    }
    .login-bg {
        position: absolute;
        top: 5px;
        z-index: 100;
        background: rgba(0, 0, 0, 0.39);
        width: 100%;
        height: 100%;
    }
    .register-bg {
        position: absolute;
        top: 5px;
        z-index: 100;
        background: rgba(0, 0, 0, 0.39);
        width: 100%;
        height: 100%;
    }
</style>
