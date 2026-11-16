def calculate_emi(principal, annual_rate, tenure):
    if annual_rate == 0:
        emi = principal / tenure
    else:
        r = annual_rate / 12 / 100
        emi = (principal * r * ((1 + r) ** tenure)) / (((1 + r) ** tenure) - 1)
    return round(emi, 2)

def calculate_total_payable(emi, tenure):
    return round(emi * tenure, 2)

def calculate_total_interest(total_payable, principal):
    return round(total_payable - principal, 2)

def check_eligibility(emi, monthly_income):
    max_allowed_emi = monthly_income * 0.40
    if emi <= max_allowed_emi:
        return True
    else:
        return False

principal = float(input("Principal: "))

if principal <= 0:
    print("Invalid loan amount. Enter a positive amount.")
else:
    annual_rate = float(input("Annual rate: "))
    tenure = int(input("Tenure (in months): "))

    if annual_rate < 0 or annual_rate > 30:
        print("Invalid interest rate. Enter a rate between 0 and 30.")
    elif tenure < 1 or tenure > 360:
        print("Invalid tenure. Enter tenure between 1 and 360 months.")
    else:
        monthly_income = float(input("Monthly income: "))

        if monthly_income <= 0:
            print("Invalid monthly income. Enter a positive amount.")
        else:

            emi = calculate_emi(principal, annual_rate, tenure)
            total_payable = calculate_total_payable(emi, tenure)
            total_interest = calculate_total_interest(total_payable, principal)
            is_eligible = check_eligibility(emi, monthly_income)


            if is_eligible:
                print(f"EMI: Rs. {emi:.2f} | Total Payable: Rs. {total_payable:.2f}")
                print(f"Total Interest: Rs. {total_interest:.2f} | Eligible: Yes")
            else:
                max_emi = monthly_income * 0.40
                print(f"EMI: Rs. {emi:.2f}")
                print(f"Maximum allowed EMI (40% of income): Rs. {max_emi:.2f}")
                print("Loan not eligible: EMI exceeds the allowed limit.")