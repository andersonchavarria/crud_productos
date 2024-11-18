from unittest.mock import patch
import unittest
from src.crud import add_product, view_products, update_product, delete_product

class TestCrudOperations(unittest.TestCase):

    @patch('src.crud.save_data')  
    @patch('src.crud.load_data')  
    def test_add_product_success(self, mock_load, mock_save):
        mock_load.return_value = []
        
        mock_save.return_value = None
        
      
        add_product("Producto de prueba", "Descripción", 100.0, 10)
        
   
        products = view_products()
        
        # Verificar que el producto se haya añadido correctamente
        self.assertEqual(len(products), 1)  # Verifica que haya un solo producto
        self.assertEqual(products[0]["nombre"], "Producto de prueba")  # Verifica el nombre del producto
        
    @patch('src.crud.save_data') 
    @patch('src.crud.load_data')  
    def test_add_product_error(self, mock_load, mock_save):
      
        mock_load.return_value = []
    
        mock_save.return_value = None
        
        # Probar con un caso de error (producto con valores inválidos)
        with self.assertRaises(ValueError):
            add_product("", "", -100.0, -10)

    @patch('src.crud.save_data')  
    @patch('src.crud.load_data')  
    def test_update_product_success(self, mock_load, mock_save):
       
        mock_load.return_value = [{"id": 1, "nombre": "Producto de prueba", "descripcion": "Descripción", "precio": 100.0, "cantidad": 10}]
       
        mock_save.return_value = None
        
        # Llamar a la función de actualizar producto
        updated_product = update_product(1, name="Producto Actualizado", price=150.0, quantity=5)
        
        # Verificar que el producto se haya actualizado correctamente
        self.assertEqual(updated_product["nombre"], "Producto Actualizado")
        self.assertEqual(updated_product["precio"], 150.0)
        self.assertEqual(updated_product["cantidad"], 5)

    @patch('src.crud.save_data')  
    @patch('src.crud.load_data') 
    def test_update_product_error(self, mock_load, mock_save):
        mock_load.return_value = [{"id": 1, "nombre": "Producto de prueba", "descripcion": "Descripción", "precio": 100.0, "cantidad": 10}]
        
        mock_save.return_value = None
        
        with self.assertRaises(ValueError):
            update_product(9999, name="Producto Inexistente", price=200.0, quantity=10)

    @patch('src.crud.save_data')  
    @patch('src.crud.load_data') 
    def test_delete_product_success(self, mock_load, mock_save):
        mock_load.return_value = [{"id": 1, "nombre": "Producto de prueba", "descripcion": "Descripción", "precio": 100.0, "cantidad": 10}]
        
        mock_save.return_value = None
        
        # Llamar a la función de eliminar producto
        deleted_product = delete_product(1)
        
        # Verificar que el producto se haya eliminado correctamente
        self.assertEqual(deleted_product["nombre"], "Producto de prueba")
        
    @patch('src.crud.save_data') 
    @patch('src.crud.load_data')  
    def test_delete_product_error(self, mock_load, mock_save):
        mock_load.return_value = [{"id": 1, "nombre": "Producto de prueba", "descripcion": "Descripción", "precio": 100.0, "cantidad": 10}]
        
        mock_save.return_value = None
        
        # Probar con un caso de error (producto no existe)
        with self.assertRaises(ValueError):
            delete_product(9999)

if __name__ == "__main__":
    unittest.main()
