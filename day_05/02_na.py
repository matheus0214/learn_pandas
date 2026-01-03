#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
# %%
df.shape

# %%
df.dropna()
# %%
df = pd.DataFrame({
    'name': ['teo', None, 'nah', 'marcio'],
    'age': [None, None, 43, 52],
    'salary': [122, 1221, None, 1231]
})
df
# %%
df.dropna()
# %%
df.dropna(subset=['age'])
# %%
df['age'].fillna(0)

#%%
df.fillna({'name': 'alguem', 'age': 0})
# %%
df.fillna(df[['salary']].mean())
