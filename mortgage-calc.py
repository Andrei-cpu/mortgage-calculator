import numpy as np

sales_price = float(input('Enter the price of the house in US dollars: '))
down_payment = float(input('How much can you pay considering the price of the house? Enter in percentage: '))
loan_amount = sales_price * (1 - down_payment / 100)
500
mortgage_type = float(input('How many years for the mortgage: '))
loan_term = int(12 * mortgage_type)
interest_rate = float(input('Enter loan interest rate as a percentage: '))
R = 1 + (interest_rate) / (12 * 100)
X = loan_amount * (R ** loan_term) * (1 - R) / (1 - R ** loan_term)

monthly_interest = []
monthly_balance = []

for i in range(1, loan_term + 1):
    interest = loan_amount * (R - 1)
    loan_amount = loan_amount - (X - interest_rate)
    monthly_interest = np.append(monthly_interest, interest)
    monthly_balance = np.append(monthly_balance, loan_amount)

print("The Home Sales Price is: = " + str('$')+ str(sales_price))
print("The Down Payment as a Percentage of Sales Price is: = " + str(down_payment)+str(' %'))
print("The Loan Amount is: = " + str(sales_price*(1-down_payment/100))+str(' %'))
print("The Interest Rate on Annual Percentage Basis is: = " + str(interest_rate)+str(' %'))
print("The duration of this loan, that is the Loan Term (in months) is: = " + str(loan_term)+str(' months'))
print("Monthly Payment for this Mortgage(P & I) is: = " + str('$')+str(np.round(X,2)))
print("Total interest paid over life cycle of the loan is: = " + str('$') + str(np.round(np.sum(monthly_interest),2)))

