# Używamy środowiska Node.js do uruchomienia Angulara
FROM node:20

WORKDIR /app

# Najpierw instalujemy zależności (żeby Docker mógł to skeszować)
COPY package*.json ./
RUN npm install
RUN npm install -g @angular/cli

# Kopiujemy resztę projektu frontendu
COPY . .

# Uruchamiamy serwer developerski z dostępem z zewnątrz
EXPOSE 4200
CMD ["ng", "serve", "--host", "0.0.0.0"]