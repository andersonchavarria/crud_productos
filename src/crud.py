import json 
import os

data_file = "data/productos.json"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            data = json.load(file)
            return data
    else:
        return []

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def create_id():
    product = load_data()
    if product:
        return max(prod['id'] for prod in product) + 1
    return 1


def add_product(name,description, price, quantity):
    data = load_data()  # Carga los datos del archivo
    nuevo_id = create_id()  # Genera un nuevo ID para el producto

    # Muestra los productos antes de agregar el nuevo producto
    print(f"Productos antes de agregar: {data}")
    
    # Crea el nuevo producto
    product = {
        "id": nuevo_id,
        "nombre": name,
        "descripcion": description,
        "precio": price,
        "cantidad": quantity
    }

    # Verifica si los datos son válidos
    if not name or not description or price <= 0 or quantity <= 0:
        raise ValueError("Invalid product data")
    
    data.append(product)  # Agrega el producto a la lista de productos
    save_data(data)  # Guarda los datos en el archivo

    # Muestra los productos después de agregar
    print(f"Productos después de agregar: {data}")
    
    return product


def view_products():
    return load_data()

def update_product(id, name=None,description=None, price=None, quantity=None):
    data = load_data()
    for product in data:
        if product['id'] == id:
            if name is not None:
                product['nombre'] = name
            if description is not None:
                product['descripcion'] = description
            if price is not None:
                product['precio'] = price
            if quantity is not None:
                product['cantidad'] = quantity
            save_data(data)
            return product
    raise ValueError("Product not found.")

def delete_product(id):
    data = load_data()
    for product in data:
        if product['id'] == id:
            data.remove(product)
            save_data(data)
            return product
    raise ValueError("Product not found.")



