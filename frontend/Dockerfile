FROM node:20-slim

WORKDIR /frontend

COPY package*.json ./

# npm lock 제거 후 항상 최신 클린 설치
RUN rm -rf package-lock.json node_modules && npm install

COPY . .

EXPOSE 5173
CMD ["npm", "run", "dev"]
