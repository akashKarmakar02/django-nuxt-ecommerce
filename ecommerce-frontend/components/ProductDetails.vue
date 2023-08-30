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
    image_urls: string[];
}

const { product }: { product?: Product } = defineProps(['product']);
let productSize: string;
let color_variant: string;
function handleBuy() {
    console.log(productSize);
}

async function handleAddToCart() {
    const response = await useFetch('http://127.0.0.1:8000/api/cart/add/', {
        headers: { 'Content-type': 'application/json' },
        method: "POST",
        credentials: 'include',
        body: JSON.stringify({
            product_uid: product?.uid,
            size_variant: productSize,
            color_variant: color_variant,
        })
    })
}
</script>

<template>
    <div class="card">
        <div class="grid grid-cols-2 gap-10">
            <div class="p-7">
                <img :src="product.image_urls[0]" alt="product image" class="mx-auto my-7 img">
            </div>
            <div class="p-7">
                <h2 class="text-4xl my-7">{{ product.product_name }}</h2>
                <p class="text-xl my-7">Price - ${{ product.price }}</p>
                <h3 class="font-bold border-b-2 mb-4 pb-2">Product Description</h3>
                <p class="mb-7">{{ product.product_description }}</p>

                <h3 class="mb-4 font-semibold text-gray-900">Sizes</h3>
                <div class="flex justify-start mb-4">
                    <ul
                        class="items-center text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg sm:flex">
                        <li class=" border-b border-gray-200 sm:border-b-0 sm:border-r"
                            v-for="size in product.size_variant">
                            <div class="flex items-center pl-3">
                                <input id="horizontal-list-radio-license" type="radio" :value="size" name="list-radio"
                                    v-model="productSize" class="w-4 h-4 text-[#12b488] bg-[#12b488] border-gray-300">
                                <label for="horizontal-list-radio-license"
                                    class="w-full py-3 px-4 ml-2 text-sm font-medium text-gray-900">{{ size }}
                                </label>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="flex justify-start space-x-4">
                    <button class="btn" v-on:click="handleBuy">Buy</button>
                    <button class="btn" v-on:click="handleAddToCart">Add to Cart</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
img {
    max-width: 400px;
}
</style>