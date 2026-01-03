#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep = ';') 
# %%
# selecione a primeira transação diária de cada cliente.

df.head()
# %%
df.sort_values['DtCriacao'].drop_duplicates(subset=['IdCliente'])
# %%
df = df.sort_values('DtCriacao')
df['data'] = pd.to_datetime(df['DtCriacao']).dt.date
# %%
df
# %%
df.drop_duplicates(subset=['IdCliente', 'data'], keep='first')
# %%
first = df.drop_duplicates(keep='first', subset=['IdCliente', 'data'])
last = df.drop_duplicates(keep='last', subset=['IdCliente', 'data'])
# %%
pd.concat([last, first])