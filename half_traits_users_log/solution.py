import glob
import pandas as pd
from functools import reduce

all_files = glob.glob('feature_*.csv')

print(f"Найдено {len(all_files)} CSV файлов для объединения.")

df_list = []

for file in all_files:
  feature_name = file.replace(".csv", "")

  df = pd.read_csv(
      file,
      header=None,
      names=["id", feature_name],
  )
  df_list.append(df)

final_df = reduce(
    lambda left, right: pd.merge(left, right, on="id", how="outer"), df_list
)

feature_cols = [c for c in final_df.columns if c != "id"]
final_df['na'] = final_df[feature_cols].isnull().sum(axis=1)

n_features = len(feature_cols)
threshold = n_features / 2
ans = final_df[final_df['na'] <= threshold].shape[0]

print(f"Количество строк с заполненностью 50% и выше: {ans}")
