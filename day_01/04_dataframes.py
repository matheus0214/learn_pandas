# %%
import pandas as pd

ages = [
    12, 89, 45, 78, 29,
    34, 36, 28, 47, 52,
    27, 23, 24, 32, 41
]

names = [
    "Maria", "Pedro", "Ana", "João", "Luis",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Tito"
]

series_ages = pd.Series(ages)
series_names = pd.Series(names)

# %%
df = pd.DataFrame()
df['ages'] = series_ages
df

# %%
df['names'] = series_names
df

# %%
type(df), type(df['names'])

# %%
df['ages']

# %%

df.iloc[0]['names']

# %%
df.iloc[-1]['ages']