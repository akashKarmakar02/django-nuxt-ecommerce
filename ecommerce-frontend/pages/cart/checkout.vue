<template>
    <div class="card relative overflow-x-auto shadow-md sm:rounded-lg px-4 py-2">
        <table class="w-full text-sm text-left text-gray-500">
            <thead>
                <tr>
                    <th scope="col" class="px-6 py-3 bg-gray-50">Product Name</th>
                    <th scope="col" class="px-6 py-3">Color</th>
                    <th scope="col" class="px-6 py-3 bg-gray-50">Size</th>
                    <th scope="col" class="px-6 py-3">Quantity</th>
                    <th scope="col" class="px-6 py-3 bg-gray-50">price</th>
                </tr>
            </thead>
            <tbody>
                <tr class="border-b border-gray-200" v-for="item in cart_items">
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50">
                        {{ item.product.product_name }}
                    </th>
                    <td class="px-6 py-4">
                        {{ item.color_variant != null ? item.color_variant : 'Default' }}
                    </td>
                    <td class="px-6 py-4 bg-gray-50">
                        {{ item.size_variant != null ? item.size_variant : 'Default' }}
                    </td>
                    <td class="px-6 py-4">
                        {{ item.item_count }}
                    </td>
                    <td class="px-6 py-4 bg-gray-50">
                        ${{ item.product.price * item.item_count }}
                    </td>
                </tr>
                <tr class="border-b border-gray-200">
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap bg-gray-50">
                    </th>
                    <td class="px-6 py-4">
                    </td>
                    <td class="px-6 py-4 bg-gray-50">
                    </td>
                    <td class="px-6 py-4">
                        Total:
                    </td>
                    <td class="px-6 py-4 bg-gray-50">
                        ${{ cart_items.reduce((sum, item) => sum + (item.product.price * item.item_count), 0) }}
                    </td>
                </tr>
            </tbody>
        </table>

        <div class="px-4">
            <form v-on:submit.prevent="hanndleCheckout">
                <h1 class="text-2xl font-semibold justify-center mb-4">Checkout Form</h1>
                <div class="mb-6">
                    <label class="text-sm mb-2 font-medium">First Name</label>
                    <input type="text"
                        class="bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 focus:border-gray-400 focus:ring-gray-400 block mb-2 w-full"
                        placeholder="First Name" v-model="first_name" required>
                </div>
                <div class="mb-6">
                    <label class="text-sm mb-2 font-medium">Last Name</label>
                    <input type="text"
                        class="bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 focus:border-gray-400 focus:ring-gray-400 block mb-2 w-full"
                        placeholder="Last Name" v-model="last_name" required>
                </div>
                <div class="mb-6">
                    <label class="text-sm mb-2 font-medium">Address</label>
                    <input type="text"
                        class="bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 focus:border-gray-400 focus:ring-gray-400 block mb-2 w-full"
                        placeholder="Address" v-model="address" required>
                </div>
                <div class="mb-6">
                    <label class="text-sm mb-2 font-medium">Phone Number</label>
                    <input type="tel"
                        class="bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 focus:border-gray-400 focus:ring-gray-400 block mb-2 w-full"
                        placeholder="Phone Number" v-model="phone_number" required>
                </div>
                <button class="bg-black text-white px-4 py-2 rounded-md" type="submit">Procced To Pay</button>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { loadStripe } from "@stripe/stripe-js";


const cart_items = useCartItems()
let first_name: string;
let last_name: string;
let address: string;
let phone_number: string;

async function hanndleCheckout() {
    const response = await fetch('http://127.0.0.1:8000/api/cart/checkout/', {
        method: 'POST',
        headers: { 'Content-type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({
            first_name: first_name,
            last_name: last_name,
            address: address,
            phone_number: phone_number,
            cart_items: JSON.stringify(cart_items.value)
        })
    })
    const data = await response.json()

    console.log(data);
    const stripe = await loadStripe(data.SPK as string);
    const result = await stripe?.redirectToCheckout({ sessionId: data.session_id })
    console.log(result);
}
</script>

<style scoped></style>