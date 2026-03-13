# def add(*args):
#     total = sum(args)
#     print(total)
# add(1,2,3,4,5,6,7,8,9,10)

#===========================
#
# from keyword import kwlist
# print(kwlist)

#
# from anac import api
#
# a = api(
#     "https://demo.netbox.dev",
#     token="cf1dc7b04de5f27cfc93aba9e3f537d2ad6fdf8c",
# )
# # get openapi spec and create attributes/endpoints
# print(a.openapi())


import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Year': [2020, 2021, 2022, 2023, 2024],
    'Sales': [25000, 27000, 30000, 32000, 35000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print basic stats
print("Sales Summary:")
print(df.describe())

# Plot the data
plt.figure(figsize=(8, 5))
plt.plot(df['Year'], df['Sales'], marker='o', linestyle='-', color='green')
plt.title("Yearly Sales")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
