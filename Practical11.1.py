import matplotlib.pyplot as plt
import pandas as pd

# Creating sample data (You can replace this with pd.read_csv("sales.csv"))
data = {
    'month': [1, 2, 3, 4, 5, 6],
    'face_cream': [2500, 2630, 2140, 3400, 3600, 2760],
    'face_wash': [1500, 1200, 1340, 1130, 1740, 1555],
    'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890],
    'total_profit': [211000, 183300, 224700, 222700, 209600, 201400]
}
df = pd.DataFrame(data)

# a) Line Plot for Total Profit
plt.figure(figsize=(6,4))
plt.plot(df['month'], df['total_profit'], marker='o', color='red')
plt.title("Total Profit per Month")
plt.show()

# b) Multiline Plot for all products
plt.plot(df['month'], df['face_cream'], label='Face Cream')
plt.plot(df['month'], df['face_wash'], label='Face Wash')
plt.plot(df['month'], df['toothpaste'], label='Toothpaste')
plt.legend()
plt.title("All Product Sales")
plt.show()

# c) Bar Chart for Face Cream and Face Wash
plt.bar(df['month'] - 0.2, df['face_cream'], width=0.4, label='Face Cream')
plt.bar(df['month'] + 0.2, df['face_wash'], width=0.4, label='Face Wash')
plt.legend()
plt.title("Face Cream vs Face Wash Sales")
plt.show()

# d) Pie Chart for Total Sales of each product
total_sales = [df['face_cream'].sum(), df['face_wash'].sum(), df['toothpaste'].sum()]
labels = ['Face Cream', 'Face Wash', 'Toothpaste']
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales Share")
plt.show()
