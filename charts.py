import pandas as pd
import matplotlib.pyplot as plt


# Load employee data
df = pd.read_csv("employees.csv")


# MAIN TASK


# 1. BAR CHART - Average Salary per Department

avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

bars = plt.bar(
    avg_salary.index,
    avg_salary.values,
    color="skyblue"
)

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Display values on bars
plt.bar_label(bars, fmt="%.2f")

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()


# 2. HISTOGRAM - Salary Distribution

plt.figure(figsize=(8, 5))

plt.hist(
    df["salary"],
    bins=5,
    color="orange",
    edgecolor="black"
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("histogram.png")
plt.close()


# 3. SCATTER PLOT - ID vs Salary
# Coloured by Department

plt.figure(figsize=(8, 5))

for department in df["department"].unique():

    department_data = df[df["department"] == department]

    plt.scatter(
        department_data["id"],
        department_data["salary"],
        label=department
    )

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()


# 4. LINE CHART - Monthly Sales

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    marker="o",
    color="green",
    label="Monthly Sales"
)

plt.title("Monthly Sales (Jan - Jun)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()


print("Main Task: All 4 charts saved successfully!")


# BONUS TASK
# MATPLOTLIB SUBPLOTS - 2x2 DASHBOARD


# Create 2 rows and 2 columns
fig, axes = plt.subplots(2, 2, figsize=(12, 8))


# 1. BAR CHART - Average Salary per Department

avg_salary = df.groupby("department")["salary"].mean()

axes[0, 0].bar(
    avg_salary.index,
    avg_salary.values,
    color="skyblue"
)

axes[0, 0].set_title("Average Salary per Department")
axes[0, 0].set_xlabel("Department")
axes[0, 0].set_ylabel("Average Salary")


# 2. LINE CHART - Employee Salary by ID

axes[0, 1].plot(
    df["id"],
    df["salary"],
    marker="o",
    color="green"
)

axes[0, 1].set_title("Salary Trend by Employee ID")
axes[0, 1].set_xlabel("Employee ID")
axes[0, 1].set_ylabel("Salary")


# 3. HISTOGRAM - Salary Distribution

axes[1, 0].hist(
    df["salary"],
    bins=5,
    color="orange",
    edgecolor="black"
)

axes[1, 0].set_title("Salary Distribution")
axes[1, 0].set_xlabel("Salary")
axes[1, 0].set_ylabel("Frequency")


# 4. PIE CHART - Department Distribution

dept_count = df["department"].value_counts()

axes[1, 1].pie(
    dept_count,
    labels=dept_count.index,
    autopct="%1.1f%%",
    startangle=90
)

axes[1, 1].set_title("Department Distribution")


plt.tight_layout()


# Save bonus dashboard as PNG
plt.savefig("bonus_dashboard.png", dpi=300)


# Display all bonus charts together
plt.show()


print("Bonus Task: Dashboard saved successfully!")

print("Main Task and Bonus Task Completed!")
