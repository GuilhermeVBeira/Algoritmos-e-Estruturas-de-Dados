"""
Implementação da priority queue com list ordenada
"""


class Person:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __repr__(self):
        return f"{self.name} - {self.priority}"


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def __repr__(self):
        return f"{self.pq}"

    def push(self, person):
        if self.empty:
            self.pq.append(person)
        else:
            flag_push = False
            # procura-se onde inserir para manter a fila ordenada
            for i in range(len(self.pq)):
                if self.pq[i].priority < person.priority:
                    self.pq.insert(i, person)
                    flag_push = True
                    break
            if not flag_push:
                # se entrou aqui é pq tem que inserir no final
                self.pq.insert(len(self.pq), person)

    def pop(self):
        if not self.empty:
            self.pq.pop(0)

    @property
    def empty(self):
        return len(self.pq) == 0

    def show(self):
        for p in self.pq:
            print(f"Nome: {p.name} - Prioridade: {p.priority}")


p1 = Person("Guilherme", 28)
p2 = Person("Catariana", 3)
p3 = Person("Pedro", 20)
p4 = Person("Joao", 35)

pq = PriorityQueue()
pq.push(p1)
pq.push(p2)
pq.push(p3)
pq.push(p4)
# print("Exibindo as inserções")
# pq.show()


# print("Exibindo após as remoções")
pq.pop()
# pq.show()
pq.push(Person("Goku", 30))
print("Exibindo apos a inserção")
pq.show()
