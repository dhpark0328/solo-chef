from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from services.vlm_client import extract_ingredients
from services.llm_client import generate_recipe
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="SoloChef API", version="1.0")

@app.post("/recommend", summary="레시피 추천", tags=["recommendation"])
async def recommend(file: UploadFile = File(...)):
    """
    이미지 파일을 받아 재료를 인식하고, 해당 재료로 만들 수 있는
    1인분 레시피(조리 시간, 난이도 포함)를 반환합니다.
    """
    try:
        image_bytes = await file.read()
        logging.info("이미지 수신: size=%d bytes", len(image_bytes))

        ingredients = extract_ingredients(image_bytes)
        if not ingredients:
            raise ValueError("인식된 재료가 없습니다.")

        constraints = "조리 시간과 난이도를 함께 안내"
        recipe = generate_recipe(ingredients, constraints)

        response = {
            "ingredients": ingredients,
            "recipe": recipe
        }
        logging.info("추천 결과 반환: 재료=%s", ingredients)
        return JSONResponse(response)

    except Exception as e:
        logging.error("추천 처리 중 오류: %s", e)
        raise HTTPException(status_code=500, detail=str(e))