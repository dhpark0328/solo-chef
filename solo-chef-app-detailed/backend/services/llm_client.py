import os
from transformers import pipeline, logging
from typing import List, Dict

logging.set_verbosity_error()

generator = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base",
    device=0 if os.getenv("USE_CUDA") == "1" else -1
)

def generate_recipe(ingredients: List[str], constraints: str) -> Dict:
    """
    ingredients: 인식된 재료 리스트
    constraints: 추가 요청사항(조리 시간, 난이도 등)
    return: 레시피 객체
    """
    prompt = (
        f"자취생 맞춤 레시피:\n"
        f"재료: {', '.join(ingredients)}\n"
        f"요청사항: {constraints}\n"
        f"1인분 기준으로 조리 시간, 난이도를 포함하여\n"
        f"단계별로 JSON 형태로 반환해주세요."
    )
    output = generator(prompt, max_length=512, num_return_sequences=1)[0]["generated_text"]
    try:
        import json
        recipe = json.loads(output)
    except Exception:
        recipe = {"title": "레시피 결과", "details": output}
    return recipe