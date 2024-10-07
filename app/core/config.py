# 환경 설정 (예: 데이터베이스 URL)

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# 환경 변수에서 'EVN' 변수를 가져오거나, 기본값을 development 로 설정
env_name = os.getenv('ENV', 'development')

# ENV 값에 따라 해당하는 .evn 파일을 로드
if env_name == 'production':
    load_dotenv('.env.production')
else:
    load_dotenv('.env.development')

# Mysql 데이터베이스 URL (사용자명, 비번, 호스트, 포트, DB이름)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# 테스트용 출력문

print(f"Using environment: {env_name}")
print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")

# SQLALchemy 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 로컬 생성기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#SQLAlchemy의 베이스 클래스 생성
Base = declarative_base()


