# build stage
FROM node:20-alpine AS builder

WORKDIR /app

# Copy requirements
COPY package.json package-lock.json ./
RUN npm install --frozen-lockfile

# Copy source code
COPY . .
RUN npm run build

# runtime stage
FROM nginx:alpine

WORKDIR /usr/share/nginx/html

# Clean standart files nginx
RUN rm -rf ./*

# Copy image from builder
COPY --from=builder /app/dist/ ./

# Copy custom config for nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
