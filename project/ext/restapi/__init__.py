from flask import Blueprint
from flask_restx import Api

from project.controller.product_controller import ProductResource, ProductResourceId
from project.utils.namespace import product_ns


bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    app.register_blueprint(bp)
    api.add_resource(ProductResource, "/products/")
    api.add_resource(ProductResourceId, "/product/<int:id>")
    api.add_namespace(product_ns)