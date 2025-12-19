#%%

import pandas as pd

df_clients = pd.read_csv('../data/clientes.csv', sep=';')
df_clients

#%%
df_clients.head(n=10)

#%%
df_clients.tail()

#%%
df_clients.sample(n=5) # amostra aleatória

#%%
df_clients.shape

#%%
df_clients.columns

#%%
df_clients.index

#%%
df_clients.info(memory_usage='deep') # memory_usage=True memória usada realmente

#%%
df_clients.dtypes['qtdePontos'] #type(df_clients.dtypes)
