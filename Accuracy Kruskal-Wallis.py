import pandas as pd
from scipy.stats import kruskal

df = pd.read_csv("accuracies.csv")

grouped_data = df.groupby("AI Model")["Accuracy"].apply(list)

statistic, p_value = kruskal(*grouped_data)

print(f"Kruskal–Wallis statistic: {statistic}")
print(f"P-value: {p_value}")