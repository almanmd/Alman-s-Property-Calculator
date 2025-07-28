import streamlit as st
import math

# Title
st.title("Alman's Property Investment Calculator")

# User Inputs
property_price = st.number_input("Enter the property price (SGD): ", min_value=0.0, step=1000.0)
downpayment_percentage = 25.0  # 25% downpayment
loan_duration_years = st.slider("Loan duration (years, up to 25 years or until age 65): ", min_value=1, max_value=25, value=25)
investor_age = st.slider("Investor's age: ", min_value=18, max_value=65, value=30)
rental_income_monthly = st.number_input("Expected monthly rental income (SGD): ", min_value=0.0, step=100.0)

# Constants and Calculations
interest_rate_annual = 0.022  # 2.2% annual interest rate
downpayment = property_price * (downpayment_percentage / 100)
loan_amount = property_price - downpayment
monthly_interest_rate = interest_rate_annual / 12
number_of_payments = loan_duration_years * 12

# Check for non-zero input values
if property_price > 0 and loan_amount > 0:
    # Monthly mortgage payment calculation using the formula for an amortizing loan
    monthly_payment = loan_amount * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, number_of_payments)) / (math.pow(1 + monthly_interest_rate, number_of_payments) - 1)
    
    # Rental Yield Calculation
    annual_rental_income = rental_income_monthly * 12
    rental_yield = (annual_rental_income / property_price) * 100

    # Capital Appreciation Calculation
    if loan_duration_years < 10:
        appreciation_rate = 0.06  # 6% for properties less than 10 years old
    else:
        appreciation_rate = 0.035  # 3.5% for holding periods over 15 years

    capital_appreciation = property_price * math.pow(1 + appreciation_rate, loan_duration_years) - property_price

    # Output Results
    st.write("## Investment Summary")
    st.write(f"**Downpayment:** SGD {downpayment:,.2f}")
    st.write(f"**Loan Amount:** SGD {loan_amount:,.2f}")
    st.write(f"**Monthly Mortgage Payment:** SGD {monthly_payment:,.2f}")
    st.write(f"**Annual Rental Income:** SGD {annual_rental_income:,.2f}")
    st.write(f"**Rental Yield:** {rental_yield:.2f}%")
    st.write(f"**Capital Appreciation after {loan_duration_years} years:** SGD {capital_appreciation:,.2f}")
else:
    st.write("Please enter a valid property price and loan amount greater than zero.")
