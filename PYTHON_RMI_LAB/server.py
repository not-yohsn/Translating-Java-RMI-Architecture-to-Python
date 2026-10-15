"""
server.py
IT 120 - Java RMI to Python (Pyro5) translation
Author: John Joseph Perez (Section HPNO1)

Equivalent to the Java files:
  - Server.java      (creates the product objects and registers them)
  - ProductImpl.java (the objects being served, imported from product.py)
  - ServerImpl.java  (empty in the original Java project)

Java RMI flow            ->  Pyro5 flow
-----------------------------------------------------------------
UnicastRemoteObject       ->  daemon.register(object)
LocateRegistry.getRegistry->  Pyro5.api.locate_ns()  (the name server)
registry.bind(name, stub) ->  ns.register(name, uri)

Before running this file, the Pyro5 name server must be running. It is the
Python equivalent of Java's rmiregistry. Start it in its own terminal with:
    python -m Pyro5.nameserver
"""

import Pyro5.api
from product import Product


def main():
    print("Server is booting....")

    # Create the Pyro5 daemon (handles incoming remote calls, like UnicastRemoteObject).
    daemon = Pyro5.api.Daemon(host="127.0.0.1")

    # Locate the running name server (the equivalent of the RMI registry).
    name_server = Pyro5.api.locate_ns()

    # Create the product objects (same data as Server.java).
    products = {
        "laptop": Product("Laptop", "Lenovo laptop", 800000.0),
        "ram": Product("Mobile", "MI 9 mobile", 24000.0),
        "bag": Product("Bag", "Branded bag", 800.0),
        "charger": Product("Charger", "MI Charger", 230.0),
    }

    # Export each object through the daemon and bind its name in the name server.
    for bind_name, obj in products.items():
        uri = daemon.register(obj)          # export the object -> get a remote URI
        name_server.register(bind_name, uri)  # bind the name so clients can look it up
        print(f"Registered '{bind_name}' -> {uri}")

    print("Server is ready. Waiting for client requests... (press Ctrl+C to stop)")
    daemon.requestLoop()


if __name__ == "__main__":
    main()
