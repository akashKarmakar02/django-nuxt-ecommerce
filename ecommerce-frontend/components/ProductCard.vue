<script setup lang="ts">
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

const { product }: { product?: Product } = defineProps(['product']);
</script>

<template>
    <div class="card text-center">
        <img :src="product.image_urls" alt="product thumb" class="thumb">
        <p class="font-bold text-gray-500 m-4 truncate">{{ product.product_name }}</p>
        <NuxtLink :to="`/products/${product.uid}`">
            <p class="btn my-4">View Details</p>
        </NuxtLink>
    </div>
</template>

<style scoped>
.thumb {
    max-height: 200px;
    max-width: 70%;
    margin: 0 auto;
}
</style>