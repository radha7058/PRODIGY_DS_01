import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data.csv")

# Bar chart (Gender)
sns.countplot(x="Gender", data=df)
plt.title("Gender Distribution")
plt.savefig("gender_chart.png")
plt.show()

# Histogram (Age)
plt.hist(df["Age"], bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("age_chart.png")
plt.show()