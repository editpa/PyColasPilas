


class Cola:
    def __init__(self):
        self.items = []

    def cola(self,x):
        self.items.append(x) #Esta linea nos permite agregar elementos a una cola
    
    def colaF(self):
        try:
            return self.items.pop(0) #Esta linea nos permite eliminar todos los registros de una cola
        except:
            raise ValueError("La cola está vacía")
    def print_cola(self):
        print(self.items) #Esta linea nos permite imprimir todos los elementos de una cola


class Pila:
    def __init__(self):
        self.items = []
    
     
    def push(self, item): 
        self.items.insert(0, item) #Esta linea nos permite agregar elementos a una pila
     
    def pop(self): 
        return self.items.pop(0) #Esta linea nos permite eliminar todos los registros de una pila
     
    def print_pila(self):
        print(self.items)  #Esta linea nos imprime todos los elementos de la pila


#Ejemplo de uso 
Mpila = Pila()
Mpila.push("Eduardo")
Mpila.print_pila()


Mcola = Cola()
Mcola.cola("José")
Mcola.print_cola()

Lista1 = Pila() #Crear pila
Lista2 = Cola() #Crear cola

for i in range (1,11):
    Lista1.push(i) #Agregar elementos
    Lista2.cola(i) #Agregar elementos

Lista1.print_pila() #Imprimir pila
Lista2.print_cola() #Imprimir cola

for i in range (1,11):
    Lista1.pop() #Eliminar elementos de la pila 
    Lista2.colaF() #Eliminar elementos de la cola

Lista1.print_pila() #Imprimir pila sin elementos
Lista2.print_cola() #Imprimir cola sin elementos