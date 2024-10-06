# Todo(할일) 관련 API

from fastapi import APIRouter

# 라우터 생성
router = APIRouter()

# todo 목록 가져오기 API
@router.get("/todos")
async def get_tasks():
    return {"todos": ["Task 1", "Task 2", "Task 3"]}

# todo 추가 API
@router.post("/todos")
async def create_tasks():
    return {"message": "Todo created"}