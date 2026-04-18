# [What kind of things must you be wary of when designing or developing for multilingual sites?](https://www.greatfrontend.com/interviews/study/gfe75/questions/quiz/designing-or-developing-for-multilingual-sites)

# Designing and Developing for Multilingual Sites

Internationalization (i18n) is the process of planning and implementing products so they can be adapted to specific local languages and cultures without engineering changes.

## 1. Linguistic & Cultural Nuances
* **Language vs. Locale:** A "language" (e.g., English) is distinct from a "locale" (e.g., `en-US` vs `en-GB`). Locales determine not only language but also formats for dates, times, numbers, and currencies.
* **Avoid Cultural Assumptions:** Do not assume a language maps to a single country. Always offer options for specific regions (e.g., `zh-CN` for Simplified Chinese vs `zh-TW` for Traditional Chinese).
* **Text Expansion/Contraction:** Words in languages like German or French are often significantly longer than English. Design flexible, responsive containers that can accommodate longer strings without breaking the layout.
* **Directionality (RTL/LTR):** Support Right-to-Left (RTL) languages like Arabic and Hebrew. This requires mirroring your layout, including icons, sidebars, and navigation patterns.

## 2. Development Best Practices
* **Never Concatenate Strings:** Avoid code like `"Hello, " + name`. Grammatical structures vary across languages. Use template strings with variables (e.g., `I will travel on {date}`) so the variable can be positioned correctly based on language grammar.
* **Externalize Text:** Keep hardcoded text out of your source code. Use JSON or YAML translation files to separate content from logic, allowing translators to work without touching the codebase.
* **Avoid Text in Images:** Never embed text within raster images (PNG, JPG). This makes localization impossible. Use CSS, web fonts, and overlays instead.
* **Dynamic Formatting:** Never hardcode date formats (e.g., `MM/DD/YYYY`). Use built-in JavaScript APIs like `Intl.DateTimeFormat` or libraries to format dates, times, and currencies based on the user's locale.

## 3. SEO & UX Strategy
* **HTML `lang` Attribute:** Always define the `lang` attribute on the `<html>` tag. This helps browsers and assistive technologies (screen readers) correctly interpret the language of the page content.
* **`hreflang` Tags:** Include `<link rel="alternate" hreflang="...">` tags in your `<head>`. This signals search engines that pages are related but tailored for specific languages/regions, preventing duplicate content penalties.
* **The `x-default` Tag:** Always include an `hreflang="x-default"` link. This acts as the fallback for users whose language is not explicitly supported by your site.
* **Predict but Don't Restrict:** It is acceptable to suggest a language based on browser headers (`Accept-Language`) or IP detection, but **always** provide a manual override. Never lock a user into a version based on an assumption.

## 4. Key Takeaways for Interviews
* **Architecture:** Focus on separating content from code (i18n libraries).
* **Layout:** Prioritize flexibility and support for RTL/LTR layouts.
* **Formatting:** Emphasize localization-aware libraries.
* **SEO:** Highlight the importance of `lang` and `hreflang` metadata.