from utils.db import db  

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    marca = db.Column(db.Integer, db.ForeignKey('marca.nombre'), nullable=False)

    def __repr__(self):
        return f"Product('{self.nombre}', '{self.marca}', '{self.precio}')"
    
