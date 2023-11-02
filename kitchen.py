import streamlit as st
import pandas as pd
import json
import requests

def increment_quantity(category, item_name):
    url = "http://localhost:8001/increment_quantity"
    payload = {"category": category, "item_name": item_name}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        st.write(f"Quantité mise à jour avec succès pour {item_name}.")
    else:
        st.write(f"Erreur lors de la mise à jour de la quantité pour {item_name}.")

def decrement_quantity(category, item_name):
    url = "http://localhost:8001/decrement_quantity"
    payload = {"category": category, "item_name": item_name}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        st.write(f"Quantité mise à jour avec succès pour {item_name}.")
    else:
        st.write(f"Erreur lors de la mise à jour de la quantité pour {item_name}.")


def show_kitchen():
    st.title("Kitchen")
    st.write("List of items available in my pantry and fridge:")

    with open('data/pantry.json') as f:
        data = json.load(f)

    for category, items in data.items():
        st.subheader(category.capitalize())
        df = pd.DataFrame(items)

        col1, col2, col3 = st.columns(3)

        col1.table(df.set_index('name'))
        for index, row in df.iterrows():
            if col2.button(f"{row['name']} - ", use_container_width= True):
                decrement_quantity(category, row['name']) 
                st.write(f"You clicked the button for {row['name']}.")
            if col3.button(f"{row['name']} + ", use_container_width= True):
                increment_quantity(category, row['name'])
                st.write(f"You clicked the button for {row['name']}.")
