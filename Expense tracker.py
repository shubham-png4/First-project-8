from datetime import datetime

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")
    
    def __str__(self):
        return f"💰 ${self.amount} | {self.category} | {self.description} | {self.date}"

class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit
        self.expenses = []
    
    def add_expense(self, amount):
        self.expenses.append(amount)
    
    def total_expenses(self):
        return sum(self.expenses)
    
    def remaining(self):
        return self.limit - self.total_expenses
    
    def is_over_budget(self):
        return self.total_expenses() > self.limit

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budgets = {}
    
    def add_expense(self):
        print("\n➕ ADD EXPENSE")
        try:
            amount = float(input("Amount: $"))
            category = input("Category (Food/Transport/Shopping/Entertainment/Other): ").strip()
            description = input("Description: ").strip()
            
            expense = Expense(amount, category, description)
            self.expenses.append(expense)
            
            # Add to budget
            if category not in self.budgets:
                budget_limit = float(input(f"Set budget for {category}: $"))
                self.budgets[category] = Budget(category, budget_limit)
            
            self.budgets[category].add_expense(amount)
            print(f"✅ Expense added!")
        except ValueError:
            print("❌ Invalid amount!")
    
    def view_expenses(self):
        if not self.expenses:
            print("📭 No expenses yet!")
            return
        
        print("\n📊 ALL EXPENSES")
        print("=" * 60)
        for expense in self.expenses:
            print(expense)
        print("=" * 60)
        print(f"Total: ${sum(e.amount for e in self.expenses)}")
    
    def view_budgets(self):
        if not self.budgets:
            print("📭 No budgets set!")
            return
        
        print("\n💵 BUDGET STATUS")
        print("=" * 60)
        for budget in self.budgets.values():
            status = "⚠️  OVER BUDGET" if budget.is_over_budget() else "✅ OK"
            print(f"{budget.category}:")
            print(f"  Budget: ${budget.limit}")
            print(f"  Used: ${budget.total_expenses()}")
            print(f"  Remaining: ${budget.remaining()}")
            print(f"  Status: {status}")
            print()
        print("=" * 60)
    
    def get_category_summary(self):
        if not self.expenses:
            print("📭 No expenses yet!")
            return
        
        print("\n📊 CATEGORY BREAKDOWN")
        print("=" * 60)
        
        categories = {}
        for expense in self.expenses:
            cat = expense.category
            categories[cat] = categories.get(cat, 0) + expense.amount
        
        for cat, total in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            percentage = total / sum(categories.values()) * 100
            print(f"{cat}: ${total:.2f} ({percentage:.1f}%)")
        
        print("=" * 60)
        print(f"Total: ${sum(categories.values()):.2f}")
    
    def menu(self):
        while True:
            print("\n" + "=" * 60)
            print("💰 EXPENSE TRACKER")
            print("=" * 60)
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. View Budgets")
            print("4. Category Summary")
            print("5. Exit")
            print("=" * 60)
            
            choice = input("Choose: ").strip()
            
            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.view_budgets()
            elif choice == "4":
                self.get_category_summary()
            elif choice == "5":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice!")

# Run the tracker
tracker = ExpenseTracker()
tracker.menu()