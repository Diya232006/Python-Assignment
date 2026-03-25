import matplotlib.pyplot as plt

# Data
companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS', 'Amdocs']
recruits = [500, 450, 600, 350, 400, 300, 200, 250]

# a) Bar Chart
plt.bar(companies, recruits, color='skyblue')
plt.title("New Recruitments by Company")
plt.xticks(rotation=45) # Rotates company names for better view
plt.show()

# b) & c) Customized Pie Chart
# 'explode' pulls out a slice, 'autopct' shows percentage
explode = [0.1, 0, 0, 0, 0, 0, 0, 0] 
plt.pie(recruits, labels=companies, autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Recruitment Distribution")
plt.show()

# d) Doughnut Chart (Pie chart with a white circle in the middle)
plt.pie(recruits, labels=companies, autopct='%1.1f%%')
circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(circle)
plt.title("Doughnut Chart: Recruitment")
plt.show()

# Compare IBM & Amdocs
names = ['IBM', 'Amdocs']
values = [350, 250] # Taken from the list above
plt.bar(names, values, color=['blue', 'green'])
plt.title("Comparison: IBM vs Amdocs")
plt.show()
