import pandas as pd

df = pd.read_csv(r"C:\Users\mohammed faraz\OneDrive\Desktop\maintenance.csv")

average = df["Flight_Hours"].mean()

highest = df["Flight_Hours"].max()

lowest = df["Flight_Hours"].min()

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
