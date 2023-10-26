#GalloConTennis

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

#Paso 3: Hacer dos listas y mandar llamar las funciones llenando la lista con números de 1 al 10.

lista1 = int(input("Digita la cantidad de elementos de la lista: " ))
list=[]
i=0

while 1 <= lista1:
    lista1= input("Digita los elementos de la lista: ")
    lista1.append(lista1)
    i+=1

for i in lista1:
    print(i)