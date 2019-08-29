from collections import defaultdict
# node
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
#graph

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def link_to_edge(self, p1, p2):
        self.graph[p1].append(p2)
        self.graph[p2].append(p1)

    def show_friends(self, person):
        for friend in self.graph[person]:
            print('%s' % friend.name)

p1 = Person("Maria", 20)
p2 = Person("Pedro", 30)
p3 = Person("Diego", 18)
p4 = Person("Carol", 25)
p5 = Person("Yankee", 14)

g = Graph()
g.link_to_edge(p1, p2)
g.link_to_edge(p1, p3)
g.link_to_edge(p2, p4)
g.link_to_edge(p4, p3)
g.link_to_edge(p5, p1)

g.show_friends(p1)