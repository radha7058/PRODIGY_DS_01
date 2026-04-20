# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: Create Sample Dataset
# -----------------------------
data = {
    "Name": ["Aman", "Riya", "Rahul", "Sneha", "Karan", "Pooja", "Arjun", "Neha"],
    "Age": [22, 25, 23, 24, 26, 22, 27, 23],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -----------------------------
# STEP 2: Bar Chart (Gender Distribution)
# -----------------------------
gender_count = df["Gender"].value_counts()

plt.figure()
gender_count.plot(kind='bar')

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.show()

# -----------------------------
# STEP 3: Histogram (Age Distribution)
# -----------------------------
plt.figure()
plt.hist(df["Age"], bins=5)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()