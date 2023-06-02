<script setup>
    import axios from 'axios'
    import {ApiHostStore} from '@/stores/api_hosts'
    import { ref } from 'vue';
    
    const api_store = ApiHostStore()
    
    const change_password_action = api_store.get_api_host + '/api-auth/change-password'
    const change_mail_action = api_store.get_api_host + '/api-auth/change-email'
    const change_username_action = api_store.get_api_host + '/api-auth/change-username'
    const upload_pic_action = api_store.get_api_host + '/api-auth/upload-profile-pic'
    
    const self_page = ref(false)
    const profile_pic_url = ref('')
    const user_page_pics_urls = ref([])
    const user_found = ref('')
    
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
    
    function get_profile_pic() {
        let data = {'current_user_page': window.location.pathname};
        axios_instance.post('api/profile-pic', data=data)
        .then(function (response) {
            console.log(response);
            profile_pic_url.value = response.data['profile_pic_src'];
            if (response.data['message'] == 'User does not exist') {
                user_found.value = false;
            } else {
                user_found.value = true;
            }
        })
        .catch(function (error) {
            console.log(error);
            user_found.value = false;
        })
        .finally(function () {
        // console.log();
        });
    }
    
    function get_userpage_pics() {
        let data = {'current_user_page': window.location.pathname};
        axios_instance.post('api/userpage-pics', data=data)
        .then(function (response) {
        user_page_pics_urls.value = response.data['userpage_pics_srcs'];
        if (response.data['message'] == 'User does not exist') {
            user_found.value = false;
        } else {
            user_found.value = true;
        }
        })
        .catch(function (error) {
            console.log(error);
            user_found.value = false;
        })
        .finally(function () {
            // console.log();
        });
    }
    
    function is_self_page() {
        axios_instance.get('api-auth/hi')
        .then(function (response) {
            console.log(response);
            if (('/user/'+response.data['username']+'/') == window.location.pathname) {
            self_page.value = true;
            } else {
            self_page.value = false;
            };
        })
        .catch(function (error) {
            console.log(error);

        })
        .finally(function () {
            console.log('self_page =', self_page.value);
        });
    }

    is_self_page();
    get_profile_pic();
    get_userpage_pics();
    // window.setInterval(is_self_page, 2*60*1000); 
</script>

