from fastapi import FastAPI

from routes import router

app = FastAPI(title="Patchwork demo API")
app.include_router(router)
