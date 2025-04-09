import streamlit as st
import pandas as pd
import duckdb

st.write("# SQL SRS \n" "Space repetition system SQL practice")

option = st.selectbox(
    "Choisi ton thème de révision",
    ("Jointure", "Group By", "Windows Function", "sans catégorie"),
    index=None,
    placeholder="Choisi ton thème de révision...",
)

st.write("Vous avez choisi: ", option)

data = {"col1": ["chien", "chat", "loup"], "col2": [2, 3, 5]}
df = pd.DataFrame(data)

tab1, tab2 = st.tabs(["dataframe", "sql"])

with tab1:
    input_text = st.text_area("Text input")
    st.write(input_text)

with tab2:
    input_column = st.text_area("Colonne SQL à requêter")
    if input_column in df.columns:
        query = f"""
                SELECT * FROM df WHERE {input_column} > 2
                """
        df_tmp = duckdb.query(query).df()
        st.dataframe(df_tmp)
    else:
        st.write("La colonne spécifiée n'existe pas dans le DataFrame.")
