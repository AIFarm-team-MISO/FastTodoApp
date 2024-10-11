# Todo(할일) 관련 API

# 라우팅 , 예외처리
from fastapi import APIRouter, HTTPException, Depends

# API스키마
from app.schemas import TodoCreate, TodoUpdate, TodoResponse

## DB 연결 후 추가
# DB세션 관리 및 의존성 주입
from sqlalchemy.orm import Session          

# CRUD 함수
from app.crud import create_todo, get_all_todos, update_todo
from app.dependencies import get_db
from typing import List


# 라우터 생성
router = APIRouter()

# 임시 데이터베이스 역할을 하는 리스트
# todos_db = []

"""
    GET 요청: todo 목록 조회
    '/todos' 경로로 GET 요청이 들어오면,
    데이터베이스에서 모든 할 일을 조회하여 반환
"""
@router.get("/todos", response_model=List[TodoResponse])
async def get_tasks(db: Session = Depends(get_db)):

    todos = get_all_todos(db)

    return todos


'''
    POST 요청: 새로운 할 일 생성
    '/todos' 경로로 POST 요청이 들어오면 아래 함수가 실행됨
    새로운 할일을 사용자가 요청시 보낸 제목, 본문, 완료값으로 
    새로운 할 일을 생성하고 데이터베이스에 저장

'''
@router.post("/todos", response_model=TodoResponse)
async def create_tasks(todo: TodoCreate, db: Session = Depends(get_db)):

    new_todo = create_todo(db=db, todo = todo)

    return new_todo

'''
    PUT 요청: 기존의 할일을 찾아 수정
    '/todos/{todo_id}' 경로로 PUT 요청이 들어오면 실행
    해당 id의 할 일을 찾아 요청 데이터를 바탕으로 수정
    해당 id의 할 일이 없는 경우 404 오류 반환

'''
@router.put("/todos/{todo_id}", response_model=TodoResponse)
async def update_existing_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated_todo = update_todo(db=db, todo_id = todo_id, todo=todo)
    if updated_todo is None:  
        raise HTTPException(status_code=404, detail="todo not found") 
            
    return updated_todo
        
    