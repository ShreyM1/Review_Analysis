import pandas as pd
from scipy.stats import mannwhitneyu
import itertools

df = pd.read_csv("specificities.csv")

grouped = df[['AI Model', 'Specificity']].dropna().groupby('AI Model')
model_pairs = list(itertools.combinations(grouped.groups.keys(), 2))

results = []
for model1, model2 in model_pairs:
    data1 = df[df['AI Model'] == model1]['Specificity']
    data2 = df[df['AI Model'] == model2]['Specificity']
    stat, p = mannwhitneyu(data1, data2, alternative='two-sided')
    results.append({
        'Model 1': model1,
        'Model 2': model2,
        'U Statistic': stat,
        'Raw P-Value': p
    })

results_df = pd.DataFrame(results)

results_df['P-Value (Bonferroni)'] = results_df['Raw P-Value'] * len(results_df)

significant_results = results_df[results_df['P-Value (Bonferroni)'] < 0.05].sort_values('P-Value (Bonferroni)')

print("All Pairwise Comparisons:")
print(results_df.to_string(index=False))

print("\nSignificant Differences After Bonferroni Correction (p < 0.05):")
print(significant_results.to_string(index=False))