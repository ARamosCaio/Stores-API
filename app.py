from flask import Flask, request
from db import stores, items
from flask_smorest import abort
import uuid

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.get("/store/<string:name>")
def get_store(store_id):  # sourcery skip: use-next
    try:

        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")

@app.get("/store/<string:name>/item")
def get_item_in_store(item_id):  # sourcery skip: use-next
        try: 
            return items[item_id]
        except KeyError:
            return {"message": "Store not found"}, 404

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    
    return store

@app.post("/store/<string:name>/item")
def create_item(name):
    item_data = request.get_json()
    
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item 

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")