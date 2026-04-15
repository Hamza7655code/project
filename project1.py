import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset.csv')

print(df.head(3))
print(df.tail(3))

print(df.info())

print(df.isnull().sum())

subset_df = df.iloc[40:75]
print(subset_df)

top_movie = df.loc[df['No_of_Votes'].idxmax()]
print(top_movie)

df['Runtime'] = df['Runtime'].astype(str).str.replace(' min', '')
df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')

plt.figure(figsize=(8,5))
sns.boxplot(data=df[['IMDB_Rating', 'Runtime']])
plt.title("Boxplot: IMDB Rating & Runtime")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df['Runtime'], df['IMDB_Rating'])
plt.xlabel("Runtime")
plt.ylabel("IMDB Rating")
plt.title("Runtime vs IMDB Rating")
plt.show()