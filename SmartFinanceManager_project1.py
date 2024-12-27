import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class FinanceManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Personal Finance Manager")
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")

        self.expenses = []  
        self.income = []    
        self.expense_categories = ["General"]  
        self.income_categories = ["General"]   

        self.create_widgets()

    def create_widgets(self):
        
        title_label = tk.Label(self.root, text="Personal Finance Manager", font=("Arial", 20), bg="lightblue")
        title_label.pack(pady=10)

        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.add_expense_tab()
        self.add_income_tab()
        self.add_charts_tab()

    def add_expense_tab(self):
        expense_tab = ttk.Frame(self.notebook)
        self.notebook.add(expense_tab, text="Expenses")

        
        add_expense_frame = ttk.LabelFrame(expense_tab, text="Add Expense")
        add_expense_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(add_expense_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.expense_amount_var = tk.DoubleVar()
        ttk.Entry(add_expense_frame, textvariable=self.expense_amount_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_expense_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.expense_category_var = tk.StringVar()
        category_menu = ttk.OptionMenu(add_expense_frame, self.expense_category_var, *self.expense_categories)
        category_menu.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_expense_frame, text="Date:").grid(row=2, column=0, padx=5, pady=5)
        self.expense_date_var = tk.StringVar()
        ttk.Entry(add_expense_frame, textvariable=self.expense_date_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(add_expense_frame, text="Add Expense", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=10)

        
        manage_categories_frame = ttk.LabelFrame(expense_tab, text="Manage Expense Categories")
        manage_categories_frame.pack(fill="x", padx=10, pady=10)

        self.new_expense_category_var = tk.StringVar()
        ttk.Entry(manage_categories_frame, textvariable=self.new_expense_category_var).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(manage_categories_frame, text="Add Category", command=self.add_expense_category).grid(row=0, column=1, padx=5, pady=5)

    def add_income_tab(self):
        income_tab = ttk.Frame(self.notebook)
        self.notebook.add(income_tab, text="Income")

        
        add_income_frame = ttk.LabelFrame(income_tab, text="Add Income")
        add_income_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(add_income_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.income_amount_var = tk.DoubleVar()
        ttk.Entry(add_income_frame, textvariable=self.income_amount_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_income_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.income_category_var = tk.StringVar()
        category_menu = ttk.OptionMenu(add_income_frame, self.income_category_var, *self.income_categories)
        category_menu.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_income_frame, text="Date:").grid(row=2, column=0, padx=5, pady=5)
        self.income_date_var = tk.StringVar()
        ttk.Entry(add_income_frame, textvariable=self.income_date_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(add_income_frame, text="Add Income", command=self.add_income).grid(row=3, column=0, columnspan=2, pady=10)

        
        manage_categories_frame = ttk.LabelFrame(income_tab, text="Manage Income Categories")
        manage_categories_frame.pack(fill="x", padx=10, pady=10)

        self.new_income_category_var = tk.StringVar()
        ttk.Entry(manage_categories_frame, textvariable=self.new_income_category_var).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(manage_categories_frame, text="Add Category", command=self.add_income_category).grid(row=0, column=1, padx=5, pady=5)

    def add_charts_tab(self):
        charts_tab = ttk.Frame(self.notebook)
        self.notebook.add(charts_tab, text="Charts")

        ttk.Button(charts_tab, text="Show Expense Chart (Weekly)", command=lambda: self.show_chart(self.expenses, "Expenses", "weekly")).pack(pady=10)
        ttk.Button(charts_tab, text="Show Expense Chart (Monthly)", command=lambda: self.show_chart(self.expenses, "Expenses", "monthly")).pack(pady=10)
        ttk.Button(charts_tab, text="Show Income Chart (Weekly)", command=lambda: self.show_chart(self.income, "Income", "weekly")).pack(pady=10)
        ttk.Button(charts_tab, text="Show Income Chart (Monthly)", command=lambda: self.show_chart(self.income, "Income", "monthly")).pack(pady=10)

    def add_expense(self):
        try:
            amount = self.expense_amount_var.get()
            category = self.expense_category_var.get()
            date = datetime.strptime(self.expense_date_var.get(), "%d-%m-%Y")

            self.expenses.append({"amount": amount, "category": category, "date": date})
            messagebox.showinfo("Success", "Expense Added")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_income(self):
        try:
            amount = self.income_amount_var.get()
            category = self.income_category_var.get()
            date = datetime.strptime(self.income_date_var.get(), "%Y-%m-%d")

            self.income.append({"amount": amount, "category": category, "date": date})
            messagebox.showinfo("Success", "Income Added")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_expense_category(self):
        category = self.new_expense_category_var.get()
        if category and category not in self.expense_categories:
            self.expense_categories.append(category)
            messagebox.showinfo("Success", "Expense Category Added")

    def add_income_category(self):
        category = self.new_income_category_var.get()
        if category and category not in self.income_categories:
            self.income_categories.append(category)
            messagebox.showinfo("Success", "Income Category Added")

    def show_chart(self, data, title, timeframe):
        filtered_data = self.filter_data_by_timeframe(data, timeframe)
        category_totals = {}

        for entry in filtered_data:
            category_totals[entry["category"]] = category_totals.get(entry["category"], 0) + entry["amount"]

        if category_totals:
            plt.figure(figsize=(6, 6))
            plt.pie(category_totals.values(), labels=category_totals.keys(), autopct="%1.1f%%")
            plt.title(f"{title} by Category ({timeframe.capitalize()})")
            plt.show()
        else:
            messagebox.showinfo("No Data", f"No {title.lower()} data available for this {timeframe} timeframe.")

    def filter_data_by_timeframe(self, data, timeframe):
        now = datetime.now()

        if timeframe == "weekly":
            start_date = now - timedelta(days=7)
        elif timeframe == "monthly":
            start_date = now - timedelta(days=30)
        else:
            start_date = now

        return [entry for entry in data if entry["date"] >= start_date]


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceManager(root)
    root.mainloop()
