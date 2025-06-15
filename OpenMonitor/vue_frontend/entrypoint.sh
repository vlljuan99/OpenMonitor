#!/bin/sh

# Eliminar node_modules y package-lock si existen
rm -rf node_modules package-lock.json

# Instalar las dependencias
npm install --legacy-peer-deps

# Aplicar las correcciones de vulnerabilidades
npm audit fix --force

# Ejecutar el servidor de desarrollo
npm run serve
