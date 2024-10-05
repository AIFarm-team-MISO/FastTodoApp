# FastTodoApp
## 프로젝트 개요
FastTodoApp은 FastAPI를 기반으로 한 간단하고 확장 가능한 Todo 관리 애플리케이션입니다.  
이 프로젝트는 FastAPI의 고성능 비동기 기능과 REST API 구조를 학습하고,  
AWS 서버에 배포하여 실시간으로 Todo를 관리할 수 있는 시스템을 구축하는 것을 목표로 합니다.  

## 프로젝트 흐름 (Flow)
사용자는 REST API를 통해 새로운 할 일을 생성, 수정, 삭제, 조회할 수 있습니다.  
FastAPI가 사용자 요청을 처리하여 백엔드에서 비동기로 데이터를 처리하고 응답을 반환합니다.  
데이터베이스는 각 Todo 항목을 저장하며, 이를 기반으로 API 응답을 제공합니다.  
AWS 서버에 배포하여 프로젝트의 실제 운영 환경에서 동작을 확인할 수 있으며,  
로컬 개발 환경과 프로덕션 환경 설정이 분리되어 있습니다.  

## 프로젝트 파일 구조 
문서참조경로  
FastTodoApp/doc/forder structure 

## 주요 기능 및 특징
- **CRUD 기능:** 사용자는 Todo 항목을 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)할 수 있습니다.
- **RESTful API:** HTTP 메서드(GET, POST, PUT, DELETE)를 통해 Todo 항목을 효율적으로 관리할 수 있습니다.
- **비동기 처리:** FastAPI의 비동기 기능을 활용해 빠르고 성능 높은 API 응답을 제공합니다.
- **Pydantic 모델:** 요청 및 응답 데이터의 유효성을 검증하는 간단하고 강력한 데이터 모델링을 제공합니다.
- **다중 환경 지원:** 로컬 개발 환경과 AWS 프로덕션 환경을 구분한 설정 파일을 통해 효율적인 배포 및 유지보수가 가능합니다.
- **테스트 코드:** 기본적인 API 동작을 확인할 수 있는 유닛 테스트가 포함되어 있어 코드의 안정성을 보장합니다.

## 기술 스택
- **언어:** Python 3.9+
- **프레임워크:** FastAPI
- **데이터베이스:** SQLite (개발 환경), PostgreSQL (프로덕션 환경)
- **서버:** AWS EC2 (Ubuntu), Nginx, Gunicorn
- **패키지 관리:** Pydantic, SQLAlchemy, Uvicorn, pytest
- **배포:** Docker, GitHub Actions (CI/CD)
- **기타:** JWT 인증 (추가 기능 예정)

## 프로젝트 안내사항
**현재 10월04일 기준으로 새로운 프로젝트를 진행하였으며 매일매일 업데이트될 예정입니다.**   