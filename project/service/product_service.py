from flask import request
from project.ext.database import db
from project.models.product_model import Product


def get_all_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            "id": product.id,
            "name": product.name,
            "value": product.value,
        }
        product_list.append(product_data)
    return product_list


def post_product():
    dados = request.get_json()
    product = Product(**dados)
    if dados['value'] < 0:
        return {"message": "You entered a negative value"}, 400
    elif dados['name'].strip() == "":
        return {"message": "You entered an empty value"}, 400
    else:
        db.session.add(product)
        db.session.commit()
        return {"message": "Successfully created product"}, 201


def get_by_id(id):
    if product := Product.query.get(id):
        return product.to_dict(), 200
    else:
        return {"message": "Product not found"}, 404
    

def put_by_id(id):
    if product := Product.query.get(id):
        data = request.get_json()
        product.name = data.get('name')
        product.value = data.get('value')
        db.session.commit()
        return product.to_dict()
    else:
        return {"message": "Product not found"}, 404


def delete_by_id(id):
    if product := Product.query.get(id):
        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted"}
    else:
        return {"message": "Product not found"}, 404
