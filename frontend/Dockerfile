# build stage
FROM node:lts-alpine AS build-stage
WORKDIR /app
COPY package*.json ./

# Use the cache to avoid downloading the dependencies again
RUN --mount=type=cache,target=/root/.cache/npm \ 
    npm install --global serve

# Also use the cache to avoid downloading the dependencies again
RUN --mount=type=cache,target=/root/.cache/npm \ 
    npm install

COPY . /app

RUN npm run build

EXPOSE 3000
CMD ["serve", "-s", "dist"]