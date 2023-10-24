import streamlit as st
import pandas as pd 
import json

def show_kitchen():
    #categories = pd.read_csv("data/categories.csv")
    st.title("Kitchen")
    st.write("List of items available in my pantry and fridge:")

    with open('data/categories.json') as f:
        data = json.load(f)

    for category, items in data.items():
            st.subheader(category.capitalize())
            data_table = {"Items": items, "Quantities": [0] * len(items)}
            df = pd.DataFrame(data_table)
            st.dataframe(df, height=300, hide_index=True)