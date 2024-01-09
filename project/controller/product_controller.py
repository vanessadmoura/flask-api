from flask_restx import Api, Resource
from ..service.product_service import get_all_products, post_product, get_by_id, delete_by_id, put_by_id


api = Api()


class ProductResource(Resource):
    
    def get(self):
        products = get_all_products()
        return products, 200
    

    def post(self):
        product = post_product()
        return product, 201
    

class ProductResourceId(Resource):

    def get(self, id):
        if product := get_by_id(id):
            return product, 200
        
    def put(self, id):
        if product := put_by_id(id):
            return product, 200
        
    def delete(self, id):
        if product := delete_by_id(id):
            return product, 200
