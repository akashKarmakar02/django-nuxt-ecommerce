<template>
    <div>
        <ProductDetails :product="product" />
    </div>
</template>

<script setup lang="ts">
const { uid } = useRoute().params;

const { data: product } = await useFetch(`http://127.0.0.1:8000/api/products/${uid}`);

</script>

<style scoped></style>