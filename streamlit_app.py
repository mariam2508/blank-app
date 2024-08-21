import streamlit as st

st.title("Car")
Year=st.number_input('Year',min_value=0,max_value=10,value=1)
Present_Price=st.number_input('Present_Price',min_value=0,max_value=10,value=1)
output = model.predict([[Year, Present_Price]])
st.write('Car is', output[0])


