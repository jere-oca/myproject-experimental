from utils.db import db  

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Product('{self.nombre}', '{self.marca}', '{self.precio}')"