# %%
import pandas as pd
import requests

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

response = requests.get('https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil', headers=header)
dfs = pd.read_html(response.text)
dfs

# %%
df_uf = dfs[1]
df_uf

# %%
df_uf.to_csv('../data/ufs.csv', sep=';', index=False)

#%%
ufs = pd.read_csv('../data/ufs.csv', sep=';')
ufs