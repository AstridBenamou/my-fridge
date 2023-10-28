# import streamlit as st
# import pandas as pd 
# import json

# def show_kitchen():
#     #categories = pd.read_csv("data/categories.csv")
#     st.title("Kitchen")
#     st.write("List of items available in my pantry and fridge:")

#     with open('data/categories.json') as f:
#         data = json.load(f)

#     for category, items in data.items():
#             st.subheader(category.capitalize())
#             data_table = {"Items": items, "Quantities": [0] * len(items)}
#             df = pd.DataFrame(data_table)
#             st.dataframe(df, height=300, hide_index=True)


import streamlit as st
import pandas as pd
import json
import requests

API_URL = "http://localhost:8000"  # Remplacez ceci par votre URL d'API

def show_kitchen():
    st.title("Kitchen")
    st.write("List of items available in my pantry and fridge:")

    with open('data/categories.json') as f:
        data = json.load(f)

    for category, items in data.items():
        st.subheader(category.capitalize())
        for item in items:
            quantity = st.number_input(f"Enter quantity for {item}", value=0)
            if st.button(f"Increment {item}"):
                payload = {"name": item, "quantity": 1}
                response = requests.post(f"{API_URL}/update_quantity", json=payload)
                if response.status_code == 200:
                    st.write(response.json()["message"])
                else:
                    st.write("Failed to increment quantity.")
            # if st.button(f"Decrement {item}"):
            #     payload = {"name": item, "quantity": 1}
            #     response = requests.post(f"{API_URL}/decrement_quantity", json=payload)
            #     if response.status_code == 200:
            #         st.write(response.json()["message"])
            #     else:
            #         st.write("Failed to decrement quantity.")

            # Afficher la quantité actuelle de l'élément
            st.write(f"Current quantity: {quantity}")

if __name__ == '__main__':
    show_kitchen()
