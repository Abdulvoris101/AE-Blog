<template>
    <div id="post-view" class="container">
        <div class="blog-view">
            <Spinner :postview="true" v-show="showSpinner" />
            <main class="blog-detail">
                <div class="blog-header">
                    <h1>{{ post.title }}</h1>
                    <div class="blog-edits">

                    </div>
                </div>
                <figure class="blog-detail-img">
                    <img :src="post.image"  alt="">
                </figure>
                <div class="blog-content">
                    <p>
                        {{ post.content }}
                    </p>
                </div>
            </main>
            <sidebar class="blog-sidebar">
                <div class="container">
                    
                    <div class="posts" v-if="posts.length > 0">
                        <h4>Latest Posts</h4>
                        <Spinner :postright="true" v-show="showRightSpinner" />

                        <article class="blog-content-card"  v-for="post in posts" :key="post.id">
                            <div class="img-content">
                                <router-link :to="{ name: 'postView', params: { slug: post.slug } }" >
                                    <img :src="post.get_thumbnail" width="100" alt="">
                                </router-link>
                            </div>
                            <router-link :to="{ name: 'postView', params: { slug: post.slug } }" class="link-more-posts">
                                <div class="text-content">
                                    {{ post.title }}
                                    <div class="content">
                                        {{ post.content }}
                                    </div>
                                </div>
                            </router-link>
                            
                        </article>
                    </div>
                    <div class="no-posts" v-else>
                        <h4>No Posts</h4>
                        <h5>Sorry no posts in the platform</h5>
                    </div>

                    
                </div>
            </sidebar>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Spinner from '@/components/Spinner.vue';

export default {
    name: 'PostView',
    components: {
        Spinner
    },
    data() {
        return {
            post: [],
            slug: this.$route.params.slug,
            posts: [],
            showSpinner: true,
            showRightSpinner: true
        }
    },
    created() {
        this.get_post(this.slug)
        this.get_last_posts()
    },
    methods: {
        async get_post(slug) {
            try{
                const post = await axios.get(`http://localhost:8000/api/v1/post/${slug}`);
                if (post) {
                    this.post = post.data;
                }
            } catch(error) {
               console.error(error);
            }
        },
        async get_last_posts() {
            try {
                const posts = await axios.get(`http://localhost:8000/api/v1/posts?last=7`);
                if (posts) {
                    this.showRightSpinner = false
                    this.posts = posts.data;
                    this.posts = this.posts.filter(post => {
                        return post.slug != this.post.slug
                    })
                }
            } catch(error) {
                console.log(error)
            }
        }
    },
    watch: {
        $route(to) {
            this.get_post(to.params.slug)

            this.get_last_posts()
        },
        post(val) {
            if (val.title) {
                this.showSpinner = false
            }
        },
  }
}
</script>

<style lang="scss" scoped>
#post-view {
    color:#fff;
}
.blog-view {
    display:flex;

    .blog-detail {
        width: 70%;
    }
    .blog-sidebar {
        width:30%;
    }
    
}
.blog-detail-img img{
    width:100%;
}
.blog-sidebar {
    margin-top: 10px;
    margin-left: 20px;
}
.blog-content-card {
    display:flex;
    align-items: center;
    border-bottom: 1px solid rgb(116, 116, 116);
    padding-bottom: 10px;
    padding-top: 10px;
    .text-content {
        padding: 0px 5px;
    }
    .content {
        display: -webkit-box;
        -webkit-line-clamp: 2;
        line-height: 1.2;
        -webkit-box-orient: vertical;
        overflow: hidden;

        font-size: 14.5px;
        color: #f2f2ff;
    }
    .link-more-posts {
        color:#fff;
        text-decoration: none;
    }
}   

</style>