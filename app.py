import streamlit as st
import pandas as pd
import duckdb
import io

csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
Select * from beverage \n
cross join food_items
"""

solution = duckdb.sql(answer).df()

st.write("# SQL SRS \n" "Space repetition system SQL practice")

with st.sidebar:
    option = st.selectbox(
        "Choisi ton thème de révision",
        ("Jointure", "Group By", "Windows Function", "sans catégorie"),
        index=None,
        placeholder="Choisi ton thème de révision...",
    )

    st.write("Vous avez choisi: ", option)


st.header("Votre code ici:")
query = st.text_area(label="Votre code SQL ici", key="user input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)


tab1, tab2 = st.tabs(["Tables", "Solutions"])

with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("Expected")
    st.dataframe(solution)

with tab2:
    st.write(answer)
