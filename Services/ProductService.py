from Model.Product import Product

class ProductService:
    def __init__(self) -> None:
        self.products = []

    def registerProduct(self, product):
        if isinstance(product, Product):
          self.products.append(product)
          print("\n<== Producto registrado con éxito. ==>\n")
        else:
          print("Error: Se esperaba un objeto de tipo Product.")

    def listProducts(self):
        if not self.products:
            print("\n<== No hay productos registrados ==>\n")
        else:
            print("\n<== Lista de Productos ==>\n")
            for product in self.products:
                print(f"IdProduct: {product.idProduct}")
                print(f"Title: {product.title}")
                print(f"Price: {product.price}")
                print(f"Taxes: {product._taxes}")
                print("-" * 20)