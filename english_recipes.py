import csv

recipes = [
    {
        "Meal": "Mushroom Risotto",
        "Ingredients": "Arborio rice, Mushrooms, Vegetable broth, White wine, Onion, Garlic, Parmesan cheese, Butter, Thyme"
    },
    {
        "Meal": "Greek Salad",
        "Ingredients": "Cucumbers, Tomatoes, Red onion, Kalamata olives, Feta cheese, Olive oil, Red wine vinegar, Dried oregano"
    },
    {
        "Meal": "Vegetable Pasta",
        "Ingredients": "Pasta, Zucchini, Cherry tomatoes, Spinach, Garlic, Olive oil, Parmesan cheese, Basil"
    },
    {
        "Meal": "Quinoa Salad",
        "Ingredients": "Quinoa, Cucumber, Bell peppers, Red onion, Cherry tomatoes, Parsley, Lemon juice, Olive oil"
    },
    {
        "Meal": "Ratatouille",
        "Ingredients": "Eggplant, Zucchini, Bell peppers, Onion, Garlic, Tomato, Thyme, Basil, Olive oil"
    },
    {
        "Meal": "Vegetable Fajitas",
        "Ingredients": "Bell peppers, Onion, Mushrooms, Zucchini, Tortillas, Chili powder, Cumin, Paprika, Lime juice"
    },
    {
        "Meal": "Sweet Potato and Black Bean Bowl",
        "Ingredients": "Sweet potatoes, Black beans, Avocado, Corn, Red onion, Cilantro, Lime juice, Cumin"
    },
    {
        "Meal": "Cauliflower Fried Rice",
        "Ingredients": "Cauliflower, Carrots, Peas, Eggs, Soy sauce, Garlic, Ginger, Green onions"
    },
    {
        "Meal": "Zucchini Noodles with Pesto",
        "Ingredients": "Zucchini, Basil, Pine nuts, Parmesan cheese, Garlic, Olive oil, Lemon juice"
    },
    {
        "Meal": "Tomato Basil Soup",
        "Ingredients": "Tomatoes, Onion, Garlic, Vegetable broth, Fresh basil, Olive oil, Cream, Salt, Pepper"
    },
    {
        "Meal": "Vegetable Tacos",
        "Ingredients": "Corn tortillas, Black beans, Corn, Avocado, Cabbage, Cilantro, Lime juice, Chili powder"
    },
    {
        "Meal": "Eggplant Parmesan",
        "Ingredients": "Eggplant, Marinara sauce, Mozzarella cheese, Parmesan cheese, Breadcrumbs, Eggs, Olive oil"
    },
    {
        "Meal": "Stuffed Mushrooms",
        "Ingredients": "Mushrooms, Cream cheese, Parmesan cheese, Garlic, Breadcrumbs, Olive oil, Parsley"
    },
    {
        "Meal": "Garlic Butter Asparagus",
        "Ingredients": "Asparagus, Butter, Garlic, Lemon juice, Parmesan cheese"
    },
    {
        "Meal": "Lentil Soup",
        "Ingredients": "Lentils, Carrots, Celery, Onion, Garlic, Vegetable broth, Cumin, Coriander, Turmeric"
    },
    {
        "Meal": "Cucumber Tomato Salad",
        "Ingredients": "Cucumbers, Tomatoes, Red onion, Olive oil, Red wine vinegar, Dill, Salt, Pepper"
    },
    {
        "Meal": "Mushroom Tacos",
        "Ingredients": "Portobello mushrooms, Cumin, Chili powder, Paprika, Lime juice, Cilantro, Red cabbage, Avocado"
    },
    {
        "Meal": "Vegetable Skewers",
        "Ingredients": "Bell peppers, Zucchini, Red onion, Cherry tomatoes, Mushrooms, Olive oil, Balsamic glaze, Thyme"
    },
    {
        "Meal": "Broccoli and Cheese Casserole",
        "Ingredients": "Broccoli, Cheddar cheese, Cream cheese, Garlic, Onion, Breadcrumbs, Butter, Milk"
    },
    {
        "Meal": "Spinach Artichoke Dip",
        "Ingredients": "Spinach, Artichoke hearts, Cream cheese, Sour cream, Garlic, Mozzarella cheese, Parmesan cheese"
    }
]

# Writing to csv
with open('vegetarian_recipes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Meal", "Ingredients"])
    for recipe in recipes:
        writer.writerow([recipe['Meal'], recipe['Ingredients']])
