
class Node:
    def __init__(self, label):
        self.label = label
        self.next = None


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self._len_list = 0

    def empty(self):
        return self.first == None
    
    def show(self):
        
        curr_node = self.first

        while curr_node != None:
            print(curr_node.label, end="")
            curr_node = curr_node.next
        print("")

    def pop(self, index):
        if not self.empty() and index >= 0 and index < self._len_list:
            flag_remove = False
            if self.first.next is None:
                #possui apenas um elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # remove do incio mas possui mais de 1 elemento
                self.first = self.first.next
                flag_remove = True
            else:
                # possui mais de um elemento e nào remove do inicio
                prev_node = self.first
                curr_node = self.first.next
                curr_index = 1

                while curr_index != None:

                    if index == curr_index:
                        prev_node.next = curr_node.next
                        curr_node.next = None
                        flag_remove = True
                        break
                    prev_node = curr_node
                    curr_node = curr_node.next
                    curr_index += 1

                if flag_remove:
                    self._len_list -=1

    def push(self, label, index):
        if index >= 0:
            node = Node(label)

            if self.empty():
                self.first = node
                self.last = node
            else:
                if index == 0:
                    #inserção no inicio
                    node.next = self.first
                    self.first = node

                elif index >= self._len_list:
                    # inserção no final
                    self.last = node
                else:
                    # inserção no meio
                    prev_node = self.first
                    curr_node = self.first.next
                    curr_index = 1

                    while curr_node != None:
                        if curr_index == index:
                            #seta o curr_node como proximo do nó
                            node.next = curr_node
                            #seta o node como o proximo do prev_node
                            prev_node.next = node

                            break
                        prev_node = curr_node
                        curr_node = curr_node.next
                        curr_index += 1
            #atualiza o tamanho da lista
            self._len_list +=1
