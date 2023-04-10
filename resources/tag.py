from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy_exc import SQLAlchemyError

from db import db
from models import TagModel, StoreModel
from schemas import TagSchema

blp = Blueprint("Tags", "tags", description="Operations on tags")

@blp.route("/store/<string:store_id>/tag")
class TagsInStore(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, store_id):
        stores = StoreModel.query.get_or_404(store_id)
        return store.tags.all()