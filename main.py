import streamlit as st 

# Func
def distance_converter(from_unit,to_unit,value):
    units ={
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def temperature_converter(from_unit,to_unit,value):
    if from_unit == "Celsius" and to_unit == "Farhenhiet":
        result = (value * 9/5) + 32 
    elif from_unit == "Farhenhiet" and to_unit == "Celsius":
          result  = (value - 32) * 5/9
    else:
        result(value)
    return result 

def weight_converter(from_unit,to_unit,value):
    units ={
         "Kilograms": 1 ,
         "Grams":0.001,
         "Pounds":0.453592,
         "Ounces":0.0283495
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def pressure_converter(from_unit,to_unit,value):
    units ={
         "Pascals": 1 ,
         "Hectopascals":100,
         "Kilopascals":1000,
         "Bar":100000
    }
    result = value * units[from_unit] / units[to_unit]
    return result

st.title("Unit Converter")


Category =st.selectbox("Select Category",["Distance","Temperature","Weight","Pressure"])

if Category == "Distance":
    from_unit = st.selectbox("From",["Meters","Kilometers","Feet","Miles"])
    to_unit = st.selectbox("To",["Meters","Kilometers","Feet","Miles"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
       result = distance_converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result: .2f} {to_unit}")

elif Category == "Temperature":
    from_unit = st.selectbox("From",["Celsius", "Fahrenhiet"])
    to_unit = st.selectbox("To",["Celsius", "Fahrenhiet"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
       result = temperature_converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result: .2f} {to_unit}")

elif Category == "weight":
    from_unit = st.selectbox("From",["Kilograms", "Grams","Pounds","Ounces"])
    to_unit = st.selectbox("To",["Kilograms", "Grams","Pounds","Ounces"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
      result = weight_converter(from_unit,to_unit,value)
      st.success(f"{value} {from_unit} = {result: .2f} {to_unit}")

elif Category == "Pressure":
    from_unit = st.selectbox("From",["Pascals", "Hectopascals","Kilopascals","Bar"])
    to_unit = st.selectbox("To",["Pascals", "Hectopascals","Kilopascals","Bar"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
      result = pressure_converter(from_unit,to_unit,value)
      st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")