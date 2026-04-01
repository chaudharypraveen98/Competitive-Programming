function applyDarkTheme() {
  if (typeof document === 'undefined') return;
  document.documentElement.classList.add('dark');
}

export { applyDarkTheme };
