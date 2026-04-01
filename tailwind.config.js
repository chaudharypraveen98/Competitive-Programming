/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: {
          50: "#eff6ff",
          500: "#3b82f6",
          900: "#1e3a8a",
        },
        secondary: {
          50: "#f0fdf4",
          500: "#22c55e",
          900: "#14532d",
        },
        // Custom theme colors for dark mode
        "text-primary": "#f1f5f9", // slate-100 - Main text
        "text-secondary": "#94a3b8", // slate-400 - Muted text
        "text-neutral": "#64748b", // slate-500 - Neutral text
        "border-card": "#334155", // slate-700 - Card borders
        "border-subtle": "#475569", // slate-600 - Subtle borders
        "bg-card": "#1e293b", // slate-800 - Card backgrounds
        "bg-primary": "#0f172a", // slate-900 - Main backgrounds
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [],
};