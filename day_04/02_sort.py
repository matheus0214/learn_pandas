#%%
import pandas as pd

df = pd.read_csv('../data/clientes.csv', sep=';')
# %%
df['qtdePontos'].sort_values(ascending=False)
# %%
df.sort_values(by='qtdePontos', ascending=False).head()['idCliente']
# %%
test = pd.DataFrame({
    'name': ['teo', 'ana', 'nah', 'jose'],
    'age': [12, 31, 18, 21],
    'rate': [2311, 1111, 2311, 1112]
})
# %%
test.sort_values(by=['rate', 'age'], ascending=[False, True])