<template>
    <div id="left-menu">
        <div class="left-menu-wrapper">
            <ul>
                <li class="mt-2">
                    <a href="" class="social-icons" >
                        <i class="pi-telegram pi"></i>
                    </a>
                </li>
                 <li>
                    <a href="" class="social-icons" >
                        <i class="pi-instagram pi"></i>
                    </a>
                </li>
                 <li>
                    <a href="" class="social-icons" >
                        <i class="pi-facebook pi"></i>
                    </a>
                </li>
                <li>
                    <a href="" class="social-icons">
                        <i class="pi pi-reddit">

                        </i>
                    </a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>


<style scoped lang="scss">
    #left-menu {
        width: 45px;
        height: 30%;
        position: fixed;
        top: 30%;
        background-color: rgb(61, 61, 61);
        border-top-right-radius: 10px;
        border-bottom-right-radius: 10px;
    }

    .left-menu-wrapper ul, li {
        margin: 0;
        padding: 5px 3px;
    }
    .social-icons i{
        font-size: 28px;
        color:#dddd;
        filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#f09433', endColorstr='#bc1888',GradientType=1 );
    }
    .social-icons:hover i {
        color:#fff;
        transform: scale(1.1);
    }
    
</style>