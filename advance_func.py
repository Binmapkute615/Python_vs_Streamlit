##import the library
import streamlit as st
import numpy as np
import pandas as pd
import time

#interactive widgets
st.text("Streamlit interactive widgets")
st.button("Click the button below!")
if st.button("Say Hello"):
    st.write("Have a wonderful day!!!")
else:
    st.write("Goodbye!!! ")