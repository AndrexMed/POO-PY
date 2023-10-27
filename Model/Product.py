class Product:
    def __init__(self):
        self._title = None
        self._price = None
        self.taxes = 500

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

    def calculate_taxes(self):
        return self._price * 0.19