import os

# BCI: read but never declared in .env.example/docker-compose.yml.
SESSION_SECRET = os.environ["SESSION_SECRET"]
DATABASE_URL = os.environ["DATABASE_URL"]
