def calculate_affordable_amount(budget):
    disposable_income = budget.monthly_income - budget.monthly_expenses
    return disposable_income - budget.savings_goal
