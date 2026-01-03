#%%
import pandas as pd

df = pd.DataFrame({
    'name': ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    'surname': ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
    'salary': []
})

df
# %%
df.drop_duplicates()