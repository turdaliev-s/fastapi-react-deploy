from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.router import router as router_crypto

app = FastAPI()

app.include_router(router_crypto)


origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 Разрешаем запросы от любых источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы
    allow_headers=["*"],  # Разрешаем все заголовки
)
