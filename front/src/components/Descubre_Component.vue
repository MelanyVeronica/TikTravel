<script setup>
  import Card_Descubre from '../components/Card_Descubre.vue'
  import {UserStatusStore} from '@/stores/user_status'
  import {ApiHostStore} from '@/stores/api_hosts'
  import axios from 'axios'
  import { ref } from 'vue';
  
  const api_store = ApiHostStore()
  const user_store = UserStatusStore()
  const upload_pic_action = api_store.get_api_host + '/api-auth/upload-pics'
  const discover_data = ref([])

  // const base_host = api_store.get_api_host
  if (api_store.is_dev) {
    var base_host = api_store.get_api_host;
  } else {
    var base_host = window.location.origin+'/';
  }
  const axios_instance = axios.create({
      baseURL: base_host,
  });
  
  const csrf_token_form = ref('')
    function get_token() {
      axios_instance.get('api-auth/x-csrf-token')
      .then(function (response) {
          console.log(response);
          console.log(response.headers['x-csrftoken']);
          csrf_token_form.value = response.headers['x-csrftoken'];
      })
      .catch(function (error) {
          console.log(error);

      })
      .finally(function () {
          // console.log();
      });
  }
  get_token();

  function get_discover() {
    axios_instance.post('api/discover-pics')
    .then(function (response) {
    discover_data.value = response.data['discover_data'];
    })
    .catch(function (error) {
        console.log(error);
    })
    .finally(function () {
    // console.log();
    });
  }
  get_discover();
</script>

<template>
  <div class="min-h-screen">
    <div class="flex justify-center p-3 bg-gray-200">
      <ul class="flex items-center flex-shrink-0 space-x-6">
        <!-- Profile menu -->
        <li class="relative ">
          <button class="align-middle rounded-full border-2 border-gray-300 shadow-lg  focus:shadow-outline-purple focus:outline-none">
            <img class="object-cover w-10 h-10 rounded-full hover-image-1 flex-shrink-0" src="https://picsum.photos/200/200?i=203" alt="" aria-hidden="true">
          </button>
        </li>

              <li class="relative">
          <button class="align-middle rounded-full border-2 border-gray-300 shadow-lg  focus:shadow-outline-purple focus:outline-none">
            <img class="object-cover w-10 h-10 rounded-full hover-image-1 flex-shrink-0" src="https://picsum.photos/200/200?i=205" alt="" aria-hidden="true">
          </button>
        </li>

              <li class="relative">
          <button class="align-middle rounded-full border-2 border-gray-300 shadow-lg  focus:shadow-outline-purple focus:outline-none">
            <img class="object-cover w-10 h-10 rounded-full hover-image-1 flex-shrink-0" src="https://picsum.photos/200/200?i=207" alt="" aria-hidden="true">
          </button>
        </li>

              <li class="relative">
          <button class="align-middle rounded-full border-2 border-gray-300 shadow-lg  focus:shadow-outline-purple focus:outline-none">
            <img class="object-cover w-10 h-10 rounded-full hover-image-1 flex-shrink-0" src="https://picsum.photos/200/200?i=209" alt="" aria-hidden="true">
          </button>
        </li>

            <li class="relative">
          <button class="align-middle rounded-full border-2 border-gray-300 shadow-lg  focus:shadow-outline-purple focus:outline-none">
            <img class="object-cover w-10 h-10 rounded-full hover-image-1 flex-shrink-0" src="https://picsum.photos/200/200?i=2011" alt="" aria-hidden="true">
          </button>
        </li>

      </ul>

    </div>

    <div class="overflow-y-scroll max-h-[40rem] pt-4 px-1 mx-auto">

      <Card_Descubre class="px-1 mx-auto" v-for="i in discover_data" :key="i.id" :profile_img_src="i['profile_pic']" :username="i['username']" :user_imgs_srcs="i['user_pics']"/>
     
    </div>

    <div class="w-full" v-if="user_store.is_logged">
              <div class="mx-auto pt-3 pb-3">
                  <div class="sm:p-8 bg-gray-200 sm:rounded-lg shadow-xl">
                      <h1 class="uppercase font-extrabold text-2xl text-center border-b-2 border-black">Publicar Imagenes</h1>
                      <form class="mt-8" x-data="{password: '',password_confirm: ''}">
                          <div class="mx-auto max-w-lg ">
                              <form :action="upload_pic_action" method="post">
                                  <div class="py-1">
                                      <span class="px-1 text-sm text-gray-600">Imagen</span>
                                      <input type="hidden" name="csrfmiddlewaretoken" :value="csrf_token_form">
                                      <input required value="" placeholder="" type="file" name="page_pic_file" accept="image/png, image/jpeg"
                                          class="text-md block px-3 py-2 rounded-lg w-full bg-white border-2 border-gray-300 placeholder-gray-600 shadow-md focus:placeholder-gray-500 focus:bg-white focus:border-gray-600 focus:outline-none">
                                  </div>

                                  <button type="submit" class="flex justify-center m-auto pt-3">  
                                      <a class="relative items-center justify-start inline-block px-4 py-1 overflow-hidden font-bold rounded-full group">
                                          <span class="w-32 h-32 rotate-45 translate-x-12 -translate-y-2 absolute left-0 top-0 bg-white opacity-[3%]"></span>
                                          <span class="absolute top-0 left-0 w-48 h-48 -mt-1 transition-all duration-500 ease-in-out rotate-45 -translate-x-56 -translate-y-24 bg-blue-500 opacity-100 group-hover:-translate-x-8"></span>
                                          <span class="relative w-full text-left text-blue-500 transition-colors duration-200 ease-in-out group-hover:text-white">Publicar</span>
                                          <span class="absolute inset-0 border-2 border-blue-500 rounded-full"></span>
                                      </a>
                                  </button>
                              </form>

                          </div>
      
                      </form>
                  </div>
              </div>
      </div>
  </div>
</template>

<style>

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
</style>
