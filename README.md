# 🎰 AI Lotto Predictor

> FastAPI + PostgreSQL + React 기반의 AI 로또 번호 예측 웹 애플리케이션

---

## 📖 프로젝트 개요

**AI Lotto Predictor**는 과거 로또 당첨 데이터를 기반으로
**빈도 분석(Frequency Analysis)** 을 통해 다음 회차 번호를 예측하는 웹 애플리케이션입니다.
백엔드는 **FastAPI**, 프론트엔드는 **React + Vite**, 데이터베이스는 **PostgreSQL** 로 구성되어 있습니다.

---

## 🚀 주요 기능

✅ **로또 번호 예측**

* 과거 데이터의 출현 빈도를 분석하여,
  가장 자주 등장한 번호를 기반으로 다음 회차의 예측 번호를 생성합니다.

✅ **데이터베이스 관리 (PostgreSQL)**

* 당첨 번호 저장 및 예측 기록 관리
* Alembic을 통한 마이그레이션 지원

✅ **프론트엔드 UI (React)**

* 간단하고 직관적인 웹 UI
* 로또 번호 시각화 (번호 색상, 그룹 구분 등)

✅ **백엔드 API (FastAPI)**

* `/predict` : 번호 예측 API
* `/history` : 과거 당첨 데이터 조회 API

✅ **Docker 기반 실행**

* 백엔드, 프론트엔드, DB 전체를 Docker Compose로 손쉽게 실행
* 로컬 환경 차이 없이 동일한 실행 보장

---

## 🧩 기술 스택

| 구분                  | 기술                                               |
| ------------------- | ------------------------------------------------ |
| **Frontend**        | React, Vite, Axios, TailwindCSS                  |
| **Backend**         | FastAPI, SQLAlchemy, Alembic                     |
| **Database**        | PostgreSQL                                       |
| **ML/AI**           | Python (pandas, numpy, scikit-learn, tensorflow) |
| **Infra**           | Docker, Docker Compose                           |
| **Version Control** | Git / GitHub                                     |

---

## 🏗️ 프로젝트 구조

```
ai_lotto_predictor/
│
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI 엔트리포인트
│   │   ├── database.py          # PostgreSQL 연결 설정
│   │   ├── models.py            # SQLAlchemy 모델 정의
│   │   ├── schemas.py           # Pydantic 스키마 정의
│   │   ├── crud.py              # DB CRUD 로직
│   │   ├── prediction.py        # 번호 예측 알고리즘 (빈도 분석)
│   │   └── routers/
│   │       ├── predict.py       # /predict 엔드포인트
│   │       └── history.py       # /history 엔드포인트
│   ├── requirements.txt
│   └── backend.Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx              # React 메인 컴포넌트
│   │   ├── components/
│   │   │   └── LottoResult.jsx  # 예측 결과 UI
│   │   └── api/
│   │       └── axiosClient.js   # 백엔드 API 호출 설정
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## ⚙️ 실행 방법

### 1️⃣ 사전 준비

* Docker Desktop 설치 (Windows/Mac)
* Git 설치 (선택, 버전 관리용)

### 2️⃣ 프로젝트 클론

```bash
git clone https://github.com/username/ai_lotto_predictor.git
cd ai_lotto_predictor
```

### 3️⃣ Docker Compose로 전체 실행

```bash
docker compose up --build
```

> 첫 실행 시, 필요한 패키지를 자동으로 설치하며
> 약 **1~3분 정도** 소요될 수 있습니다.

---

## 🌐 서비스 접속

| 서비스                        | 주소                                                       |
| -------------------------- | -------------------------------------------------------- |
| **Frontend (React)**       | [http://localhost:5173](http://localhost:5173)           |
| **Backend (FastAPI Docs)** | [http://localhost:8000/docs](http://localhost:8000/docs) |
| **Database (PostgreSQL)**  | localhost:5432                                           |

---

## 🧠 예측 알고리즘 개요

현재 모델은 **단순 빈도 기반 예측**을 사용합니다:

1. 과거 회차 데이터를 모두 수집
2. 각 번호(1~45)의 출현 횟수를 계산
3. 상위 빈도 번호 6개를 선택
4. 중복/패턴을 피하도록 무작위 가중치 조정

---

## 🧰 개발 및 버전 관리

### Git 초기화

```bash
git init
git add .
git commit -m "v1.0 - Initial release"
git tag -a v1.0 -m "Stable version"
```

### 새 버전 커밋 예시

```bash
git add .
git commit -m "v1.1 - Improved UI and API performance"
git tag -a v1.1 -m "Frontend enhancement"
git push origin main --tags
```

---

## 📦 환경 변수 (.env 예시)

`.env` 파일은 프로젝트 루트에 생성하세요:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=lotto_db
POSTGRES_HOST=lotto-db
POSTGRES_PORT=5432
```

---

## 🧹 초기화 및 정리

```bash
# 모든 컨테이너 중지 및 삭제
docker compose down -v

# 캐시 정리
docker system prune -a
```

---

## 👨‍💻 개발자 정보

**Author:** [TEO]
**Email:** [teo.baek@outlook.com]
**GitHub:** [https://github.com/teo-baek]

---

## 🪪 라이선스

MIT License © 2025 [teo]
