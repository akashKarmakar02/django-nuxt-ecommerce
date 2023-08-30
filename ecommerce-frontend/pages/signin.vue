<template>
    <div>
        <div class="max-w-md justify-center items-center mx-auto">
            <form @submit.prevent="handleSumbit" class="card">
                <h1 class="text-2xl font-semibold justify-center mb-4">Sign in</h1>
                <div class="mb-6">
                    <label for="email" class="text-sm mb-2 font-medium">Your Email</label>
                    <input type="email"
                        class="bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 focus:border-gray-400 focus:ring-gray-400 block mb-2 w-full"
                        placeholder="Email" v-model="email" required>
                </div>
                <div class="mb-6">
                    <label for="email" class="text-sm mb-2 font-medium">Your Password</label>
                    <input type="password"
                        class="bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 focus:border-gray-400 focus:ring-gray-400 block mb-2 w-full"
                        placeholder="Password" v-model="password" required>
                </div>
                <button class="bg-[#12b488] text-white px-4 py-2 rounded-md" type="submit">Submit</button>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
let email: string;
let password: string;

async function handleSumbit(event: Event) {
    const response = await fetch('http://127.0.0.1:8000/api/accounts/login/', {
        method: "POST",
        headers: { 'Content-type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({
            email: email,
            password: password,
        })
    })
    const jwt = useCookie('jwt');
    const data = await response.json();
    jwt.value = data['jwt'];
    navigateTo('/');
}

</script>

<style scoped></style>