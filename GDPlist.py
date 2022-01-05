#%%
import pandas as pd

df = pd.read_csv('GDPlist.csv')
df.info()

# %%
df.rename(columns={'Country':'Nuoc','Continent':'ChauLuc','GDP (millions of US$)':'GDP (trieu $)'},inplace=True)
df
#%%
df['Nuoc']= df['Nuoc'].map(lambda x:x.lstrip('�'))
df.insert(1,'ThanhPho',df.Nuoc)
df

# %%
df['ThanhPho'].replace({'Vietnam':'Hanoi'},inplace=True)
df

# %%
df.drop(df.loc[df.ChauLuc == 'Asia'].index, inplace=True)
df
# %%
df.drop(df.loc[df['GDP (trieu $)']< 300000].index, inplace=True)
df

# %%
