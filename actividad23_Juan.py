


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


#Ejemplo de uso 
Mpila = Pila()
Mpila.push("Eduardo")
Mpila.print_pila()

Mcola = Cola()
Mcola.cola("José")
Mcola.print_cola()



Lista1 = [i for i in range(1, 11)]
Lista2 = [i for i in range(1, 11)]


def Imprimir_lista(Lista):
    for elemento in Lista:
        print(elemento, end=' ')
    print()


print("Contenido de la lista 1:")
Imprimir_lista(Lista1)

print("Contenido de la lista 2:")
Imprimir_lista(Lista2)