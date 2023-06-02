<template>
  <!-- Nav inicio sesión -->
  <nav class="md:flex md:flex-grow items-center justify-items-center bg-blue-900 md:px-5 py-2 sticky top-0 z-50" v-if="user_store.is_logged">

    <button class="flex items-center text-white p-1 px-2 md:ml-12 rounded-full mx-auto my-1 md:my-auto">
        <img src="../assets/t.png" class="w-10 mr-2">
        <RouterLink to="/" class=" link-underline link-underline-black text-2xl tracking-tight" id="text">TikTravel</RouterLink>
    </button>

    <div class="flex md:flex-grow items-center justify-items-center mx-auto my-1 md:my-auto">
      <div class="flex md:flex-grow items-center justify-items-center mx-auto my-1 md:my-auto">
        <button class="p-3">
          <RouterLink to="/viajes" class="text-gray-200 p-1 hover:text-white font-medium">Viajes</RouterLink>
        </button>
        <button class="p-3">
          <RouterLink to="/descubre" class="text-gray-200 p-1 hover:text-white font-medium">Descubre</RouterLink>
        </button>
        <button class="p-3">
          <RouterLink to="/reservas" class="text-gray-200 p-1 hover:text-white font-medium">Reservas</RouterLink>
        </button>
      </div>
      <form class="flex">

      <button type="submit" class="flex items-center justify-items-center rounded-lg md:mr-3 px-1 mx-auto my-2 md:my-auto group">
        <RouterLink :to="profile_path">
          <img :src="profile_pic_url" class="m-auto object-cover w-11 h-11 rounded-full hover-image-1 flex-shrink-0">
        </RouterLink>
      </button>

      <button type="submit" formmethod="get" :formaction="logout_action" class="flex items-center justify-items-center border border-white hover:bg-white rounded-lg md:mr-3 px-1 mx-auto my-2 md:my-auto group">
        <p class="text-sm text-white group-hover:text-blue-900 p-2">Cerrar Sesión</p> 
      </button>
    </form>
    </div>
  </nav>
  <!-- Nav no inicio sesión -->
  <nav class="md:flex md:flex-grow items-center justify-items-center bg-blue-900 md:px-5 py-2 sticky top-0 z-50" v-else>

    <button class="flex items-center text-white p-1 px-2 md:ml-12 rounded-full mx-auto my-1 md:my-auto">
        <img src="../assets/t.png" class="w-10 mr-2">
        <RouterLink to="/" class=" link-underline link-underline-black text-2xl tracking-tight" id="text">TikTravel</RouterLink>
        <!-- <span class="font-semibold text-xl tracking-tight"><RouterLink to="/">TikTravel</RouterLink></span> -->
    </button>

    <div class="flex md:flex-grow items-center justify-items-center mx-auto my-1 md:my-auto">
      <div class="flex md:flex-grow items-center justify-items-center mx-auto my-1 md:my-auto">
        <button class="p-3">
          <RouterLink to="/viajes" class="text-gray-200 p-1 hover:text-white font-medium">Viajes</RouterLink>
        </button>
        <button class="p-3">
          <RouterLink to="/descubre" class="text-gray-200 p-1 hover:text-white font-medium">Descubre</RouterLink>
        </button>
        <div class=" h-8 w-px bg-gray-300"></div>
        <div class="flex">
          <button class="p-3">
            <!-- aqui vvael routerlink sin <a></a> -->
          <RouterLink to="/login" class="text-white p-1" id="m">Inicia sesión</RouterLink>
          </button>
        </div>
      </div>
    </div>
  </nav>

</template>

<!-- <script setup>
    import {computed} from "vue";
    import {UserStatusStore} from '@/stores/user_status'
    const user_store = UserStatusStore()
    const logged = computed({
      get() {
        console.log(user_store.is_logged, 0)
        return user_store.is_logged
      },
      // set(val) {
      //   someReactiveRef.value = val
      // }
    })
</script> -->
  
<script setup>
  import { ref } from 'vue';
  import {UserStatusStore} from '@/stores/user_status'
  import axios from 'axios'
  import {ApiHostStore} from '@/stores/api_hosts'
  
  const api_store = ApiHostStore()
  const user_store = UserStatusStore()

  const logout_action = api_store.get_api_host + '/api-auth/logout'
  const usern = ref('')

  if (api_store.is_dev) {
    var base_host = api_store.get_api_host;
  } else {
    var base_host = window.location.origin+'/';
  }
  const axios_instance = axios.create({
      baseURL: base_host,
  });
  
  const profile_pic_url = ref('')
  const profile_path = ref('')
  function get_profile_pic() {
        let data = {'current_user_page': window.location.pathname};
        axios_instance.post('api/profile-pic', data=data)
        .then(function (response) {
            console.log(response);
            profile_pic_url.value = response.data['profile_pic_src'];
        })
        .catch(function (error) {
            console.log(error);
        })
        .finally(function () {
          // console.log('profile_pic_url =', profile_pic_url.value);
      });
  }

  function api_login_status() {
      // let header = {'csfrtoken': document.cookie};
      // axios.get(api_store.get_host+'api-auth/hi', {headers: header})
      // axios.defaults.headers.common['HTTP_CSFRTOKEN'] = document.cookie;
      // console.log(axios.defaults.headers);
      axios_instance.get('api-auth/hi')
      .then(function (response) {
          console.log(response);
          user_store.yes_logged();
          usern.value = response.data['username'];
          profile_pic_url.value = response.data['profile_pic_src'];
          profile_path.value = { name: 'user', params: { username: (response.data['username']) }};
          // get_profile_pic();
      })
      .catch(function (error) {
          console.log(error);
          user_store.not_logged();

      })
      .finally(function () {
          console.log('logged =', user_store.is_logged);
      });
  }
  api_login_status();
  window.setInterval(api_login_status, 2*60*1000);
  // get_profile_pic();
  // if (user_store.is_logged) {
  //   get_profile_pic();
  // }
  
</script>

<style>
#id{
  font-family: 'Lobster';
}
  .link-underline {
		border-bottom-width: 0;
		background-image: linear-gradient(transparent, transparent), linear-gradient(#fff, #fff);
		background-size: 0 2px;
		background-position: 0 100%;
		background-repeat: no-repeat;
		transition: background-size .5s ease-in-out;
	}

	.link-underline-black {
		background-image: linear-gradient(transparent, transparent), linear-gradient(#FFFFFF, #FFFFFF)
	}

	.link-underline:hover {
		background-size: 100% 2px;
		background-position: 0 100%
	}

  #m {
    position: relative;
    color: #ffffff;
    text-decoration: none;
  }
  
  #m:hover {
    color: #ffffff;
  }
  
  #m::before {
    content: "";
    position: absolute;
    display: block;
    width: 100%;
    height: 1px;
    bottom: 0;
    left: 0;
    background-color: #ffffff;
    transform: scaleX(0);
    transition: transform 0.5s ease;
  }
  
  #m:hover::before {
    transform: scaleX(1);
  }

</style>