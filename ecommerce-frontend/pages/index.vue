<template>
    <div class="mt-8">
        <div class="grid grid-cols-2 lg:grid-cols-4 md:grid-cols-3 space-x-4 space-y-2">
            <div v-for="product in products">
                <ProductCard :product="product" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import ProductCard from "~/components/ProductCard.vue";

interface Product {
    uid: string;
    product_name: string;
    slug: string;
    category: string;
    price: number;
    product_description: string;
    color_variant: string[];
    size_variant: string[];
    image_urls: string;
}

const jwt = useCookie('jwt')

const { data: response } = await useFetch('http://127.0.0.1:8000/api/products/');
const userResponse = await fetch('http://127.0.0.1:8000/api/accounts/user/', {
    credentials: 'include',
})
console.log(await userResponse.json());
const products = response.value;

</script>

<style scoped></style>