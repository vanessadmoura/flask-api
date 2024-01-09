from flask_restx import Namespace


product_ns = Namespace(name='Product',
                       description='Manage product',
                       path='/')
