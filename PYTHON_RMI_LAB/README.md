# Python RMI Lab (Pyro5) - Product Catalog

**IT 120 - Integrative Programming Technologies 2**
**Author:** John Joseph Perez (Section HPNO1)

A Python translation of a Java Remote Method Invocation (RMI) project. The
original Java app is a simple distributed product catalog: a server shares
`Product` objects, and a client looks them up over the network and reads their
details. This version reproduces the same architecture in Python using
**Pyro5 (Python Remote Objects)**.

## Project Structure

```
PYTHON_RMI_LAB/
  product.py    # Remote object: Product (name, description, price) + getters
  server.py     # Creates the products and registers them for remote access
  client.py     # Looks up a product by name and calls its remote methods
  README.md
```

## How the Java RMI parts map to Python / Pyro5

| Java RMI | Python (Pyro5) | File |
|---|---|---|
| `Product.java` (remote interface) + `ProductImpl.java` (implementation) | one `Product` class marked with `@Pyro5.api.expose` | `product.py` |
| `Server.java` (`UnicastRemoteObject.exportObject`, `registry.bind`) | `daemon.register(obj)` + `name_server.register(name, uri)` | `server.py` |
| `Client.java` (`registry.lookup`, `obj.getName()`) | `Pyro5.api.Proxy("PYRONAME:laptop")`, `obj.get_name()` | `client.py` |
| `rmiregistry` (the RMI registry process) | the Pyro5 name server (`python -m Pyro5.nameserver`) | n/a |

The four products registered by the server are the same as the Java version:
`laptop` (Laptop), `ram` (Mobile), `bag` (Bag), and `charger` (Charger).

## Requirements

- Python 3.9 or newer
- Pyro5

```bash
pip install Pyro5
```

## How to Run

Just like Java RMI needs `rmiregistry` running, Pyro5 needs its name server
running. Use **three terminals**, in this order.

**Terminal 1 - start the name server (the registry):**
```bash
python -m Pyro5.nameserver
```
Leave it running. It listens on 127.0.0.1:9090.

**Terminal 2 - start the server:**
```bash
python server.py
```
You should see it register the four products and print
`Server is ready. Waiting for client requests...`. Leave it running.

**Terminal 3 - run the client:**
```bash
python client.py
```

## Expected Client Output

```
Name: Laptop
Description: Lenovo laptop
Price: 800000.0

--- Full product catalog ---
[laptop] Laptop - Lenovo laptop - Price: 800000.0
[ram] Mobile - MI 9 mobile - Price: 24000.0
[bag] Bag - Branded bag - Price: 800.0
[charger] Charger - MI Charger - Price: 230.0
```

## How It Works (short)

1. The name server runs and acts as a phone book for remote objects.
2. `server.py` creates the `Product` objects, exports each one through a Pyro5
   daemon to get a remote address (URI), and registers each URI under a name
   (laptop, ram, bag, charger) in the name server.
3. `client.py` asks the name server for the object named "laptop", receives a
   proxy that stands in for the remote object, and calls its methods. The calls
   run on the server and the results are returned over the network.
