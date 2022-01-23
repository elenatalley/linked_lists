"""
 Класс узла структуры двухсвязанного списка
"""
class Node:
    def __init__(self, data, next_node, previous_node):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

    def __str__(self):
        return str(self.data)

class DoublelinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = self.head

    def get_head(self): #get next node
        return self.head.next_node

    def __str__(self):
        current_node = self.get_head()
        res = ""
        while current_node != None:
            res += str(current_node) + " "
            current_node = current_node.next_node
        return res

    def append(self, value):
        new_node = Node(value, None, None)
        self.tail.next_node = new_node
        self.tail = new_node

l = DoublelinkedList()
l.append(2)
l.append(5)
l.append(12)
print(l)