<template>
    <div class="min-h-screen bg-blue-100">
    <div>
        <div v-if="user_found">
            <section v-if="self_page">
                <div class="max-w-2xl mx-auto pt-4">
                    <div class="sm:p-8 bg-blue-200 sm:rounded-lg shadow-xl">
                        <h1 class="uppercase font-extrabold text-2xl text-center border-b-2 border-black">Configurar Información del Perfil</h1>
                        <form class="mt-8" x-data="{password: '',password_confirm: ''}">
                            <div class="mx-auto max-w-lg ">

                                <div class="m-auto">
                                    <div class="flex justify-center pb-2"><span class="text-base font-bold text-gray-600">Foto de perfil</span></div>
                                    <img :src="profile_pic_url" class="m-auto object-cover w-20 h-20 rounded-full hover-image-1 flex-shrink-0">
                                </div>

                                <form :action="change_username_action" method="post">
                                    <div class="py-1">
                                        <span class="px-1 text-sm text-gray-600">Nombre</span>
                                        <input type="hidden" name="csrfmiddlewaretoken" :value="csrf_token_form">
                                        <input required placeholder="" type="text" name="usern"
                                            class="text-md block px-3 py-2 rounded-lg w-full bg-white border-2 border-gray-300 placeholder-gray-600 shadow-md focus:placeholder-gray-500 focus:bg-white focus:border-gray-600 focus:outline-none">
                                    </div>

                                    <button type="submit" class="flex justify-center m-auto pt-3">  
                                        <a class="relative items-center justify-start inline-block px-4 py-1 overflow-hidden font-bold rounded-full group">
                                            <span class="w-32 h-32 rotate-45 translate-x-12 -translate-y-2 absolute left-0 top-0 bg-white opacity-[3%]"></span>
                                            <span class="absolute top-0 left-0 w-48 h-48 -mt-1 transition-all duration-500 ease-in-out rotate-45 -translate-x-56 -translate-y-24 bg-blue-500 opacity-100 group-hover:-translate-x-8"></span>
                                            <span class="relative w-full text-left text-blue-500 transition-colors duration-200 ease-in-out group-hover:text-white">Guardar</span>
                                            <span class="absolute inset-0 border-2 border-blue-500 rounded-full"></span>
                                        </a>
                                    </button>
                                </form>
                                <form :action="change_mail_action" method="post">
                                    <div class="py-1">
                                        <span class="px-1 text-sm text-gray-600">Correo electronico</span>
                                        <input type="hidden" name="csrfmiddlewaretoken" :value="csrf_token_form">
                                        <input required placeholder="" type="email" name="email"
                                            class="text-md block px-3 py-2 rounded-lg w-full bg-white border-2 border-gray-300 placeholder-gray-600 shadow-md focus:placeholder-gray-500 focus:bg-white focus:border-gray-600 focus:outline-none">
                                    </div>

                                    <button type="submit" class="flex justify-center m-auto pt-3">  
                                        <a class="relative items-center justify-start inline-block px-4 py-1 overflow-hidden font-bold rounded-full group">
                                            <span class="w-32 h-32 rotate-45 translate-x-12 -translate-y-2 absolute left-0 top-0 bg-white opacity-[3%]"></span>
                                            <span class="absolute top-0 left-0 w-48 h-48 -mt-1 transition-all duration-500 ease-in-out rotate-45 -translate-x-56 -translate-y-24 bg-blue-500 opacity-100 group-hover:-translate-x-8"></span>
                                            <span class="relative w-full text-left text-blue-500 transition-colors duration-200 ease-in-out group-hover:text-white">Guardar</span>
                                            <span class="absolute inset-0 border-2 border-blue-500 rounded-full"></span>
                                        </a>
                                    </button>
                                </form>
                                <form :action="change_password_action" method="post">
                                    <div class="py-1">
                                        <span class="px-1 text-sm text-gray-600">Contraseña</span>
                                        <input type="hidden" name="csrfmiddlewaretoken" :value="csrf_token_form">
                                        <input required placeholder="" type="password" x-model="password" name="passw"
                                            class="text-md block px-3 py-2 rounded-lg w-full
                                bg-white border-2 border-gray-300 placeholder-gray-600 shadow-md focus:placeholder-gray-500 focus:bg-white focus:border-gray-600 focus:outline-none">
                                    </div>

                                    <button type="submit" class="flex justify-center m-auto pt-3">  
                                        <a class="relative items-center justify-start inline-block px-4 py-1 overflow-hidden font-bold rounded-full group">
                                            <span class="w-32 h-32 rotate-45 translate-x-12 -translate-y-2 absolute left-0 top-0 bg-white opacity-[3%]"></span>
                                            <span class="absolute top-0 left-0 w-48 h-48 -mt-1 transition-all duration-500 ease-in-out rotate-45 -translate-x-56 -translate-y-24 bg-blue-500 opacity-100 group-hover:-translate-x-8"></span>
                                            <span class="relative w-full text-left text-blue-500 transition-colors duration-200 ease-in-out group-hover:text-white">Guardar</span>
                                            <span class="absolute inset-0 border-2 border-blue-500 rounded-full"></span>
                                        </a>
                                    </button>
                                </form>
                                <form :action="upload_pic_action" method="post">
                                    <div class="py-1">
                                        <span class="px-1 text-sm text-gray-600">Foto de perfil</span>
                                        <input type="hidden" name="csrfmiddlewaretoken" :value="csrf_token_form">
                                        <input required value="" placeholder="" type="file" name="profile_pic_file" accept="image/png, image/jpeg"
                                            class="text-md block px-3 py-2 rounded-lg w-full bg-white border-2 border-gray-300 placeholder-gray-600 shadow-md focus:placeholder-gray-500 focus:bg-white focus:border-gray-600 focus:outline-none">
                                    </div>

                                    <button type="submit" class="flex justify-center m-auto pt-3">  
                                        <a class="relative items-center justify-start inline-block px-4 py-1 overflow-hidden font-bold rounded-full group">
                                            <span class="w-32 h-32 rotate-45 translate-x-12 -translate-y-2 absolute left-0 top-0 bg-white opacity-[3%]"></span>
                                            <span class="absolute top-0 left-0 w-48 h-48 -mt-1 transition-all duration-500 ease-in-out rotate-45 -translate-x-56 -translate-y-24 bg-blue-500 opacity-100 group-hover:-translate-x-8"></span>
                                            <span class="relative w-full text-left text-blue-500 transition-colors duration-200 ease-in-out group-hover:text-white">Guardar</span>
                                            <span class="absolute inset-0 border-2 border-blue-500 rounded-full"></span>
                                        </a>
                                    </button>
                                </form>

                            </div>
        
                        </form>
                    </div>
                </div>
        </section>

            <br>
            <h1 class="uppercase font-extrabold text-2xl text-center border-b-2 border-black p-4">Imagenes subidas</h1>
            <section class='px-13 overflow-y-scroll max-h-[40rem]'>
                <img v-for="i in user_page_pics_urls" :src="i" class="py-3 w-2/3 m-auto"/>
            </section>
            <br>
        </div>

        <div v-else class="flex justify-center min-h-screen items-center">
            <h1> 
                <p id="text" class="show text-2xl text-gray-800">This user doesn't exist yet</p>
            </h1>
        </div>

    </div>

</div>
</template>

<style>
::-webkit-scrollbar{
    display: none;
  }
  
  *{
    scrollbar-width: none; 
    -ms-overflow-style: none; 
  }
  #text {
    font-family: 'Sansita Swashed';
  }
</style>