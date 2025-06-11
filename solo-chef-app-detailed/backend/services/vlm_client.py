import os
import requests
from typing import List

HF_API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("환경 변수 HF_TOKEN을 설정해주세요.")

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def extract_ingredients(image_bytes: bytes) -> List[str]:
    """
    image_bytes: 이미지 파일 바이트
    return: 재료 이름 리스트
    """
    response = requests.post(HF_API_URL, headers=headers, files={"file": image_bytes})
    data = response.json()
    caption = data.get("generated_text", "")
    raw_items = caption.replace("및", ",").split(",")
    ingredients = [item.strip() for item in raw_items if item.strip()]
    return ingredients