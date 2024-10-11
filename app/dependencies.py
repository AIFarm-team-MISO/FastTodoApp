from sqlalchemy.orm import Session
from app.core.config import SessionLocal
from typing import Generator

# 데이터베이스의 세션을 생성하고 반환
'''
    - 데이터베이스 세션을 생성하고 반환하는 함수 -  

    데이터베이스 세션을 요청마다 생성하고, 요청이 끝나면 세션을 종료
    이 함수는 FastAPI의 Depends를 통해 의존성 주입에 사용
    세션이 사용된 곳에서 처리가 끝나면 자동으로 세션을 닫아준다.
'''
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal() # 데이터베이스 세션 생성
    try:
        yield db        # 요청이 처리되는 동안 데이터베이스 세션을 제공
    finally:
        db.close()      # 요청이 완료되면 데이터베이스 세션을 종료