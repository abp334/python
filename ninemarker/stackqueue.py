# wap to create class StackQueue and define four methods for LIFO and FIFO
# Methods are :
#     PushFirst()
#     PopFirst()
#     PushLast()
#     PopLast()
class StackQueue:
    def __init__(self,l):
        self.l = l
    def pushlast(self,n):
        self.l.append(n)
    def poplast(self):
        if len(self.l) == 0:
            print("Stack Underflow")
        else:
            return self.l.pop()
    def pushfirst(self,n):
        self.l.insert(0,n)
    def popfirst(self):
        if len(self.l) == 0:
            print("Stack Underflow")
        else:
            return self.l.pop(0)
l = []
s = StackQueue(l)
s.pushfirst(1)
s.pushfirst(2)
s.pushlast(3)
s.pushlast(4)
s.popfirst()
s.poplast()
print(l)
