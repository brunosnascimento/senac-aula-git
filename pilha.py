class Nodo:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class Pilha:
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return '[' + str(self.topo) + ']'

    def insert(self, value):
        novo_nodo = Nodo(value)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def pop(self):
        value = self.topo.dado
        self.topo = self.topo.anterior
        return value

    def list(self):
        nodo = self.topo
        while nodo is not None:
            print("Prato saindo: ", nodo.dado)
            nodo = nodo.anterior

    def search(self, value):
        if self.topo.dado == value:
            print(f"Procurando valor {value} encontrado {self.topo.dado}")
            print(f"Valor {value} encontrado!!")
            return
        nodo = self.topo
        # print(nodo)
        while (nodo is not None) and nodo.dado != value:
            print(f"Procurando valor {value} encontrado {nodo.dado}")
            nodo = nodo.anterior
            if nodo is None:
                break
            if nodo.dado == value:
                print(f"Procurando valor {value} encontrado {nodo.dado}")
                print(f"Valor {value} encontrado")
                return

        print("Valor não encontrado!!!")


p = Pilha()
print(p)

# LIFO - Last in First out (Último a entrar é o primeiro a sair)
nodo1 = Nodo()
nodo2 = Nodo()
nodo3 = Nodo(3)
nodo4 = Nodo(4)

# Nodo: nodo4 => nodo3 => nodo2 => nodo1
nodo4.anterior = nodo3
nodo3.anterior = nodo2
nodo2.anterior = nodo1

p.topo = nodo4
print("Pilha: ", p)

print(nodo1)
print(nodo2)
print(nodo3)
print(nodo4)

p.insert(40)
p.insert(60)
p.insert(7)
print("Pilha: ", p)

p.pop()
p.pop()
print(p)

p.list()

print("Nova busca =======================")
p.search(40)

print("Nova busca =======================")

p.search(7)

print("Nova busca =======================")
p.search(20000)


print("Nova busca =======================")
p.search(3)