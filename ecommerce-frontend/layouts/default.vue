<template>
    <div>
        <NuxtLoadingIndicator />
        <header class="px-8 pt-4">
            <nav class="flex justify-between">
                <NuxtLink to="/" class="text-2xl">Shopping Market</NuxtLink>
                <ul class="flex space-x-4">
                    <NuxtLink to="/">Home</NuxtLink>
                    <li>Search</li>
                    <NuxtLink to="/cart" v-if="isLoggedIn()">Cart</NuxtLink>
                    <NuxtLink to="/signin" v-if="!isLoggedIn()">Sign in</NuxtLink>
                    <NuxtLink to="/register" v-if="!isLoggedIn()">Register</NuxtLink>
                    <li v-if="isLoggedIn()">
                        <button v-on:click="logout">Logout</button>
                    </li>
                </ul>
            </nav>
        </header>
    </div>
    <div class="px-8 pt-4">
        <slot />
    </div>
</template>

<script setup lang="ts">


function isLoggedIn() {
    const token = useCookie('jwt', {
        httpOnly: true,
        secure: true,
        sameSite: 'none'
    });
    return !!token.value;
}
async function logout(event: Event) {
    const token = useCookie('jwt');
    token.value = null;
    await fetch("http://127.0.0.1:8000/api/accounts/logout/", {
        credentials: 'include',
    })
}
</script>

<style scoped>
.router-link-exact-active {
    @apply text-[#12b488]
}
</style>