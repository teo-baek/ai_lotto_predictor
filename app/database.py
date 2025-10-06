from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL 연결 URL (Docker 환경에서 'lotto-db' 컨테이너 이름 사용)
SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://postgres:postgres@lotto-db:5432/lotto_db"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
