import streamlit as st
import pandas as pd
import numpy as np
# Title of the app
st.title('My menu for the week')

meals = pd.read_csv('data/vegetarian_recipes.csv')
#breakfast = pd.read_csv('recettes_petit_dejeuner.csv')

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

df = pd.DataFrame(data, index=[#'Breakfast', 
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
flat_list = [item for sublist in ingredients_list for item in sublist]

# Creating a dictionary with ingredient counts
ingredient_count = {}
for ingredient in flat_list:
    if ingredient in ingredient_count:
        ingredient_count[ingredient] += 1
    else:
        ingredient_count[ingredient] = 1

# Printing the dictionary
print(ingredient_count)

cats = pd.read_csv('data/categories.csv')
df_ingredient_count = pd.DataFrame.from_dict(ingredient_count, orient='index', columns=['Ingredients'])

final_groceries = df_ingredient_count.merge(cats.set_index(['Ingredients']), right_index=True, left_index=True)
final_groceries.sort_values('Category', inplace=True)
st.write(df)

# Displaying the sorted ingredients as a table in Streamlit
st.table(final_groceries)