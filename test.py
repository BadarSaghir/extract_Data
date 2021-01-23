# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("data.csv")

# generating one row
row1 = data.sample(n=150)

# display
print(type(row1))
print(row1)
row1.to_csv(r"sample.csv", index=False)

# generating another row
