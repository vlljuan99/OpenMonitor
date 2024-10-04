# Usar la imagen oficial de Node.js
FROM node:16-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos package.json y package-lock.json
COPY package*.json ./

# Instalar las dependencias
RUN npm install

# Copiar el resto de los archivos del proyecto
COPY . .

# Construir la aplicación
RUN npm run build

# Exponer el puerto 8080
EXPOSE 8080

# Comando para iniciar el servidor de desarrollo de Vue.js
CMD ["npm", "run", "serve"]
