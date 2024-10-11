'''
    데이터베이스와 상호작용하는 함수들을 정의하는 곳

    - Create, Read, Update, Delete와 관련된 함수들을 정의 - 
    Create: 새로운 할 일을 데이터베이스에 추가하는 함수.
    Read: 특정 할 일을 조회하거나, 모든 할 일을 조회하는 함수.
    Update: 기존 할 일의 상태나 내용을 수정하는 함수.
    Delete: 특정 할 일을 삭제하는 함수.

    * 스키마 정의 (schemas.py)와 모델 정의 (models.py)는 기본적으로 서로 일치해야 함

'''

from sqlalchemy.orm import Session
from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate

# 
'''
    Create : 새로운 할일 추가
    
    refresh : 자동 생성된 값(id등) 확인, DB와의 일관성유지
              자동생성된 값이 필요하거나, 입력된 내용을 사용자에게 다시 보여주어야 할경우
              방금생성된 내용을 db로부터 받아올수 있다.
'''
def create_todo(db: Session, todo: TodoCreate):
    new_todo = Todo(
        title = todo.title,
        description = todo.description,
        is_completed = todo.is_competed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo) # 데이터베이스의 최신 상태를 반영하여 new_todo 객체 업데이트
    
    return new_todo

# Read by id : 특정(id) 할일 조회
def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()   #filter()는 SQL 쿼리의 WHERE 절과 유사

# 
# 
'''
    Read : 모든 할일 조회

    offset() : 몇 번째 항목부터 가져올것인가 지정
    limit() : 가져올 데이터 갯수 제한

    둘을 함께 사용하면 페이지네이션을 구현할 수 있음
    예를 들어, offset(0).limit(10)은 처음 10개를 가져오고, offset(10).limit(10)은 다음 10개를 가져오는 방식
'''
def get_all_todos(db: Session, skip: int = 0, limit: int = 0):
    query = db.query(Todo).offset(skip)
    if limit:
        query = query.limit(limit)

    return query.all()

#Update: 할일 수정
def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if existing_todo:
        if todo.title is not None:
            existing_todo.title = todo.title
        if todo.description is not None:
            existing_todo.description  = todo.description
        existing_todo.is_completed = todo.is_competed
        db.commit()
        db.refresh(existing_todo)
    return existing_todo

# Delete: 할일 삭제
def delete_todo(db: Session, todo_id: int):
    existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if existing_todo:
        db.delete(existing_todo)
        db.commit()
    return existing_todo