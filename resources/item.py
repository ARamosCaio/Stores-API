import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema, ItemUpdateSchema
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import ItemModel

blp = Blueprint("Items", "items", description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        # sourcery skip: inline-immediately-returned-variable
        item = ItemModel.query.get_or_404(item_id)
        return item
        
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted"}

    def put(self, item_id):
        item_data = request.get_json()

        if "price" not in item_data or "name" not in item_data:
            abort(400, message="Bad request. Ensure 'price' and 'name' are included in the JSON payload")
        
        try:
            item = items[item_id]
            item |= item_data
        
            return item
        except KeyError:
            abort(404, message="Item not found")    

@blp.response(200, ItemSchema(many=True))
def get(self):
    return ItemModel.query.all()

@blp.arguments(ItemSchema)
@blp.response(201, ItemSchema)
def post(self, item_data):
    
    item = ItemModel(**item_data)
    try:
        db.session.add(item)
        de.session.commit()
    
    except SQLAlchemyError:
        abort(500, message="An error occurred while inserting the item")

    return item

@blp.arguments(ItemUpdateSchema)
@blp.response(200, ItemSchema)
def put(self, item_data, item_id):  # sourcery skip: use-named-expression
    item = ItemModel.query.get(item_id)
    if item:
        item.price = item_data["price"]
        item.name = item_data["name"]

    else:
        item = ItemModel(id=item_id, **item_data)
    
    db.session.add(item)
    db.session.commit()

    return item
