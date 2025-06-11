# SoloChef: 자취생 맞춤 요리 추천 앱

> 냉장고 사진 한 장으로 오늘 만들 수 있는 레시피를 추천받는 혁신적인 서비스

---

## 프로젝트 개요
- **목표**: 자취생 또는 요리 초보가 냉장고 안 재료 사진을 업로드하면, AI가 해당 재료를 인식하고 1인분 기준 레시피와 **조리 시간**, **난이도**를 함께 제공
- **제약**: 유료 모델 사용 불가 → 무료 오픈소스 VLM 및 LLM만 사용
- **주요 기술**: FastAPI, Hugging Face Inference API, Hugging Face Transformers, Python

---

## 디렉터리 구조
```
solo-chef-app/
├── backend/
│   ├── app.py
│   ├── services/
│   │   ├── vlm_client.py
│   │   └── llm_client.py
│   └── requirements.txt
├── tests/
│   ├── test_vlm_client.py
│   └── test_llm_client.py
└── README.md
```

---

## 사전 준비
1. Python 3.10 이상 설치  
2. 가상환경 생성  
3. 의존성 설치: `pip install -r backend/requirements.txt`  
4. 환경 변수 설정:  
   ```bash
   export HF_TOKEN="hf_xxx"
   export USE_CUDA=0
   ```

---

## 실행 방법
```bash
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

API 호출 예:
```bash
curl -X POST "http://localhost:8000/recommend" \
     -F "file=@/path/to/fridge.jpg" \
     -H "Accept: application/json"
```

---