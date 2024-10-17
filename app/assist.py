import re
import time
from typing import Optional

from utils.utils import exec_code
from app.models.yandexgpt import YandexGPT


class Assistant:
    def __init__(self,
                 system_prompt: str,
                 ask_prompt: str,
                 check_prompt: str,
                 too_long_prompt: str,
                 main_llm_token: str,
                 folder_id: str,
                 main_llm_temperature: float
                ) -> None:
        self.sys_prompt = system_prompt
        self.ask_prompt = ask_prompt
        self.check_prompt = check_prompt
        self.too_long_prompt = too_long_prompt
        self.llm_token = main_llm_token

        self.folder_id = folder_id
        self.main_llm_temperature = main_llm_temperature
        self.llm = YandexGPT(token=self.llm_token,
                             system_prompt=self.sys_prompt,
                             folder_id=self.folder_id,
                             temperature=self.main_llm_temperature
                            )

    def _get_prompt(self, description: str, level: str, student_solution: str, inputs: str, output: str, student_out: str) -> Optional[str]:
        return self.ask_prompt.format(description=description,
                                      level=level,
                                      student_solution=student_solution,
                                      input=inputs,
                                      output=output,
                                      student_output=student_out
                                    )

    def _generate_hint(self, prompt: str) -> str:
        return self.llm.ask(prompt)

    def _check_hint(self, hint: str) -> str:
        if len(hint) > 400:
            hint = self.llm.ask(self.too_long_prompt, clear_history=False)
        check_prompt = self.check_prompt.format(hint=hint)
        hint = self.llm.ask(check_prompt)
        return hint

    def _hash_quota_attack(self, code: str) -> str:
            """Удаляет комментарии из кода, игнорируя HEX цвета."""
            code_without_multiline = re.sub(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', '', code)
            hex_pattern = r'#[0-9a-fA-F]{3,6}\b'
            def replace_comment(match):
                if re.match(hex_pattern, match.group(0)):
                    return match.group(0)
                return ''

            code_without_singleline = re.sub(r'#.*', replace_comment, code_without_multiline)
            cleaned_code = code_without_singleline.strip()
            return cleaned_code

    def predict(self,
                description: str,
                level: str,
                student_solution: str,
                output: str,
                inputs: str,
                test_type: str
                ) -> str:
        cleaned_code = self._hash_quota_attack(student_solution)
        student_output = exec_code(cleaned_code, inputs)
        prompt = self._get_prompt(description, level, cleaned_code, inputs, output, student_output)

        # print(cleaned_code, "\n\n", inputs, "\n\n", student_output, "\n", output)

        # hints = []
        # for i in range(3):
        #     hints.append(self._generate_hints(prompt))

        hint = self._generate_hint(prompt)
        if test_type == 'open':
            hint = "Ошибка в открытых тестах. \n\n" + hint
        # hint = self._check_hint(hint)
        time.sleep(1)
        return hint
