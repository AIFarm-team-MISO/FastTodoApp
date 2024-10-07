# Pydantic 스키마(모델) 정의 (요청/응답 데이터 검증)

from pydantic import BaseModel
from typing import Optional

#
'''
    TodoCreate, TodoUpdate 등 공통필드들을 정의하는 모델
    title은 필수이고, description과 is_completed는 선택적 필드

'''
class TodoBase(BaseModel):                  
    title: str                               #할일의 제목(필수)
    description: Optional[str] = None        #할일의본문 (선택)
    is_competed: bool = False                #완료여부

'''
    할일 생성시 사용되는 모델
    pass : 추가필드 없이 TodoBase 그대로 상속

'''
class TodoCreate(TodoBase):                  
    pass

'''
    할일을 수정할 때 사용하는 모델
    필요에 따라 title, description, is_completed를 업데이트 가능
    title이 Optional로 설정되어 있어, 업데이트 시 제목은 선택사항
'''
class TodoUpdate(TodoBase):
    title: Optional[str] = None  

'''
    API 응답 시 사용할 모델
    데이터베이스에서 자동 생성되는 고유 ID를 포함하여 응답 데이터 구조를 정의
    id : 할일의 고유 ID (데이터베이스에서 각 할 일을 식별하는 값, create 이후 DB에 저장이 되어서야 고유ID가 생성됨)
    orm_mode(ORM 모드 설정) : SQLAlchemy 모델 객체에서 Pydantic 모델로 자동 변환을 가능하게 함
'''
class TodoResponse(TodoBase):
    id: int                       

    
    class Config:
        from_attributes  = True   # Pydantic V2 에서 orm_mode 가 from_attributes 로 변경됨