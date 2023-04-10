from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy_exc import SQLAlchemyError

from db import db
from models import TagModel, StoreModel
from schemas import TagSchema

blp = Blueprint("Tags", "tags", description="Operations on tags")

@blp.route("/tags")
def get_tags():
    pass