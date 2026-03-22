import pandas as pd

# Load the data
df = pd.read_csv("books.csv")

# a) Print complete report
print("\n--- Complete Book Report ---")
print(df)

# b) Print list by a given author
auth = input("\nEnter Author Name: ")
print(df[df['author'] == auth])

# c) Print list by a given publishing house
pub = input("\nEnter Publishing House: ")
print(df[df['publisher'] == pub])

# d) Titles of cheapest & costliest books
cheapest = df.loc[df['price'].idxmin(), 'title']
costliest = df.loc[df['price'].idxmax(), 'title']
print(f"\nCheapest Book: {cheapest}")
print(f"Costliest Book: {costliest}")

# e) Sort by year of publication
print("\n--- Books Sorted by Year ---")
print(df.sort_values(by='year'))
