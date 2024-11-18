import unittest
import json
import os
from src.crud import add_product, view_products, update_product, delete_product

data_file = "data/productos.json"

# Helper functions to reset data file between tests
def reset_data_file():
    if os.path.exists(data_file):
        os.remove(data_file)
    with open(data_file, "w") as file:
        json.dump([], file)

class TestCRUDOperations(unittest.TestCase):
    
    def setUp(self):
        reset_data_file()  # Reset data before each test
    
    def test_add_product_success(self):
        # Test successful product addition
        add_product("Producto1", "Descripción de Producto1", 100.0, 10)
        products = view_products()  # Get all products after adding one
        self.assertEqual(len(products), 1)  # Verify there is one product
        self.assertEqual(products[0]['nombre'], "Producto1")
        self.assertEqual(products[0]['descripcion'], "Descripción de Producto1")
        self.assertEqual(products[0]['precio'], 100.0)
        self.assertEqual(products[0]['cantidad'], 10)

    def test_add_product_invalid_data(self):
        # Test adding a product with invalid data (negative price)
        with self.assertRaises(ValueError):
            add_product("Producto2", "Descripción de Producto2", -10.0, 5)

    def test_view_products_empty(self):
        # Test viewing products when the list is empty
        self.assertEqual(len(view_products()), 0)

    def test_update_product_success(self):
        # Test successful product update
        product = add_product("Producto3", "Descripción de Producto3", 200.0, 5)
        updated_product = update_product(product['id'], name="Producto3 Actualizado", price=250.0, quantity=8)
        self.assertEqual(updated_product['nombre'], "Producto3 Actualizado")
        self.assertEqual(updated_product['precio'], 250.0)
        self.assertEqual(updated_product['cantidad'], 8)

    def test_update_product_not_found(self):
        # Test updating a product that does not exist
        with self.assertRaises(ValueError):
            update_product(9999, name="Producto Inexistente", price=300.0, quantity=10)

    def test_delete_product_success(self):
        # Test successful product deletion
        product = add_product("Producto4", "Descripción de Producto4", 150.0, 15)
        deleted_product = delete_product(product['id'])
        self.assertEqual(len(view_products()), 0)
        self.assertEqual(deleted_product['nombre'], "Producto4")
    
    def test_delete_product_not_found(self):
        # Test deleting a product that does not exist
        with self.assertRaises(ValueError):
            delete_product(9999)

    def test_create_id_success(self):
        # Test that the product ID is generated correctly
        add_product("Producto5", "Descripción de Producto5", 120.0, 12)
        new_id = add_product("Producto6", "Descripción de Producto6", 130.0, 14)['id']
        self.assertEqual(new_id, 2)

if __name__ == "__main__":
    unittest.main()
