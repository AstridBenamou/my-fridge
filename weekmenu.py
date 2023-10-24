import streamlit as st
import pandas as pd
import numpy as np

def get_menu(data_recipes): 

    #breakfast = pd.read_csv('recettes_petit_dejeuner.csv')
    meals = pd.read_csv(data_recipes)

    l_main_course = meals['Meal']
    #l_breakfast = breakfast['Nom']
    #rb = np.random.randint(low = 0,high=len(l_breakfast),size=7)
    rl = np.random.randint(low = 0,high=len(l_main_course),size=7)
    rd = np.random.randint(low = 0,high=len(l_main_course),size=7)

    DAYS = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    data = {DAYS[i]:[#l_breakfast[rb[i]], 
                    l_main_course[rl[i]],  
                    l_main_course[rd[i]]] 
                    for i in range(len(DAYS))}

    menu = pd.DataFrame(data, index=[#'Breakfast', 
                                'Lunch', 
                                'Diner']) 
    grocery_list = []
    #ingredients_list = breakfast.iloc[rb, 3].values #3 is the index of the ingredient list 
    #grocery_list.extend(ingredients_list)

    ingredients_list2 = meals.iloc[rl,1].values
    grocery_list.extend(ingredients_list2)

    ingredients_list3 = meals.iloc[rd, 1].values
    grocery_list.extend(ingredients_list3)

    ingredients_list = [ingredients.split(', ') for ingredients in grocery_list]
    ingredients = [item for sublist in ingredients_list for item in sublist]

    return(menu, ingredients)


def show_menu(menu):
    st.title('My menu for the week')
    st.write(menu)

def get_groceries(ingredients_list, categories_data_file):
    df_categories = pd.read_csv(categories_data_file)
    # Creating a dictionary with ingredient counts
    ingredient_count = {}
    for ingredient in ingredients_list:
        if ingredient in ingredient_count:
            ingredient_count[ingredient] += 1
        else:
            ingredient_count[ingredient] = 1

    df_ingredient_count = pd.DataFrame.from_dict(ingredient_count, orient='index', columns=['Ingredients'])
    final_groceries = df_ingredient_count.merge(df_categories.set_index(['Ingredients']), right_index=True, left_index=True)
    final_groceries.sort_values('Category', inplace=True)

    grouped_groceries = final_groceries.groupby('Category')
    return(grouped_groceries)

   
def show_groceries(grouped_groceries):
    # Create a Streamlit app
    st.title('My grocery list:')

    # Iterate through each group and display as tables
    for category, group in grouped_groceries:
        st.write(category.capitalize())
        group_without_category = group.drop('Category', axis=1)  # Drop the 'category' column
        st.write(group_without_category)
