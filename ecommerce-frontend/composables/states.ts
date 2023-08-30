export const useCount = () => useState('counter', () => 0)
export const useCartItems = () => useState('cart_items', () => [] as any[])