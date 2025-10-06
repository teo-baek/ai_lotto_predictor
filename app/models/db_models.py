from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    Date,
    ARRAY,
    Float,
    String,
    TIMESTAMP,
)
from sqlalchemy.sql import func
from app.database import Base


class LottoDraw(Base):
    __tablename__ = "lotto_draws"
    id = Column(Integer, primary_key=True, index=True)
    draw_no = Column(Integer, unique=True, nullable=False)
    numbers = Column(ARRAY(Integer))
    bonus = Column(Integer)
    first_prize = Column(BigInteger, nullable=True)
    first_winners = Column(Integer, nullable=True)
    draw_date = Column(Date, server_default=func.now())


class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    predicted_numbers = Column(ARRAY(Integer))
    model_version = Column(String(50))
    confidence = Column(Float)
    created_at = Column(TIMESTAMP, server_default=func.now())
