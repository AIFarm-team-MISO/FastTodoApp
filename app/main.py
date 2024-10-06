# FastAPI 앱의 엔트리 포인트

from fastapi import FastAPI
from app.routers import todo

app = FastAPI()

# todo 라우터포함
app.include_router(todo.router)

@app.get("/")
async def root():
    return{"message": "welcome"}
