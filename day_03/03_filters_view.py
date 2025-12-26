#%%

import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
df.head()

#%%
ft = df['qtdePontos'] == 0
df_zero = df[ft] # clientes com 0 pontos
df_zero

#%%
df_zero['flag_1'] = 1
df_zero

#%%
df_zero

#%%
df