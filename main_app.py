import streamlit as st
from weekmenu import get_menu, show_menu, get_groceries, show_groceries
#from kitchen import show_kitchen
def main():
    st.title("My fridge")
    menu, ingredients = get_menu('data/vegetarian_recipes.csv')
    grocery_list = get_groceries(ingredients,'data/categories.csv')

    pages = {
        "Menu": show_menu,
        "Grocery list": show_groceries,
        #"Kitchen":show_kitchen
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    if selection == 'Menu':
        pages['Menu'](menu)
    elif selection == 'Grocery list':
        pages['Grocery list'](grocery_list)
    #elif selection == "Kitchen":
        #pages['Kitchen']()

if __name__ == '__main__':
    main()