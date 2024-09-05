/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./src/**/*.{js,jsx,ts,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                "main": "#004389",
                "secondary": "#002e77",
                "accent": "#005db3",
                "accent-secondary": "#25e2ee",
                "accent-tertiary": "#1b91cb",
                "white": "#ffffff",
                "black": "#000000",
            },
        }
    },
    plugins: [],
}
