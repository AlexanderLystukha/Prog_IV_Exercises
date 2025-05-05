class Link:
    def __init__(self, element=None):
        self.element = element
        self.next = None


class StackList:
    def __init__(self):
        self.head: Link = None

    def push(self, x):
        hi = Link(x)
        hi.next = self.head
        self.head = hi
    def pop(self):
        if self.head is None:
            raise Exception
        c = self.head.next
        self.head.next = None
        self.head = c

class QueueList:
    def __init__(self):
        self.head: Link = None

    def push(self, x):
        hi = Link(x)
        hi.next = self.head
        self.head = hi
    def pop(self):
        if self.head is None:
            raise Exception
        c = self.head.next
        self.head.next = None
        self.head = c

def make_chain(length: int):
    link = Link()
    head = link
    for i in range(length):
        head.element = i + 1
        head.next = Link()
        head = head.next

    return link


temp: Link = make_chain(4)

while temp.next is not None:
    print(temp.element)
    temp = temp.next

# head = Link()
# head.element = 1
# head.next = Link()
# head.next.element = 2
# head.next.next = Link()
# head.next.next.element = 3
# head.next.next.next = Link()
# head.next.next.next.element = 4
