import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv", sep="\t")

sns.barplot(x="Species", y="SepalLengthCm", data=data)
plt.show()

sns.countplot(x="Species", data=data)
plt.show()

sns.boxplot(x="Species", y="SepalWidthCm", data=data)
plt.show()

sns.displot(data["SepalWidthCm"], kde=True)

sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=data)

sns.pairplot(data, hue="Species")