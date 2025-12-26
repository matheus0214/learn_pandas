#%%
import pandas as pd

df = pd.read_csv('../data/transacao_produto.csv', sep=';')
df.head()

#%%
# código de produto 5 e 11
df[(df['IdProduto'] == '5') | (df['IdProduto'] == '11')]

#%%
df[df['IdProduto'].isin(['5', '11'])]

#%%
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.shape

#%%
clientes[clientes['DtCriacao'].notna()]

#%%
clientes[~clientes['DtCriacao'].notna()]