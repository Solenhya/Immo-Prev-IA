# Utiliser une image de base Python
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances dans le conteneur
COPY requirements_docker.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements_docker.txt

# Copier le code source
COPY . .

# Exposer le port utilisé par l'application
EXPOSE 8000

# Définir la commande de démarrage
ENTRYPOINT ["fastapi","run", "app/main.py"]