<template>
    <div id="home">
        <div class="post-filter mb-3">
            <div class="left-filter-items">
               <Button label="Filter" class="p-button-secondary btn-filter" icon="pi pi-filter" iconPos="left"  />
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
                    Mashhurlari</button>
               </div>
            </div>
        </div>

        <div class="grid">
            <div class="col-6 col-sm-12" v-for="post in filteredPosts" :key="post.id">
                
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
    </div>
</template>

           
<script>
import Button from 'primevue/button';
import axios from 'axios'
import Card from '../components/Card' 

export default {
    name: 'Home',
    components: {
        Card,
        Button,
    },
    data() {
        return {
            posts: [],
            activeBtn: 1,
            filteredPosts: [],
        }
    },
    created() {
        this.getPosts()
    },
    methods: {
        async getPosts() {
            try{
                const res = await axios.get('http://localhost:8000/api/v1/posts/');
                this.posts = res.data;
                this.filteredPosts = res.data;
            } catch(error) {
                console.error(error);
            }
        },

        
        changeActivity(id) {
           if (id == 2) {
                this.activeBtn = 2
           } else {
                this.activeBtn = 1
           }
        },


    },
   
    
}
</script>

<style>
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
    .btn-filter:hover {
        background-color: #333 !important;
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
   
</style>
