# Setup color
https://realtimecolors.com/

Select color and update in `tailwind.config.ts`

```ts
import type { Config } from 'tailwindcss'

const config: Config = {
  ...
  theme: {
    colors: {
      text: '#050703',
      background: '#e6f1df',
      primary: '#89bd65',
      secondary: '#d5e8c5',
      accent: '#669c43',
    },
  },
}
export default config
```
Then we can use this color like bg-primary, text-accent,...

# Responsive design

|Breakpoint |prefix|	Minimum width	CSS|
|---|---|---|
|sm	|640px	|@media (min-width: 640px) { ... }|
|md	|768px	|@media (min-width: 768px) { ... }|
|lg	|1024px	|@media (min-width: 1024px) { ... }|
|xl	|1280px	|@media (min-width: 1280px) { ... }|
|2xl	|1536px	|@media (min-width: 1536px) { ... }|

# Marquee
https://www.npmjs.com/package/react-fast-marquee
