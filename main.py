import os
from dotenv import load_dotenv

from utils.prompts import sys_prompt
from app.assist import Assistant
from submition.submit import generate_submit


if __name__ == "__main__":
    load_dotenv()

    asistant = Assistant(
        system_prompt=sys_prompt,
        main_llm_token=os.getenv('MAIN_LLM_TOKEN'),
        # sub_llm_token=os.getenv('SUB_LLM_TOKEN'),
    )

    generate_submit(
        test_solutions_path='../data/raw/test/solutions.xlsx',
        tasks_path='../data/raw/tasks.xlsx',
        predict_func=asistant.predict,
        save_path='../data/processed/submission.csv',
    )
