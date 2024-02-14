# build stage
FROM node:lts-alpine AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install --global serve
RUN npm install

COPY . /app

RUN npm run build

EXPOSE 3000
CMD ["serve", "-s", "dist"]