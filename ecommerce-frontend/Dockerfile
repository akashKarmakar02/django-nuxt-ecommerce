FROM node:18.16.0-slim

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

EXPOSE 3000
EXPOSE 24678

CMD npm run build && npm run preview
