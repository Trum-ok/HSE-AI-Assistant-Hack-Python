import torch
import pandas as pd

from typing import Callable
from transformers import BertModel, BertTokenizer

print("Loading models...", end="")
model_name = "DeepPavlov/rubert-base-cased-sentence"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)
print("OK")


def get_sentence_embedding(sentence: str) -> torch.Tensor:
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
        embedding = outputs.last_hidden_state[:, 0, :].squeeze()
    return embedding


def string2embedding(string: str) -> torch.Tensor:
    return torch.Tensor([float(i) for i in string.split()])


def embedding2string(embedding: torch.Tensor) -> str:
    return " ".join([str(i) for i in embedding.tolist()])


def generate_submit(data_path: str, predict_func: Callable, save_path: str, use_tqdm: bool = True) -> None:
    if use_tqdm:
        import tqdm

    data = pd.read_excel(data_path)

    bar = range(len(data))
    if use_tqdm:
        bar = tqdm.tqdm(bar, desc="Predicting")

    submit_df = pd.DataFrame(columns=["solution_id", "author_comment", "author_comment_embedding"])

    for i in bar:
        idx = data.index[i]
        task_row = data.iloc[i]['description']
        level_row = data.iloc[i]['level']
        solution_row = data.iloc[i]['student_solution']
        rout_row = data.iloc[i]['output']
        input_row = data.iloc[i]['input']
        test_type = data.iloc[i]['type']

        text = predict_func(task_row, level_row, solution_row, rout_row, input_row, test_type)
        print(text)
        print("="*70)
        embedding = embedding2string(get_sentence_embedding(text))

        submit_df.loc[i] = [idx, text, embedding]

    submit_df.to_csv(save_path, index=False)
