<template>
    <div id="post-view">
        <div class="container">
            <main class="blog-detail">
                <h1>{{ post.title }}</h1>
                <figure class="blog-detail-img">
                    <img :src="post.image" width="900" height="600" alt="">
                </figure>
            </main>
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'PostView',
    data() {
        return {
            post: null,
            slug: this.$route.params.slug
        }
    },
    created() {
        this.get_post()
    },
    methods: {
        async get_post() {
            try{
                const post = await axios.get(`http://localhost:8000/api/v1/post/${this.slug}`);
                if (post) {
                    this.post = post.data;
                }

            } catch(error) {
               console.error(error);
            }
        }
    }
}
</script>

<style lang="scss" scoped>
#post-view {
    color:#fff;
}
</style>