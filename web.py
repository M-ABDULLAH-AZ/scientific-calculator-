import streamlit as st
import math


st.title("Scientific Calculator")

st.header("This ia a scientific calculator by AZ_DEVELOPERS.")

num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number (if needed)", value=0.0, key='num2')
operation = st.selectbox("Choose an operation", [
    "Add", "Subtract", "Multiply", "Divide", "Power", "Square Root",
    "Sin", "Cos", "Tan", "Log (Base 10)", "Log (Base e)",
    "Anti Log (Base 10)", "Anti Log (Base e)"
])


if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    elif operation == "Power":
        result = num1 ** num2
    elif operation == "Square Root":
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            result = "Error! Square root of a negative number."
    elif operation == "Sin":
        result = math.sin(math.radians(num1))
    elif operation == "Cos":
        result = math.cos(math.radians(num1))
    elif operation == "Tan":
        result = math.tan(math.radians(num1))
    elif operation == "Log (Base 10)":
        if num1 > 0:
            result = math.log10(num1)
        else:
            result = "Error! Logarithm of a non-positive number."
    elif operation == "Log (Base e)":
        if num1 > 0:
            result = math.log(num1)
        else:
            result = "Error! Logarithm of a non-positive number."
    elif operation == "Anti Log (Base 10)":
        result = 10 ** num1
    elif operation == "Anti Log (Base e)":
        result = math.exp(num1)
    else:
        result = "Invalid Operation"


    st.write("Result:", result)


























