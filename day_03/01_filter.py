#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()

#%%
points_data = [10, 100, 1, 1, 50, 130, 20, 12]
gt_50 = [x for x in points_data if x >= 50]
gt_50

#%%
test = pd.DataFrame(
    {
        'nome': ['teo', 'nah', 'mah'],
        'idade': [32, 35, 14],
        'uf': ['sp', 'pr', 'rj']
    }
)

# filtrar quem tem mais de 18 anos
test_filter = test['idade'] >= 18 # returns a serie

test[test_filter]

#%%

# pega do data frame os que tem a qtd. de pontos maior ou igual a 50
df[df['QtdePontos'] >= 50]

#%%
# filter_points = (df['QtdePontos'] >= 50) * (df['QtdePontos'] <= 100)
filter_points = (df['QtdePontos'] >= 50) & (df['QtdePontos'] <= 100)
df[filter_points]

#%%
filter_points = (df['QtdePontos'] == 1) + (df['QtdePontos'] > 100)
# filter_points = (df['QtdePontos'] == 1) | (df['QtdePontos'] > 100)

df[filter_points]

#%%
# pontos entre 0 e 50 ou do ano de 2025 para frente
filter_points = (df['QtdePontos'] > 0) & (df['QtdePontos'] <= 50) | (df['DtCriacao'] >= '2025-01-01')
df[filter_points]