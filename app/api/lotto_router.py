from fastapi import APIRouter, HTTPException
from app.ml_model import generate_predictions
from app.utils import calculate_frequency

router = APIRouter()


@router.get("/predict")
async def predict_numbers():
    try:
        predictions = generate_predictions()
        freq = calculate_frequency(predictions)
        return {"predictions": predictions, "frequency": freq}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"에러 발생: {str(e)}")
