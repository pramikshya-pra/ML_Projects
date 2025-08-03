
import streamlit as st

st.title(" BMI Calculation")

weight = 65
height = 5.6

bmi= round(weight/((height/3.28)**2),2)

st.write(f"weitht:{weight}kg")

st.write(f"height:{height}ft")

st.write(f"***BMI:{bmi}**")

st.subheader("Calculation of BMI")

if bmi < 16:
    st.error("Extermly Underweight")
elif 16 <= bmi <18.5 :
    st.warning("You are underweight")
elif 18.5 <= 25 :
    st.success("Healthy person you are.")
elif 25 <= 30: 
    st.info("You are overweight, it is harmful for you.")
else:
    st.error("Extermly Overweight. You need to consult with doctor and follow instructions.")