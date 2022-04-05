<template>
    <div id="post-view">
        {{ post.title }}
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