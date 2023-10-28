from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

class Kitchen_item(BaseModel):
    name: str
    quantity: int

with open('data/pantry.json', 'r') as file:
    pantry_data = json.load(file)


class PantryItem(BaseModel):
    name: str
    quantity: int

class PantryData(BaseModel):
    vegetables: List[PantryItem]
    condiments: List[PantryItem]
    starches: List[PantryItem]
    dairies: List[PantryItem]
    tins: List[PantryItem]
    others: List[PantryItem]


@app.get("/pantry")
async def get_pantry():
    return pantry_data

@app.post("/update_quantity")
async def update_quantity(item: Kitchen_item):
    global pantry_data
    item_found = False
    for category, items in pantry_data.items():
        for i in range(len(items)):
            if items[i]['name'] == item.name:
                items[i]['quantity'] = item.quantity
                item_found = True
                break

    if not item_found:
        # Ajouter un nouvel élément si l'article n'existe pas déjà
        pantry_data[category].append({"name": item.name, "quantity": item.quantity})

    # Écrire les données mises à jour dans le fichier JSON
    with open('data/pantry.json', 'w') as file:
        json.dump(pantry_data, file, indent=4)

    return {"message": f"La quantité pour {item.name} a été mise à jour à {item.quantity}."}


# @app.post("/increment_quantity")
# async def increment_quantity(pantry_item: PantryItem):
#     global pantry_data
#     for category, items in pantry_data.items():
#         for item in items:
#             if item["name"] == pantry_item.name:
#                 item["quantity"] += 1
#                 break

#     # Write the updated data to the JSON file
#     try:
#         with open('data/pantry.json', 'w') as file:
#             json.dump(pantry_data, file, indent=4)
#     except Exception as e:
#         return {"message": f"Failed to update the JSON file: {e}"}

#     return {"message": f"Quantity of {pantry_item.name} incremented successfully."}

# @app.post("/decrement_quantity")
# async def decrement_quantity(pantry_item: PantryItem):
#     global pantry_data
#     for category, items in pantry_data.items():
#         for item in items:
#             if item["name"] == pantry_item.name:
#                 if item["quantity"] > 0:
#                     item["quantity"] -= 1
#                 else:
#                     return {"message": f"The quantity of {pantry_item.name} is already 0."}
#                 break

#     # Write the updated data to the JSON file
#     try:
#         with open('data/pantry.json', 'w') as file:
#             json.dump(pantry_data, file, indent=4)
#     except Exception as e:
#         return {"message": f"Failed to update the JSON file: {e}"}

#     return {"message": f"Quantity of {pantry_item.name} decremented successfully."}
