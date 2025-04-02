class Node:
    def __init__(self, value):
        self.value = value  # Valor armazenado no nó
        self.next = None  # Ponteiro para o próximo nó


class CircularLinkedList:
    def __init__(self):
        self.head = None  # Ponteiro para o primeiro nó
        self.tail = None  # Ponteiro para o último nó

    # Adicionar um novo nó à lista
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node  # Se a lista estiver vazia, o novo nó será o primeiro nó
            self.tail = new_node  # O novo nó também será o último nó
            self.tail.next = self.head  # O último nó aponta para o primeiro nó (fazendo a lista circular)
        else:
            self.tail.next = new_node  # O atual último nó aponta para o novo nó
            self.tail = new_node  # O novo nó se torna o último nó
            self.tail.next = self.head  # O novo último nó aponta para o primeiro nó

    # Imprimir a lista circular
    def print_list(self):
        if self.head is None:
            print("A lista está vazia!")
            return

        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:  # Se voltarmos ao início, paramos
                break
        print(f"(voltando ao início: {self.head.value})")


# Exemplo de uso
circular_list = CircularLinkedList()

# Adicionando elementos à lista circular
circular_list.append(1)
circular_list.append(2)
circular_list.append(3)
circular_list.append(4)

# Imprimindo a lista circular
circular_list.print_list()