import abc
from typing import Optional


class BaseModel(abc.ABC):
    """Абстрактный класс для всех моделей"""

    # TODO: доработать с учетом features и ... в данных таблицах
    def __init__(self, system_prompt: Optional[str] = None) -> None:
        self.messages = []
        self.system_prompt = system_prompt
        pass

    def __call__(self, *args, **kwargs) -> Optional[str]:
        return self.ask(*args, **kwargs)

    @abc.abstractmethod
    def ask(self, user_message: str,
            clear_history: bool = True) -> Optional[str]:
        """Отправка запроса к ассистенту для получения ответа"""
        pass
