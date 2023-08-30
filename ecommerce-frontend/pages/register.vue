<template>
    <div>
        <div class="max-w-md justify-center items-center mx-auto">
            <form @submit.prevent="handleSubmit" class="card">
                <h1 class="text-2xl font-semibold justify-center mb-4">Register</h1>
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
                    <label class="text-sm mb-2 font-medium">Username</label>
                    <input type="text"
                        class="bg-gray-50 border border-gray-300 rounded-lg px-4 py-2 focus:border-gray-400 focus:ring-gray-400 block mb-2 w-full"
                        placeholder="Username" v-model="username" required>
                </div>
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
                        v-model="password" required>
                </div>

                <label class="block mb-2 text-sm font-medium text-gray-900" for="file_input">Upload
                    file</label>
                <input
                    class="block w-full text-sm text-gray-900 py-2 mb-2 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none"
                    id="file_input" type="file" v-on:change="handleFile">
                <button class="bg-[#12b488] text-white px-4 py-2 rounded-md" type="submit">Submit</button>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
let profile_pic: File;
let email: string;
let username: string;
let password: string;
let first_name: string;
let last_name: string;


function handleFile(event: Event) {
    const inputElement = event.target as HTMLInputElement;
    let pic: FileList = inputElement.files!;
    if (!pic) {
        console.log("no pic")
        return;
    }
    profile_pic = pic[0];
}



async function handleSubmit(event: Event) {
    if (!profile_pic) {
        return;
    }
    const formData = new FormData();

    formData.append('profile_image', profile_pic);
    formData.append('email', email);
    formData.append('username', username);
    formData.append('first_name', first_name);
    formData.append('last_name', last_name);
    formData.append('password', password);

    try {
        await useLazyFetch('http://127.0.0.1:8000/api/accounts/register/', {
            method: 'POST',
            body: formData
        });
        console.log("success");
    } catch (e) {
        console.log("failed");
    }
}
</script>

<style scoped></style>