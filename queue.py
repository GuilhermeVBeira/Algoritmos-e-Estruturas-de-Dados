
class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1

    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1
    
    def empty(self):
        return self.len_queue == 0

    def length(self):
        return self.len_queue
    
    def front(self):
        if not self.empty():
            return self.queue[0]
    
    def back(self):
        if not self.empty():
            return self.queue[-1]