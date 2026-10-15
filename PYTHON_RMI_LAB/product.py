"""
product.py
IT 120 - Java RMI to Python (Pyro5) translation
Author: John Joseph Perez (Section HPNO1)

Equivalent to the Java files:
  - Product.java     (the remote interface: getName, getDescription, getPrice)
  - ProductImpl.java (the implementation: attributes + the getter methods)

In Java RMI you need a separate interface (Product) and an implementation
class (ProductImpl). In Python with Pyro5 we combine both into one class and
simply mark it with @Pyro5.api.expose so its methods can be called remotely.
"""

import Pyro5.api


@Pyro5.api.expose
class Product:
    # Attributes (same as ProductImpl.java: name, description, price)
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    # Remote methods (same signatures as the Product interface in Java)
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price
