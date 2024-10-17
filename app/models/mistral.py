from transformers import AutoModelForCausalLM, AutoTokenizer

# Замените 'mistralai/Mistral-Large-Instruct-2407' на нужную вам модель
model_name = "mistralai/Mistral-Large-Instruct-2407"

# Загрузка токенизатора и модели
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Если хотите сохранить модель локально
model.save_pretrained("./mistral_large_instruct_2407")
tokenizer.save_pretrained("./mistral_large_instruct_2407")
