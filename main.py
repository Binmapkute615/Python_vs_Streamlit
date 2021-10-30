import streamlit as st


## simple hello world!!!
st.write ("Howdy World! My Name is Curt\n")

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
