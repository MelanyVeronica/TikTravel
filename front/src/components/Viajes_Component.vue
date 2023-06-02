<script setup>
import Card from '../components/Card.vue'
var styles_list = [
  "background-image: url('https://upload.wikimedia.org/wikipedia/commons/d/de/Dawn_Charles_V_Palace_Alhambra_Granada_Andalusia_Spain.jpg')",
  "background-image: url('https://ep00.epimg.net/elpais/imagenes/2017/04/18/album/1492501737_090856_1492503664_album_normal.jpg')",
  "background-image: url('https://ichef.bbci.co.uk/news/640/cpsprodpb/52FA/production/_122524212_foto_01.jpg')",
  "background-image: url('https://res.cloudinary.com/hello-tickets/image/upload/c_limit,f_auto,q_auto,w_1300/v1636970940/rsibwpe9q22v2s79cwpf.jpg')",
  "background-image: url('https://www.economiadigital.es/tendenciashoy/wp-content/uploads/2020/08/ciudad-artes-1282x780.jpg')",
];
</script>

<template>

<div id="fondo_v">

    <div class="flex items-center min-h-screen">

        <div class="text-center px-10 pl-28 hidden lg:block">
            <h1 id="animacion"> <p id="text" class="show lg:text-4xl xl:text-6xl text-white">Descubre el mundo con nosotros <br> ¡ Tu aventura comienza aquí !</p></h1>
        </div>

        <section class='px-2 overflow-y-scroll max-h-[40rem] mx-auto'>
          <Card v-for="item in styles_list" :key="item.id" :bg_img_src="item"/>
        </section>

    </div>
    
</div>
</template>


<style>
#fondo_v {
background-image: url('../assets/image.jpg');
background-attachment: fixed;
background-repeat: no-repeat;
background-size: cover;

}

.fade-in {
opacity: 0;
animation: fade-in-animation 2s ease-in forwards;
}

@keyframes fade-in-animation {
from {
opacity: 0;
}
to {
opacity: 1;
}
}

section {
scrollbar-width: none; 
-ms-overflow-style: none; 
}

section::-webkit-scrollbar {
display: none; 
}

::-webkit-scrollbar{
display: none;
}

*{
scrollbar-width: none; 
-ms-overflow-style: none; 
}

#animacion {
animation: anim-lineUp 2s;
}

@keyframes anim-lineUp {
0% {
  opacity: 0;
  transform: translateY(30%);
}
100% {
  opacity: 1;
  transform: translateY(0%);
}
}

#text {
font-family: 'Lobster';
}
</style>