FROM node:22-alpine

WORKDIR /var/www

COPY . .

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

ENTRYPOINT ["npm", "run", "start"]