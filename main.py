import pandas as pd
import matplotlib.pyplot as plt
import os


if not os.path.exists("output"):
    os.makedirs("output")

file_path = "data/tracker.xlsx"
df = pd.read_excel(file_path)


print("\n📌 Data Preview:")
print(df.head())



total_expense = df["Amount"].sum()
print("\n💰 Total Expense:", total_expense)

total_hours = df["Hours"].sum()
print("⏱️ Total Hours:", total_hours)

category_expense = df.groupby("Category")["Amount"].sum()


category_hours = df.groupby("Category")["Hours"].sum()

print("\n📊 Expense by Category:\n", category_expense)
print("\n📊 Hours by Category:\n", category_hours)


plt.figure()
category_expense.plot(kind="pie", autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.ylabel("")
plt.savefig("output/expense_pie.png")


plt.figure()
category_hours.plot(kind="bar")
plt.title("Hours Spent per Category")
plt.xlabel("Category")
plt.ylabel("Hours")
plt.savefig("output/hours_bar.png")



summary = pd.DataFrame({
    "Category": category_expense.index,
    "Total Expense": category_expense.values,
    "Total Hours": category_hours.values
})

summary.to_excel("output/summary.xlsx", index=False)

print("\n✅ Charts saved in 'output/' folder")
print("✅ Summary file created: summary.xlsx")



max_expense_category = category_expense.idxmax()
max_hours_category = category_hours.idxmax()

print("\n🔍 Insights:")
print(f"📌 Highest spending category: {max_expense_category}")
print(f"📌 Most time spent on: {max_hours_category}")
