FROM node:20

# Crear directorio de trabajo
WORKDIR /app

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm install --legacy-peer-deps

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto de Vite
EXPOSE 5174

# Comando por defecto para ejecutar Vite
CMD ["npm", "run", "dev"]
