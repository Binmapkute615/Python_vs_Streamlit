import streamlit as st


## simple hello world!!!
st.write ("Howdy World! \n My Name is Curt\n")

import random
import pandas as pd

## explore_widgets 
#Display a Text
st.title ("Demo streamlit widgets\n")
st.header ("Display Python variables\n")

my_var = 10
st.write(my_var)

#Dictionary of data
data ={"first_name": "Curt", "last_name":"Hnirt"}
st.write(data)

#A list of 10 random integers between o and 10
num = [random.randint(0, 10) for i in range(10)]
st.table(num)

st.bar_chart(num)
st._arrow_bar_chart(num)

st.line_chart(num)
st.area_chart(num)

# A dictionary of random x and y coordinates for a time plot
num1 = {"x": [1, 2, 3, 4, 5], "y": [1, 4, 9, 16, 25]}
st.line_chart(num1)
st.area_chart(num1)

image_url ="https://cybersecurity.umbc.edu/files/2019/11/Campus-airial-Picture1.png"
st.image(image_url)

# lat and long of UM baltimore county in a dictionary
data2 = {"lat": 39.2557, "lon": -76.7110}
df = pd.DataFrame([data2])
st.map(df)

## Math_app
# https://docs.streamlit.io/library/api-reference/widgets

X = st.number_input("X", step=1)
Y = st.select_slider("Y", range(0, 10))

show_balloons = st.checkbox("Show balloons?")
if st.button("Add"):
    st.write(f" Your Sum is {X + Y}")
if st.button ("Mul"):
    st.write(f" Your Multiply is {X * Y}")
if st.button ("Div"):
    st.write(f" Your Divide is {X % Y}")
    if show_balloons:
        st.balloons()

## 4 API request
import requests
# API URL
URL = "https://api.agify.io"

name = st.text_input("Enter your name: ")

# input params
PARAM = {"name":name}

# Get the result from the API
res = requests.get(url=URL, params=PARAM)
data = res.json()

if st.button("Calculate Age"):
    st.write(f"{data['name']} is {data['age']} years old.")
