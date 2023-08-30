export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
  ],
  routeRules: {
    '/cart': { ssr: false },
  },
})
