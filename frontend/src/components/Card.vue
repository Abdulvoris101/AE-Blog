<template>
    <div class="blog-card bg-gray-700"> 
        <div class="card-img">
             <router-link :to="{ name: 'postView', params: { slug: slug } }" class="router-link-img">   
                <figure :style="{ backgroundImage: 'url(' + get_thumbnail + ')' }" class="card-image-bg">

                </figure>
            </router-link>
            
        </div>
        <div class="card-main">
            <h4 class="card-title">
                <router-link :to="{ name: 'postView', params: { slug: slug } }">
                    {{ title }}
                </router-link>
            </h4>
            <p class="card-content line-height-2 text-600"> {{ content }} </p>
            
            <div class="blog-card-footer">
                
                        
                <div class="card-reactions">
                    <a  href="#" @click="SubmitLike(id)" :id="id" class="like-btn">
                        
                        <span class="material-icons" :ref="'like' + id" >
                            thumb_up_off_alt
                        </span>

                        <span class="mt-1" >
                            <span :ref="'likecnt' + id">
                                {{ likesFiltered.length }}
                            </span>
                        </span>
                    </a>   
                    <a href="" class="like-btn comment-btn">
                        <span class="material-icons">
                            forum 
                        </span>
                        <span>
                            6
                        </span>
                    </a>
                </div>
                <p class="mt-1">
                    <i class="pi-user-edit pi"></i> {{ author }}
                </p>
            </div>
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Card',
    props: ['title', 'get_thumbnail', 'author', 'date', 'content', 'slug', 'id', 'likes', 'getPosts'],

    data() {
        return {
            msg: 'hello',
            likesFiltered: [],
            myuser: []
            
        }
    },
    created() {
        axios.get('http://127.0.0.1:8000/user/info/', {
            headers: {
                Authorization: 'Token f9c1cad1e2b49d9b4ec41ca1107bfd67d0c7b090'
            }
        })
        .then(response => this.likedUser(response))
        .catch(function (error) {
            console.log(error);
        })

    },
    methods: {
        likedUser(myuser) {
            this.myuser = myuser.data
            this.likesFiltered = this.likes.filter(like => {
                if (like.user == myuser.data.username && like.status == 'Like') {
                    let likedBtn = this.$refs['like' + like.post];
                    likedBtn.innerHTML = 'thumb_up_alt'
                }
                return like.status == 'Like' 
            })
        },
        SubmitLike(id) {
            let likedBtn = this.$refs['like' + id];
            let likedCnt = this.$refs['likecnt' + id];
            let likedCntInt = parseInt(likedCnt.innerHTML);
            

            if (likedBtn.innerHTML  == 'thumb_up_alt') {
                likedBtn.innerHTML = 'thumb_up_off_alt'
                likedCnt.innerHTML = likedCntInt - 1
            } else {
                likedBtn.innerHTML = 'thumb_up_alt'
                likedCnt.innerHTML = likedCntInt + 1
            }

            let url = `http://127.0.0.1:8000/api/v1/like/${id}/`

            axios.get(url, {
                headers: {
                  Authorization: 'Token f9c1cad1e2b49d9b4ec41ca1107bfd67d0c7b090'  
                }
            })
            .then(response => console.log(response))
            .catch(error => console.log(error))

            
            
        }
    },

}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
.blog-card {
    display: flex;
    position: relative;
    border-radius: 7px;
    color: #fff;
    height: 180px;
    .router-link-img {
        width: 100%;
        display: flex;
    }
    figure {
        width: 100%;
        height: 100%;
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    .card-main {
        padding: 25px;
        padding-left: 34px;
        width: 60%;
        
    }
    .card-img {
        width: 45%;
        display: flex;

    }
    .card-content {
        font-size: 14px;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    .card-author {
        i {
            font-size:10px;
        }
    }
    .card-date {
        i {
            font-size: 10px;
        }
    }
    .blog-card-footer {
        position:absolute;
        bottom:15px;
        align-items:center;
        display: flex;
        justify-content: space-between;
        width:40%;
    }
    .blog-card-footer p{
        margin-top: 0;
        margin-bottom: 4px;
    }
    .card-title {
        font-size: 19px;
        a {
            color: #ffff;
            text-decoration: none;
            transition: all .1s linear;
        }
        a:hover {
            color:#fff;
        }
    }
    
    
    
}
    
.card-reactions {
    display:flex;
    list-style: none;
    padding: 0;
}
.like-btn {
    margin-right: 5px;
    display: flex;
    width:50px;
    align-items: center;
    justify-content: space-around;
    background-color: rgb(53, 53, 53);
    color: #fff;
    text-decoration: none;
    padding: 5px !important;
    border-radius: 6px;

}
.material-icons {
    margin: 0;
    padding: 0;
    font-size: 24px;
}
.comment-btn .material-icons{
    font-size: 19px;
}

.flex-center {
    display:flex;
    align-items:center;
}

</style>