from flask import Blueprint

products = Blueprint('products', __name__)

@products.route('/')
def home():
    return 'Hello world'

@products.route('/add_products')
def add_product():
    return 'Add Products'

@products.route('/edit')
def edit_contact():
    return 'Edit Products'


@products.route('/delete')
def delete_contact():
    return 'Delete'
