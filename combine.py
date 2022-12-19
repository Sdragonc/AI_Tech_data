import pandas as pd
combined_csv = pd.read_csv('annotation_csvs_split_by_person_YC.csv', encoding='utf-8')
for name in ["GU", "DI", "SH", "JD"]:
    tmp = pd.read_csv(f"annotation_csvs_split_by_person_{name}.csv", encoding='utf-8')
    pd.concat([combined_csv, tmp],  axis=0)
combined_csv.to_csv('combined_csv.csv')
