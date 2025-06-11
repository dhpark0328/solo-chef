import sys, os
import pytest
# 프로젝트의 backend 경로 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
from services.vlm_client import extract_ingredients

class MockResp:
    def __init__(self):
        self._json = {"generated_text": "달걀, 우유, 양파"}
    def json(self):
        return self._json

def mock_post(url, headers, files):
    return MockResp()

def test_extract_ingredients(monkeypatch):
    import services.vlm_client as vlm_mod
    monkeypatch.setattr(vlm_mod.requests, "post", mock_post)
    ingredients = extract_ingredients(b"dummy")
    assert "달걀" in ingredients
    assert "우유" in ingredients
    assert "양파" in ingredients