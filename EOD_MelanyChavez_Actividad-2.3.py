##Programa solucionado

class Cola:
    def __init__(self):
        self.items = []

    def cola(self,x):
        self.items.append(x)

    def colaF(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    def print_cola(self):
        print(self.items)


class Pila:
    def __init__(self):
        self.items = []


    def push(self, item): 
        self.items.insert(0, item)

    def pop(self): 
        return self.items.pop(0)

    def print_pila(self):
        print(self.items)
 
Mpila = Pila()
Mpila.push("Eduardo")
Mpila.print_pila()

Mcola = Cola()
Mcola.cola("José")
Mcola.print_cola()

#Hacer dos listas y mandar llamar las funciones llenando la lista con números de 1 al 10.
lista1 = []
lista2 = []

for numero in range(1, 11):
    lista1.append(numero)
    lista2.append(numero)
print("Lista 1:", lista1)
print("Lista 2:", lista2)