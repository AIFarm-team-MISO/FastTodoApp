# FastTodoApp
## 프로젝트 개요
FastTodoApp은 FastAPI를 기반으로 한 간단하고 확장 가능한 Todo 관리 애플리케이션입니다.  
이 프로젝트는 FastAPI의 고성능 비동기 기능과 REST API 구조를 학습하고,  
AWS 서버에 배포하여 실시간으로 Todo를 관리할 수 있는 시스템을 구축하는 것을 목표로 합니다.  

## 프로젝트 진행상황
- **FastAPI 서버 설정 완료**  
FastAPI 서버 구조를 구축하고, 기본적으로 Uvicorn으로 서버를 실행하여  
REST API 테스트를 할 수 있도록 설정하였습니다.  

- **요청 및 응답 모델 정의**  
Pydantic을 사용하여 TodoCreate, TodoUpdate, TodoResponse 등의 모델을 정의했으며  
이를 통해 POST, PUT 요청을 통한 데이터 검증 및 응답 구조를 설정했습니다.  

- **CRUD 기능 구현**  
할 일 생성, 조회, 수정, 삭제 기능을 구현하고,  
임시 저장소로 todos_db 리스트를 사용하여 동작을 테스트했습니다.  
Uvicorn 서버를 통해 API 테스트를 완료했으며,  
Swagger UI와 ReDoc을 통해 API 엔드포인트와 문서를 손쉽게 확인할 수 있습니다.  

- **AWS 서버에 배포 및 포트 설정**  
AWS EC2 인스턴스에 FastAPI 프로젝트를 배포하였으며,  
포트 8080에서 서버를 실행하도록 설정했습니다.  
보안 그룹 인바운드 규칙을 설정하여 외부에서 해당 포트로   
접근할 수 있도록 구성했습니다.  

# 차후 작업계획
데이터베이스(MySQL 등)를 연동하여 임시 저장소(todos_db) 대신 영구 저장소로 전환할 예정입니다.  

# 서버테스트 방법  
- **클라이어트 요청 테스트**  
브라우저에서 아래의 링크로 확인가능  
http://3.39.6.220:8080/docs (Swagger UI)  

Swagger 페이지에서 다양한 API 엔드포인트들을 확인할 수 있으며  
Try it out 버튼을 클릭해 실제로 API 요청을 보낼 수 있습니다.  

**POST 요청: 할일 생성**  
POST 클릭 ->  Try it out 클릭 -> title, description -> Excute클릭  
이후 하단 Responses에 200의 code가 나오면 성공, Response body 내용확인가능  
**각각의 값은 임의로 작성가능**  

**GET 요청: 할일 가져오기**  
POST 클릭 ->  Try it out 클릭
이후 하단 Responses에 200의 code가 나오면 성공, Response body 내용확인가능  
**POST 실행후에 확인가능**  

**PUT 요청: 할일 수정**  
POST 클릭 -> Try it out 클릭 -> todo_id 값을 입력  
-> title, description, is_completed 값 입력 -> Excute클릭  
이후 하단 Responses에 200의 code가 나오면 성공, Response body 내용확인가능  
**이후 GET요청을 실행하여 변경내용 확인가능**


- **API문서확인**  
브라우저에서 아래의 링크로 확인가능  
http://3.39.6.220:8080/redoc (API 문서)

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