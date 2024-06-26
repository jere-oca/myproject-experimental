import unittest
from flask import Flask, url_for
from flask_testing import TestCase

# Importa la aplicación Flask
from app.run import app

class TestRedirecciones(TestCase):

    def create_app(self):
        # Configura la aplicación para pruebas
        app.config['TESTING'] = True
        return app

    def test_redireccion_agregar_marca(self):
        # Realiza una solicitud ficticia a la ruta de 'marcas.add_marca'
        with self.client:
            response = self.client.get(url_for('marcas.add_marca'))
            self.assert200(response)  # Asegura que la respuesta sea exitosa (código 200)

    def test_redireccion_inicio(self):
        # Realiza una solicitud ficticia a la ruta de 'products.home'
        with self.client:
            response = self.client.get(url_for('products.home'))
            self.assert200(response)  # Asegura que la respuesta sea exitosa (código 200)

if __name__ == '__main__':
    unittest.main()
