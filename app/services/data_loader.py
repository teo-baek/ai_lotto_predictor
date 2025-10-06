import pandas as pd
import numpy as np
from sqlalchemy.orm import Session
from app.models.db_models import LottoDraw


def load_lotto_data(filepath: str, db: Session):
    df = pd.read_excel(filepath)

    for _, row in df.iterrows():
        numbers = [int(row[f"num{i}"]) for i in range(1, 7)]
        record = LottoDraw(
            draw_no=int(row["회차"]),
            numbers=[int(n) for n in numbers],
            bonus=int(row["보너스"]),
            first_prize=None,
            first_winners=None,
        )
        db.add(record)
    db.commit()
    print(f"{len(df)}개의 회차 데이터가 성공적으로 업로드되었습니다.")
