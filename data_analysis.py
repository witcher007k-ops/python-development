import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")
print(df.head())
print(df.describe())
selected_column = df.columns[1]
print("Average of", selected_column, "=", df[selected_column].mean())

plt.figure()
df[selected_column].value_counts().plot(kind="bar")
plt.title("Bar Chart")
plt.show()

plt.figure()
plt.scatter(df[df.columns[0]], df[selected_column])
plt.title("Scatter Plot")
plt.show()

plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Heatmap of Correlation")
plt.show()
