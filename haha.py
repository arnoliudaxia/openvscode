import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.title('title')
st.header('st.write')

code="""
print(f"x+1")

"""

st.code(code, language='python')

st.latex("""x+x_1+x_2""")

st.caption("I'm caption")