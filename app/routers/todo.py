# Todo(할일) 관련 API

# 라우팅 , 예외처리
from fastapi import APIRouter, HTTPException

# API스키마
from app.schemas import TodoCreate, TodoUpdate, TodoResponse
from typing import List


# 라우터 생성
router = APIRouter()

# 임시 데이터베이스 역할을 하는 리스트
todos_db = []

# GET 요청: todo 목록 조회
@router.get("/todos")
async def get_tasks():
    return todos_db

'''
    POST 요청: 새로운 할 일 생성
    '/todos' 경로로 POST 요청이 들어오면 아래 함수가 실행됨
    데이터베이스에 저장할 새로운 할일을 사용자가 요청시 보낸 제목, 본문, 완료값으로 딕셔너리로 생성
    

'''
@router.post("/todos")
async def create_tasks(todo: TodoCreate):
    new_todo = {
        "id": len(todos_db) +1,
        "title": todo.title,
        "description":todo.description,
        "is_completed":todo.is_competed
    }
    todos_db.append(new_todo)

    return new_todo

'''
    PUT 요청: 기존의 할일을 찾아 수정
    '/todos/{todo_id}' 경로로 PUT 요청이 들어오면 실행
    해당 id의 할 일이 없는 경우 404 오류 반환

'''
@router.put("/todos/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, todo: TodoUpdate):
    for existing_todo in todos_db:
        if existing_todo["id"] == todo_id:
            if todo.title is not None:
                existing_todo["title"] = todo.title
            if todo.description is not None:
                existing_todo["description"]  = todo.description
            existing_todo["is_completed"] = todo.is_competed
            return existing_todo
    raise HTTPException(status_code=404, detail="todo not found") 