import pandas as pd
import streamlit as st
import numpy as np

st.title("DataFrame Display Example")

# ##Display and simple text

# st.write("This is a simple text display using Streamlit.")

# # Display a DataFrame
# df = pd.DataFrame({
#     "first row": [1,2,3],
#     "second row":[4,5,6]
#     })
# st.write(df)

dataset = pd.DataFrame(np.random.randn(20,3), columns=['first','second', 'third'])
st.write(dataset)
st.line_chart(dataset)