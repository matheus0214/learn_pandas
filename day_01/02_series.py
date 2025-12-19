# %%

ages = [
    12, 89, 45, 78, 29,
    34, 36, 28, 47, 52,
    27, 23, 24, 32, 41
]

age_median = sum(ages) / len(ages) # média

diffs = 0 # variância
for i in ages:
    diffs += (i - age_median)**2

diffs / (len(ages) - 1)

# %%

import pandas as pd

series_ages = pd.Series(ages)
series_ages

# %%
series_ages.mean()
series_ages.var()
series_ages.describe()