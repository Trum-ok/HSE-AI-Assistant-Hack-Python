import json
from sklearn.model_selection import train_test_split

with open('./data/datasets/ChatDataset.json', 'r') as file:
    data = json.load(file)

train_data, val_data = train_test_split(data, test_size=0.2, random_state=42)

# Функция для сохранения данных в формате .jsonl
def save_to_jsonl(filename, dataset):
    with open(filename, 'w', encoding='utf-8') as outfile:
        for record in dataset:
            json.dump(record, outfile, ensure_ascii=False)
            outfile.write('\n')

save_to_jsonl('./data/datasets/train_chat.jsonl', train_data)

save_to_jsonl('./data/datasets/val_chat.jsonl', val_data)

print(f"Данные успешно разбиты на train_chat.jsonl {len(train_data)} и val_chat.jsonl {len(val_data)}")
