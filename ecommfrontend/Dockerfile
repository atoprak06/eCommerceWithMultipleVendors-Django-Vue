FROM node:14-slim
WORKDIR /vue-app
COPY . .
RUN npm install
RUN npm install -g live-server
RUN npm install @popperjs/core --save
RUN npm run build
EXPOSE 8080

