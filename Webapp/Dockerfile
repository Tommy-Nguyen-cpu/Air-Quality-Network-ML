FROM node:latest

WORKDIR /usr/src/app
RUN npm install -g @angular/cli
ADD . .
RUN npm install
CMD ng serve --host 0.0.0.0
