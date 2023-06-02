<script setup>
    import Card from '../components/Card_Reservas.vue'
    import {UserStatusStore} from '@/stores/user_status'
    const user_store = UserStatusStore();
    if (!(user_store.is_logged)) {
      window.location.replace(window.location['origin']+'/login');
    }
    var styles_list = [
      "background-image: url('https://upload.wikimedia.org/wikipedia/commons/d/de/Dawn_Charles_V_Palace_Alhambra_Granada_Andalusia_Spain.jpg')",
      "background-image: url('https://ep00.epimg.net/elpais/imagenes/2017/04/18/album/1492501737_090856_1492503664_album_normal.jpg')",
    ];
</script>

<template>
      <div class="bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-blue-400 via-blue-100 to-gray-100 min-h-screen mx-auto">
        <section class='flex justify-center pt-52 mx-auto'>
          <Card v-for="item in styles_list" :key="item.id" :bg_img_src="item"/>
        </section>
      </div>
</template>


<style>

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

  #text {
  font-family: 'Lobster';
  }
</style>
