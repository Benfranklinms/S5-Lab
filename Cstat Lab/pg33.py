import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")

plt.figure(figsize=(8,5))
plt.plot(df['month_number'], df['total_profit'], label="Total Profit")
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.plot(df['month_number'], df['total_profit'], color='red', linestyle='--', marker='o', linewidth=3, label="Profit")
plt.title("Styled Profit Line Plot")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
for col in df.columns[1:-1]:
    plt.plot(df['month_number'], df[col], label=col)
plt.title("Monthly Sales Data of Products")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df['month_number'], df['toothpaste'], color='green', marker='o')
plt.title("Toothpaste Sales per Month")
plt.xlabel("Month")
plt.ylabel("Toothpaste Units")
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df['month_number']-0.2, df['facecream'], width=0.4, label="Face Cream")
plt.bar(df['month_number']+0.2, df['facewash'], width=0.4, label="Face Wash")
plt.title("Face Cream & Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df['month_number'], df['bathingsoap'], color='blue')
plt.title("Bathing Soap Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("bathingsoap_sales.png")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df['total_profit'], bins=5, color='purple', edgecolor='black')
plt.title("Profit Ranges Histogram")
plt.xlabel("Profit Range")
plt.ylabel("Frequency")
plt.show()

product_totals = df.drop(columns=['month_number','total_profit']).sum()
plt.figure(figsize=(8,8))
plt.pie(product_totals, labels=product_totals.index, autopct='%1.1f%%')
plt.title("Total Sales of Each Product (Yearly)")
plt.show()

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(df['month_number'], df['bathingsoap'], marker='o', color='blue')
plt.title("Bathing Soap Sales")
plt.subplot(1,2,2)
plt.plot(df['month_number'], df['facewash'], marker='o', color='orange')
plt.title("Face Wash Sales")
plt.show()

plt.figure(figsize=(10,6))
plt.stackplot(df['month_number'],
              df['facecream'], df['facewash'], df['toothpaste'],
              df['bathingsoap'], df['shampoo'], df['moisturizer'],
              labels=['Face Cream','Face Wash','Toothpaste','Bathing Soap','Shampoo','Moisturizer'])
plt.title("All Product Sales (Stack Plot)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend(loc='upper left')
plt.show()
