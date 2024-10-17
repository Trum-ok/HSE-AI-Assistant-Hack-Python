import json
import pandas as pd

tasks = pd.read_excel('./data/datasets/hackaton_files/for_teams/train/tasks.xlsx')
tests = pd.read_excel('./data/datasets/hackaton_files/for_teams/train/tests.xlsx')
solutions = pd.read_excel('./data/datasets/hackaton_files/for_teams/train/solutions.xlsx')

def create_chat_message(task_row, test_row, solution_row):
    user_message = {
        "role": "user",
        "content": f"Задача: {task_row['description']}. Ввод: {test_row['input']}. Решение студента: {solution_row['student_solution']}."
    }
    bot_message = {
        "role": "bot",
        "content": f"Ошибка: {solution_row['author_comment']}."
    }

    return [user_message, bot_message]

chat_dataset = []

# Итерируем по решениям студентов и матчим с задачами и тестами по task_id
for _, solution_row in solutions.iterrows():
    task_id = solution_row['task_id']
    # Находим соответствующую задачу по task_id
    task_row = tasks[tasks['id'] == task_id].iloc[0]
    # Находим соответствующий тест по task_id (можно выбрать, например, первый тест)
    test_row = tests[tests['task_id'] == task_id].iloc[0]
    messages = create_chat_message(task_row, test_row, solution_row)

    chat_entry = {
        "id": int(solution_row['id']),
        "source": "example",
        "messages": messages
    }
    chat_dataset.append(chat_entry)

with open('./data/datasets/ChatDataset.json', 'w', encoding='utf-8') as f:
    json.dump(chat_dataset, f, ensure_ascii=False, indent=4)

print("Данные успешно сохранены в ChatDataset.json")
