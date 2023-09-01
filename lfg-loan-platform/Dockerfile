# Stage 1: Build the Angular application
FROM node:lts-alpine as build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Serve the Angular application from Nginx
FROM nginx:alpine
COPY --from=build /app/dist/lfg-loan-platform /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
