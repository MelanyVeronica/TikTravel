<template>
    <div id="card" class="px-3 py-4">

        <div class="bg-white shadow-xl rounded-lg overflow-hidden">

            <div class="bg-cover bg-center h-56 p-4" :style=bg_img_src>
                <button type="submit" class="flex float-right">
                    <a href="#" class="text-sm bg-gray-700 hover:bg-gray-800 rounded-lg px-2 text-white p-1.5">Reservado</a>
                </button>
            </div>

            <h3 id="text" class="border-t border-gray-300 text-center text-3xl p-1">Viaje</h3>

            <div class="p-2 flex items-center justify-around">

                <div class="bg-gray-200 flex flex-col w-32 p-3 rounded-xl border-2 border-white">
                    <span class="font-semibold text-sm text-center">Estancia</span>
                    <select id="underline_select" class="text-center block px-0 w-full text-sm text-gray-900 bg-transparent border-b-2 focus:outline-none">
                        <option value="Option 3">Selecciona</option>
                        <option selected value="hotel">Hotel</option>
                        <option value="alojamiento">Alojamiento</option>
                        <option value="apartamento">Apartamento</option>
                        <option value="hostal">Hostal</option>
                        <option value="resort">Resort</option>
                        <option value="casa-rural">Casa rural</option>
                    </select>
                </div>

                <div class="bg-gray-200 flex flex-col w-32 p-3 rounded-xl border-2 border-white">
                    <span class="font-semibold text-sm text-center">¿De dónde?</span>
                    <select id="underline_select" class="text-center block px-0 w-full text-sm text-gray-900 bg-transparent border-b-2 focus:outline-none">
                        <option value="Option 3">Ubicación</option>
                        <option selected value="ATL">Aeropuerto Internacional Hartsfield-Jackson (ATL)</option>
                        <option value="LAX">Aeropuerto Internacional de Los Ángeles (LAX)</option>
                        <option value="ORD">Aeropuerto Internacional de Chicago O'Hare (ORD)</option>
                        <option value="LHR">Aeropuerto de Londres Heathrow (LHR)</option>
                        <option value="CDG">Aeropuerto de París-Charles de Gaulle (CDG)</option>
                        <option value="DXB">Aeropuerto Internacional de Dubái (DXB)</option>
                        <option value="HND">Aeropuerto Internacional de Haneda (HND)</option>
                        <option value="JFK">Aeropuerto Internacional John F. Kennedy (JFK)</option>
                        <option value="SYD">Aeropuerto Internacional Kingsford Smith de Sídney (SYD)</option>
                    </select>
                </div>

            </div>

        </div>

    </div>
</template>

<style>
#card{
    width: 35rem;
}
</style>

<script setup>
import { defineProps } from "vue";
const props = defineProps({
    bg_img_src: '',
})

</script>