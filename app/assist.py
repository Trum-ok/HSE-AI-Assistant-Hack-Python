import pandas as pd
from typing import Any

from app.models.yandexgpt import YandexGPT

class Assistant:
    def __init__(self, system_prompt: str, main_llm_token: str):
        self.sys_prompt = system_prompt
        self.llm_token = main_llm_token

    def _generate_hints(self):
        response = YandexGPT()  # передать параметры (подстроить под промпт)
        return response

    def _hints_check(self):
        pass

    def _hash_quota_attack(self, code: str):
        """Функция для выявления атак на модель в комментариях в коде."""
        pass

    def predict(self,
                task: pd.Series,
                student_code: pd.Series,
                **kwargs: Any) -> str:
        pass
