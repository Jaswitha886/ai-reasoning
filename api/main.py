from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="AI Reasoning System")

app.include_router(router)
