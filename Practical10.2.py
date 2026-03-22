import pandas as pd

# Creating the data for 5 states
data = {
    'State': ['Maharashtra', 'Rajasthan', 'Goa', 'UP', 'Gujarat'],
    'Area': [307713, 342239, 3702, 240928, 196024],
    'Population': [112374333, 68548437, 1458545, 199812341, 60439692]
}

df = pd.DataFrame(data)

# a) Print complete information
print("\n--- State Information ---")
print(df)

# b) State with largest Area
max_area_state = df.loc[df['Area'].idxmax(), 'State']
print(f"\nState with Largest Area: {max_area_state}")

# c) State with largest Population
max_pop_state = df.loc[df['Population'].idxmax(), 'State']
print(f"State with Largest Population: {max_pop_state}")

# d) Calculate Population Density (Population / Area)
df['Density'] = df['Population'] / df['Area']
print("\n--- Table with Population Density ---")
print(df)

# e) State with highest Population Density
high_density_state = df.loc[df['Density'].idxmax(), 'State']
print(f"\nState with Highest Population Density: {high_density_state}")
