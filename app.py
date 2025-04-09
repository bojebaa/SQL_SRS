import streamlit as st
import pandas as pd
import duckdb

st.write("hello world")
data = {"col1": ["chien", "chat", "loup"], "col2": [2, 3, 5]}
df = pd.DataFrame(data)

tab1, tab2 = st.tabs(["dataframe", "sql"])

with tab1:
    input = st.text_area("Text input")
    st.write(input)

with tab2:
    input = st.text_area("Colonne sql a requeter")
    query = f"""
            Select * from df where {input} > 2
            """
    df_tmp = duckdb.query(query).df()
    st.dataframe(df_tmp)
