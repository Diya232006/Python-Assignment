import pandas as pd

# Creating the Dataframe from the image data
data = {
    'carat': [0.23, 0.21, 0.23, 0.29, 0.31],
    'cut': ['Ideal', 'Premium', 'Good', 'Premium', 'Good'],
    'price': [326, 326, 327, 334, 335],
    'x': [3.95, 3.89, 4.05, 4.20, 4.34],
    'y': [3.98, 3.84, 4.07, 4.23, 4.35],
    'z': [2.43, 2.31, 2.31, 2.63, 2.75]
}
df = pd.DataFrame(data)

# i) Mean price for each cut
print("--- Mean Price per Cut ---")
print(df.groupby('cut')['price'].mean())

# ii) Count, Min, and Max price for each cut
print("\n--- Price Stats (Count, Min, Max) per Cut ---")
print(df.groupby('cut')['price'].agg(['count', 'min', 'max']))

# iii) Average value of x, y, and z separately
print("\n--- Average of x, y, and z ---")
print("Avg x:", df['x'].mean())
print("Avg y:", df['y'].mean())
print("Avg z:", df['z'].mean())
