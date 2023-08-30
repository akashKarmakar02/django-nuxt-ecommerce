<template>
    <div>
        <div class="card p-8">
            <div v-if="cart_items.length == 0">
                <p class="text-3xl mb-10 flex justify-center">
                    No Item in you cart
                </p>
                <div class="flex justify-center">
                    <button class="btn" v-on:click="handleContinue">Continue Browsing</button>
                </div>
            </div>
            <div v-for="item in cart_items" :key="item.uid">
                <div class="p-3 rounded-xl bg-slate-100 mt-2 flex justify-between items-center">
                    <div class="flex items-center">
                        <img :src="item.product.image_urls" class="h-16 rounded-lg">
                        <div class="ml-4">
                            {{ item.product.product_name }} {{ item.size_variant != null ? `(${item.size_variant})` : null }}
                            {{ item.color_variant != null ?
                                `(${item.color_variant})` : null }}
                        </div>
                    </div>
                    <div class="flex h-fit items-center space-x-2  py-1 border border-slate-700 rounded-lg">
                        <button class="border-r border-slate-700 px-3"
                            v-on:click="(event) => handleItemDecrement(item)">-</button>
                        <p class="px-2">{{ item.item_count }}</p>
                        <button class="border-l border-slate-700 px-3"
                            v-on:click="(event) => handleItemIncrement(item.product)">+</button>
                    </div>
                </div>
            </div>
            <button class="btn mt-4" v-if="cart_items.length != 0"
                v-on:click="() => navigateTo('/cart/checkout/')">Buy</button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { it } from 'node:test';

const cart_items_state = useCartItems()
const response = await fetch("http://127.0.0.1:8000/api/cart", {
    credentials: 'include'
});
const data = await response.json();
const cart_items = ref(data.cart_items);
cart_items_state.value = cart_items;
console.log(cart_items);

async function handleItemIncrement(product: any) {
    await useFetch('http://127.0.0.1:8000/api/cart/add/', {
        headers: { 'Content-type': 'application/json' },
        method: "POST",
        credentials: 'include',
        body: JSON.stringify({
            product_uid: product?.uid
        })
    })

    const response = await fetch("http://127.0.0.1:8000/api/cart", {
        credentials: 'include'
    });

    const data = await response.json();
    cart_items.value = data.cart_items;
    cart_items_state.value = cart_items;
}

function handleContinue() {
    navigateTo('/');
}

async function handleItemDecrement(item: any) {
    await useFetch('http://127.0.0.1:8000/api/cart/remove/', {
        headers: { 'Content-type': 'application/json' },
        method: "POST",
        credentials: 'include',
        body: JSON.stringify({
            cart_uid: item?.uid
        })
    })

    const response = await fetch("http://127.0.0.1:8000/api/cart", {
        credentials: 'include'
    });

    const data = await response.json();
    cart_items.value = data.cart_items;
    cart_items_state.value = cart_items;
}

</script>

<style scoped></style>