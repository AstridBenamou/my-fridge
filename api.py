from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

with open('data/pantry.json', 'r') as file:
    data = json.load(file)

class ItemRequest(BaseModel):
    category: str
    item_name: str

@app.get("/pantry")
async def get_pantry():
    return data


# Point de terminaison pour la requête POST
@app.post('/increment_quantity')
async def increment_quantity(item_request: ItemRequest):
    category = item_request.category
    item_name = item_request.item_name

    # Rechercher l'élément dans le fichier JSON et ajouter 1 à la quantité
    for item in data[category]:
        if item['name'] == item_name:
            item['quantity'] += 1

    # Mettre à jour le fichier JSON
    with open('data/pantry.json', 'w') as f:
        json.dump(data, f, indent=4)

    return {'message': f'La quantité de {item_name} a été mise à jour avec succès.'}


# Point de terminaison pour la requête POST
@app.post('/decrement_quantity')
async def decrement_quantity(item_request: ItemRequest):
    category = item_request.category
    item_name = item_request.item_name

    # Rechercher l'élément dans le fichier JSON et ajouter 1 à la quantité
    for item in data[category]:
        if item['name'] == item_name:
            if item['quantity'] > 0:
                item['quantity'] -= 1
            break

    # Mettre à jour le fichier JSON
    with open('data/pantry.json', 'w') as f:
        json.dump(data, f, indent=4)

    return {'message': f'La quantité de {item_name} a été mise à jour avec succès.'}