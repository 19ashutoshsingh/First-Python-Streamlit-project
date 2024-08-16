import streamlit as st
import pandas

data = {
    'Series_1': [1, 15, 10, 5, 20],
    'Series_2': [10, 60, 30, 70, 50]
}

df = pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything With Python')
st.write('''This is our first Web App.
Enjoy it!
''')

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, myslider * 9/5 + 32)
