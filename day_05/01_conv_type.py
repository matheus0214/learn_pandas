#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df

#%%
df['qtdePontos'].astype(float)

#%%
df['DtCriacao'] = pd.to_datetime(df['DtCriacao'])

#%%
df['DtCriacao'].dt.year

#%%
df['DtCriacao'].replace(to_replace={'0000-00-00 00:00:00.000': '2026-01-02 15:42:00.000'})