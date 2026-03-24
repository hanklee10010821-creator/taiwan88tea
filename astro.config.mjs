// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://88tea.tw',
  markdown: {
    shikiConfig: { theme: 'github-light' },
  },
});
