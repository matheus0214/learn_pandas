# %%

import pandas as pd

ages = [
    12, 89, 45, 78, 29,
    34, 36, 28, 47, 52,
    27, 23, 24, 32, 41
]

series_ages = pd.Series(ages)
series_ages

# %%

ages[0], ages[-1]
series_ages[0]

# %%

series_ages = series_ages.sort_values()

# %%

series_ages.iloc[0], series_ages.iloc[-1]

# %%

series_ages.iloc[:3]

# %%

series_ages.iloc[::-1]

# %%
ages = [
    12, 89, 45, 78, 29,
    34, 36, 28, 47, 52,
    27, 23, 24, 32, 41
]

index_ages = [
    "Maria", "Pedro", "Ana", "João", "Luis",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Tito"
]

series_ages = pd.Series(ages, index_ages)
series_ages

# %%
series_ages.iloc[[1]]

# %%
series_ages.loc["Pedro"] # msm coisa que series_ages["Pedro"]