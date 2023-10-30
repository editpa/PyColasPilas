class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, x):  # Cambié "cola" a "encolar"
        self.items.append(x)

    def desencolar(self):  # Cambié "colaF" a "desencolar"
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise ValueError("La cola está vacía")

    def esta_vacia(self):  # Agregué un método para verificar si la cola está vacía
        return len(self.items) == 0

    def print_cola(self):
        print(self.items)


class Pila:
    def __init__(self):  # Corregí "__init__" para que tenga dos guiones bajos en cada lado
        self.items = []

    def push(self, item):
        self.items.append(item)  # Cambié "insert(0, item)" a "append(item)" para que funcione como una pila

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise ValueError("La pila está vacía")

    def esta_vacia(self):  # Agregué un método para verificar si la pila está vacía
        return len(self.items) == 0

    def print_pila(self):
        print(self.items)

# Ejemplo de uso
Mpila = Pila()
Mpila.push("Eduardo")
Mpila.print_pila()

Mcola = Cola()
Mcola.encolar("José")
Mcola.print_cola()
