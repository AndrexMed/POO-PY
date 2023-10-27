class Product:
    def __init__(self):
        self._idProduct = None
        self._title = None
        self._price = None
        self._taxes = None

    @property
    def idProduct(self):
        return self._idProduct

    @idProduct.setter
    def idProduct(self, value):
        self._idProduct = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        self._taxes = self.calculate_taxes()  # Calculamos impuestos cuando se establece el precio

    def calculate_taxes(self):
        if self._price is not None:
            taxes = self._price * 0.19
            return taxes
        return 0  # Retornamos 0 si el precio no está definido