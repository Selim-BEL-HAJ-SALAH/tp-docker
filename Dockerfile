# Utiliser l'image de base datascientest/fastapi:1.0.0
#FROM datascientest/fastapi:1.0.0

# Exposer le port 8000 sur lequel l'API sera accessible
#EXPOSE 8000

# Commande pour démarrer l'API quand le conteneur sera lancé
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# Dockerfile
FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip && pip install requests

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
