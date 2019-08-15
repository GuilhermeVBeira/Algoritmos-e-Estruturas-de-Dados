
class Deque:
    def __init__(self):
        self.deque = []
        self.len = 0

    def empty(self):
        return self.len == 0

    def push_front(self, e):
        self.deque.insert(0, e)
        self.len += 1
    
    def push_back(self, e):
        self.deque.append(e)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len -= 1
    
    def pop_back(self):
        if not self.empty():
            self.deque.pop()
            self.len -= 1
    
    def front(self):
        if not self.empty():
            return self.deque[0]
    
    def back(self):
        if not self.empty():
            return self.deque[-1]

    def show(self):
        print(self.deque)
