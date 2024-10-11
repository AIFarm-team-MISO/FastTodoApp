'''
    데이터 베이스의 모델을 정의

    sqlalchemy 가 DB와의 맵핑을 도와주기 때문에 Base 모델을 상속받아 사용함
    그리고 alembic 의 설정에 Base를 상속받은 model 클래스가 필요
    상속받은 클래스로 테이블 이름과 컬럼을 정의해두고 alembic설정파일에
    Base의 메타데이터로 설정을 해두면 Base를 상속받은 클래스의 
    모든 DB정의 를 수집해 DB와의 마이그레이션을 진행하게 됨 
    

'''

from sqlalchemy import Column, Integer, String, Boolean
from .core.config import Base
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__="todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=True)
    is_completed = Column(Boolean, default=False)

