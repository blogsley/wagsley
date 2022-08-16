// FILE: vite.config.js

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { quasar, transformAssetUrls } from '@quasar/vite-plugin'

import { ViteAliases } from 'vite-aliases'
import path from 'path'

import { VitePWA } from 'vite-plugin-pwa'

const root = path.resolve('../../packages/blogsley')
const envDir = path.resolve(__dirname, './src/config')
const outDir = path.resolve(__dirname, './wagsley/static/admin')
const publicDir = path.resolve(root, '/public')
const base = '/admin/'

console.log(path.resolve(root, './src'))

// https://vitejs.dev/config/
export default defineConfig({
  root,
  envDir,
  build: {       
     outDir,
  },
  publicDir,
  //base,

  plugins: [
    ViteAliases({
      dir: path.resolve(root, './src'),
    }),
    VitePWA({
      mode: "development",
      base: root,
      srcDir: root,
      filename: "sw.js",
      includeAssets: ["/favicon.png"],
      strategies: "injectManifest",

      manifest: {
        name: 'Blogsley',
        short_name: 'Blogsley',
        description: 'Best PWA App in town!',
        display: 'standalone',
        orientation: 'portrait',
        background_color: '#ffffff',
        theme_color: '#007d7e',
        icons: [
          {
            src: 'public/icons/icon-128x128.png',
            sizes: '128x128',
            type: 'image/png'
          },
          {
            src: 'public/icons/icon-192x192.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: 'public/icons/icon-256x256.png',
            sizes: '256x256',
            type: 'image/png'
          },
          {
            src: 'public/icons/icon-384x384.png',
            sizes: '384x384',
            type: 'image/png'
          },
          {
            src: 'public/icons/icon-512x512.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      }
    }),

    vue({
      template: { transformAssetUrls }
    }),

    quasar({
      sassVariables: path.resolve(root, './src/css/quasar-variables.scss'),
    })
  ]
})
