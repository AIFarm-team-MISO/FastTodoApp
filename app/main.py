# FastAPI 앱의 엔트리 포인트

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "welcome"}
