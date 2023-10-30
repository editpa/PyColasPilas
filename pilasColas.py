class Cola:
    def __init__(self):
        self.items = []

    def cola(self,x):
        self.items.append(x)
    
    def colaF(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola esta vacia")
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
Mcola.cola("Jose")
Mcola.print_cola()