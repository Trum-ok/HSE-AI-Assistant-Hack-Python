import os
from dotenv import load_dotenv

from utils.prompts import sys_prompt, ask_prompt, check_prompt, too_long_prompt
from app.assist import Assistant
from submition.submit import generate_submit


if __name__ == "__main__":
    load_dotenv(override=True)

    if (os.environ["YANDEX_GPT_FOLDER_ID"] is None) or (os.getenv('YANDEX_GPT_IAM_TOKEN') is None):
        print("Yandex GPT folder id or IAM token is not set!")
        exit(-1)

    asistant = Assistant(
        system_prompt=sys_prompt,
        ask_prompt=ask_prompt,
        check_prompt=check_prompt,
        too_long_prompt=too_long_prompt,
        folder_id=os.environ["YANDEX_GPT_FOLDER_ID"],
        main_llm_token=os.getenv('YANDEX_GPT_IAM_TOKEN'),
        main_llm_temperature=0.6
        # sub_llm_token=os.getenv('SUB_LLM_TOKEN'),
    )

    generate_submit(
        data_path='./data/raw/test/merged_data.xlsx',
        predict_func=asistant.predict,
        save_path='./data/processed/submission.csv',
    )
