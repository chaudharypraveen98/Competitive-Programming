# UI Theme Documentation

This document describes the color palette and theming system for the Competitive Programming Visualizer.

## Color Philosophy

All colors are designed for dark mode to ensure proper contrast and readability.

- **Primary colors**: Used for main text, headings, and interactive elements
- **Secondary colors**: Used for muted text, subtitles, and supporting content
- **Neutral colors**: Used for backgrounds, borders, and subtle UI elements
- **Accent colors**: Used sparingly for highlights and call-to-actions

## Color Palette

### Text Colors
- `text-primary`: `#f1f5f9` (slate-100) - Main headings and primary content
- `text-secondary`: `#94a3b8` (slate-400) - Subtitles, descriptions, muted text
- `text-neutral`: `#64748b` (slate-500) - Neutral text, labels

### Background Colors
- `bg-primary`: `#0f172a` (slate-900) - Main app background
- `bg-card`: `#1e293b` (slate-800) - Card/component backgrounds

### Border Colors
- `border-card`: `#334155` (slate-700) - Card borders, main dividers
- `border-subtle`: `#475569` (slate-600) - Subtle borders, form elements

### Accent Colors
- `success`: `#22c55e` (green-500) - Success states, confirmations
- `warning`: `#f59e0b` (amber-500) - Warnings, cautions
- `error`: `#ef4444` (red-500) - Errors, destructive actions
- `info`: `#3b82f6` (blue-500) - Information, links

## Usage Examples

### Basic Components
```jsx
// Main text
<h1 className="text-text-primary">Title</h1>

// Card component
<div className="bg-bg-card border border-border-card text-text-primary">
  <p className="text-text-secondary">Description</p>
</div>

// Button
<button className="bg-bg-card text-text-primary hover:bg-bg-primary border border-border-subtle">
  Click me
</button>
```

### Form Elements
```jsx
// Input field
<input
  className="bg-bg-card border border-border-subtle text-text-primary placeholder:text-text-secondary focus:border-info"
/>

// Label
<label className="text-text-neutral">Field Label</label>
```

## Developer Guidelines

1. **Always use theme colors**: Instead of hardcoded colors like `text-slate-100`, use `text-text-primary`
2. **Test contrast ratios**: Aim for 4.5:1 minimum for text accessibility
3. **Semantic naming**: Use primary for main content, secondary for supporting content
4. **Accent sparingly**: Reserve accent colors for important actions and states
5. **Consistent spacing**: Use the established color hierarchy throughout the app

## Configuration

Colors are defined in `tailwind.config.js` under the `theme.extend.colors` section. Update that file to modify colors globally.

## Accessibility Notes

- All text colors meet WCAG AA contrast requirements on their respective backgrounds
- Focus states use the `info` accent color for consistency
- Error states use `error` red for clear visual feedback