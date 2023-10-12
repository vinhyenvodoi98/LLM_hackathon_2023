import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    colors: {
      text: '#050703',
      background: '#e6f1df',
      primary: '#89bd65',
      secondary: '#d5e8c5',
      accent: '#669c43',
    },
    fontSize: {
      sm: "0.75rem",
      base: "1rem",
      lg: "1.25rem",
      xl: "1.5rem",
      "2xl": "2rem",
      "3xl": "3rem",
    },
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        md: '3rem',
        lg: '4rem',
        xl: '5rem',
        '2xl': '6rem',
      },
    },
    animations: {
      "slide-left-right": {
        // Xác định các bước trong animation
        from: {
          // Di chuyển ảnh sang trái
          transform: "translateX(-100%)",
        },
        to: {
          // Di chuyển ảnh sang phải
          transform: "translateX(0%)",
        },
      },
    }
  },
  plugins: [require("daisyui")],
}
export default config
