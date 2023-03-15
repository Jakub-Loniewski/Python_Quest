credit_amount = int(input("How much do you want to borrow? "))
credit_percentage = int(input("Enter the loan interest rate "))
credit_contribution = int(input("Enter the amount of own contribution "))
credit_time_year = int(input("Loan duration in years "))
you_income = int(input("Enter you monthly income "))
you_expenses = int(input("Sum of monthly expenses "))


installment = (credit_amount * credit_percentage /100)/12 + credit_amount /(credit_time_year *12)

available_money = you_income - you_expenses
property_value = credit_amount + credit_contribution

credit_contribution = credit_contribution / property_value
money_over_installment = available_money - installment

matching_higher_own_part = credit_contribution >= 0.2 and money_over_installment >= 1000
matching_lower_own_part = credit_contribution >= 0.1 and money_over_installment >= 2000

if matching_lower_own_part or matching_higher_own_part:
    print("Credit is available ")
else:
    print("Credit is not available")