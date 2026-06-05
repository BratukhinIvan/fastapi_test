# Как задеплоить FastAPI на сервер
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get(path: "users", tags=["Пользователи"], summary="Получить пользователей")
async def get_users():
    return [{"id": 1, "name": "Artem"}]

if __name__ == "__main__":
    uvicorn.run(app: "main7:app", host="0.0.0.0", port=8000)
