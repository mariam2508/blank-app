import streamlit as st

st.title("Car")
Year=st.number_input('Year',min_value=0,max_value=10,value=1)
Present_Price=st.number_input('Present_Price',min_value=0,max_value=10,value=1)
output=model.predict([[Present_Price,Year]])
st.write('car is',output[0][0])


