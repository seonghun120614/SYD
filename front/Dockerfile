FROM node:20

WORKDIR /front

COPY package.json .

RUN yarn install

COPY . .

EXPOSE 8080

CMD ["yarn", "preview", "--port", "8080", "--host", "0.0.0.0"]