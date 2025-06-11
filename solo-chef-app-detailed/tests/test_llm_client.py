import sys, os
import pytest
# 프로젝트의 backend 경로 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
from services.llm_client import generate_recipe

def mock_generator(prompt, max_length, num_return_sequences):
    return [{"generated_text": '{"title":"테스트","cook_time":"5분","difficulty":"쉬움","steps":["step1"]}'}]

def test_generate_recipe(monkeypatch):
    import services.llm_client as llm_mod
    monkeypatch.setattr(llm_mod, "generator", mock_generator)
    recipe = generate_recipe(["달걀"], "test")
    assert isinstance(recipe, dict)
    assert recipe.get("title") == "테스트"