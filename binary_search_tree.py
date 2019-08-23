

class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def empty(self):
        if self.root is None:
            return True
        return False

    def show(self, curr_node):
        if curr_node != None:
            print("%d" % curr_node.label, end=' ')
            self.show(curr_node.left)
            self.show(curr_node.right)


    def insert(self, label):
        #cria um novo nó
        node = Node(label)
        #verifica se a arvore esta vazia
        if self.empty():
            self.root = node
            return
        else:
            dad_node = None
            curr_node = self.root
            while True:
                if curr_node != None:
                    dad_node = curr_node
                    #verifica se vai para esquerda ou direita
                    if node.label < curr_node.label:
                        #vai para esquerda
                        curr_node = curr_node.left
                    else:
                        #vai para a direita
                        curr_node = curr_node.right
                else:
                    # se cure_node é None, então encontrou onde inserir
                    if node.label < dad_node.label:
                        dad_node.left = node
                    else:
                        dad_node.right = node
                    break
                
        
t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(6)
t.insert(1)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)

t.show(t.root)