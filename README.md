# Bank Loan Calculator

A simple and robust Python 3 console application designed to calculate monthly EMIs, total payable amounts, total interest, and loan eligibility based on user income. 

This project was built as part of the Rungta International Skills University - School of Computer Science and Engineering curriculum (Project PS No. 72: Bank Loan Calculator).

---

## Features

- **Modular Design:** Uses separate Python functions for EMI computation, total payable calculation, interest calculation, and eligibility checks.
- **Zero-Interest Protection:** Safely handles cases where the annual interest rate is $0\%$ without triggering a division-by-zero error.
- **Input Validation:** Validates inputs for loan amounts, interest rates, tenures, and monthly incomes to prevent runtime crashes.
- **Precise Formatting:** Displays financial figures rounded to two decimal places matching standard financial conventions.

---

## Prerequisites

- **Python 3.x** installed on your system.

---

## How to Run

1. Clone or download the repository to your local machine.
2. Open your terminal or command prompt in the project directory.
3. Run the script using the following command:
   ```bash
   python bank_loan_calculator.py
   ```

---

## Project Structure

- `bank_loan_calculator.py`: The single-file source code containing all calculation functions, input validations, and console I/O.
- `README.md`: Documentation file explaining the project setup and test cases.

---

## Test Cases Verified

| Test Case | Input Values | Expected Output | Status |
| :--- | :--- | :--- | :--- |
| **1. Normal Input** | Principal: `500000`<br>Annual Rate: `10`<br>Tenure: `60`<br>Monthly Income: `50000` | EMI: Rs. 10623.52 \| Total Payable: Rs. 637411.20<br>Total Interest: Rs. 137411.20 \| Eligible: Yes | Passed |
| **2. Boundary / Minimum Input** | Principal: `120000`<br>Annual Rate: `0`<br>Tenure: `12`<br>Monthly Income: `30000` | EMI: Rs. 10000.00 \| Total Payable: Rs. 120000.00<br>Total Interest: Rs. 0.00 \| Eligible: Yes | Passed |
| **3. Invalid Input** | Principal: `-50000`<br>Annual Rate: `9`<br>Tenure: `24` | Invalid loan amount. Enter a positive amount. | Passed |
| **4. Different Valid Scenario** | Principal: `1000000`<br>Annual Rate: `9`<br>Tenure: `120`<br>Monthly Income: `20000` | EMI: Rs. 12667.58<br>Maximum allowed EMI (40% of income): Rs. 8000.00<br>Loan not eligible: EMI exceeds the allowed limit. | Passed |
