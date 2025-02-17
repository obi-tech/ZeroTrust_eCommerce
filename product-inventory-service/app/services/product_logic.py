products = {}  # Simulated in-memory database


def add_product(request):
    product = {
        "id": request.id,
        "name": request.name,
        "description": request.description,
        "price": request.price,
        "quantity": request.quantity
    }
    products[request.id] = product
    return product


def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return {"error": "Product not found"}
    return product


def update_product(request):
    if request.id not in products:
        return {"error": "Product not found"}
    product = products[request.id]
    product.update({
        "name": request.name,
        "description": request.description,
        "price": request.price,
        "quantity": request.quantity
    })
    return product


def delete_product(product_id):
    if product_id not in products:
        return {"error": "Product not found"}
    del products[product_id]
    return {"message": "Product deleted successfully"}
