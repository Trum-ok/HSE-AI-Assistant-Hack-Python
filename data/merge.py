import pandas as pd

tasks_df = pd.read_excel('./data/raw/test/tasks.xlsx')
tests_df = pd.read_excel('./data/raw/test/tests.xlsx')
solutions_df = pd.read_excel('./data/raw/test/solutions.xlsx')

tasks_df = tasks_df.drop(columns=['author_solution'])
solutions_df = solutions_df.drop(columns=['author_comment', 'author_comment_embedding'])

merged_df = pd.merge(solutions_df, tasks_df, left_on='task_id', right_on='id', how='left')
merged_df = pd.merge(merged_df, tests_df, on='task_id', how='left')
merged_df['solution_id'] = merged_df['id_x']

final_df = merged_df[['solution_id', 'task_id', 'level', 'description', 'student_solution', 'input', 'output', 'type']].copy()
final_df.to_excel('./data/raw/test/merged_data.xlsx', index=False)

print("Данные успешно объединены и сохранены в 'merged_data.xlsx'.")
