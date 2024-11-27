#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import CategoricalDtype
import numpy as np

# %%
df=pd.read_csv('StudentPerformanceFactors.csv')
# %%
df
# %%
df['TIPO_DE_ESCOLA']=df['School_Type'].apply(lambda x : 1 if x == 'Private' else 0) 
# %%
df_publico=df[df['TIPO_DE_ESCOLA']==0]
df_private=df[df['TIPO_DE_ESCOLA']==1]
df.shape

# %%

plt.hist(df['Sleep_Hours'], bins= 13)
plt.xlabel('Hours of Sleep')
plt.ylabel('Frequency')
plt.title('Histogram of Sleep Hours')
plt.show()
# %%
descr_publibo=df_publico.describe()
descr_publibo
# %%
plt.figure(figsize=(10, 6))
sns.histplot(df_publico['Exam_Score'],color='gray', bins=50, label='White Wine')
sns.histplot(df_private['Exam_Score'],color='red', bins=50, label='Red Wine')
plt.xlabel("Exam_Score")
plt.ylabel('frequency')
plt.title('Histogram of Exam_Score Content for White and Red Wines')
plt.legend()
plt.show()



# %%
plt.figure(figsize=(10,6))
sns.histplot(df_publico['Tutoring_Sessions'],color='blue',bins=10,label='blue wine')
sns.histplot(df_private['Tutoring_Sessions'],color='red',bins=10,label='red wine')

# %%
print(df['Teacher_Quality'].value_counts())
print(df['Exam_Score'].value_counts())
# %%
colunas_lista = list(df.columns)
# %%
colunas_lista
variaveis_quantitativas = df.select_dtypes(include=['number']).columns.tolist()
# %%
pearson_corr = df[variaveis_quantitativas].corr(method='pearson')
spearman_corr = df[variaveis_quantitativas].corr(method='spearman')

print("Pearson Correlation:\n", pearson_corr)


# %%
sns.pairplot(df[variaveis_quantitativas])
plt.show()
# %%
sns.lmplot(x='Hours_Studied', y='Exam_Score', data=df)

#sns.lmplot(x='residual_sugar', y='total_sulfur_dioxide', data=vinho)
plt.show()
# %%
df