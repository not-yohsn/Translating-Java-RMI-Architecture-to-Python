"""
client.py
IT 120 - Java RMI to Python (Pyro5) translation
Author: John Joseph Perez (Section HPNO1)

Equivalent to the Java file:
  - Client.java (looks up a remote object and calls its methods)

Java RMI flow                 ->  Pyro5 flow
-----------------------------------------------------------------
LocateRegistry.getRegistry    ->  connect via the name server
registry.lookup("laptop")     ->  Pyro5.api.Proxy("PYRONAME:laptop")
laptop.getName()              ->  laptop.get_name()

The name server must be running, and server.py must already be started.
"""

import Pyro5.api


def main():
    # Look up the "laptop" remote object by name (same as Client.java).
    # "PYRONAME:laptop" asks the name server to resolve the name to a remote object.
    laptop = Pyro5.api.Proxy("PYRONAME:laptop")

    print("Name:", laptop.get_name())
    print("Description:", laptop.get_description())
    print("Price:", laptop.get_price())

    # Bonus: look up and display all registered products to show the full catalog.
    print("\n--- Full product catalog ---")
    for bind_name in ("laptop", "ram", "bag", "charger"):
        product = Pyro5.api.Proxy("PYRONAME:" + bind_name)
        print(f"[{bind_name}] {product.get_name()} - "
              f"{product.get_description()} - Price: {product.get_price()}")


if __name__ == "__main__":
    main()
