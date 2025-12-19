#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df

#%%
df.shape

#%%
# df.memory_usage(deep=True)
df.info(memory_usage='deep')

#%%
df.dtypes

#%%
df.rename(columns={'QtdePontos': 'qtdPontos'}, inplace=True)

#%%
df.dtypes

#%%
df[['IdCliente', 'qtdPontos']]

#%%

# SELECT * FROM df
df

#%%

# SELECT idCliente FROM df
df[['IdCliente']]

#%%

# SELECT IdCliente, qtdPontos FROM df LIMIT 5
df[['IdCliente', 'qtdPontos']].sample(5)

#%%
# SELECT IdCliente, IdTransacao, qtdPontos FROM df LIMIT 5

df[['IdCliente', 'IdTransacao', 'qtdPontos']].sample(5)

#%%
c = df.columns.to_list()
c.sort()
c
#%%
df = df[c]

#%%
df