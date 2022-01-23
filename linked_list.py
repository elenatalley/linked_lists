# class Node have 2 elem: value and link on next node
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
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

    def delete_last(self):
        if self.head == self.tail:
            return False
        current_node = self.head
        while current_node.next_node != self.tail:
            current_node = current_node.next_node
        current_node.next_node = None
        return True

    def delete_first(self):
        if self.head == self.tail:
            return False
        self.head.next_node = self.head.next_node.next_node
        if self.head.next_node == None:# когда удалили все элем из списка
            self.tail = self.head
        return True

    # 2(0)->4(1)->8(2)->15(3): need to delete 8(2)
    # нужно удалить ссылку числа 8(2), после 4(1) будет иметь ссылку на 15(3)
    # питон при компиляции удалит этот нод -  8(2)
    def delete_by_index(self, index):
        index_prev = index - 1
        prev = self.head
        count = -1
        while prev != None and count < index_prev:
            current_el = prev.next_node
            count += 1 # счетчик
            node_to_delete = current_el.next_node
            next_after_deleted = node_to_delete.next_node
            current_el.next_node = next_after_deleted
            return
        if index == 0:
            self.delete_first()
            return
        else:
            print("Index out of range")


    def append(self, value):
        n = Node(value, None)
        self.tail.next_node = n # взять ссылку на след
        self.tail = n

    def appfront (self, value):
        self.head.next_node = Node(value, self.head.next_node)

    def insert (self, index, value):
        index_prev = index - 1
        prev = self.head
        ind = -1
        while prev != None and ind < index_prev:  # I
            prev = prev.next_node
            ind += 1
        if prev == None:  # особые случаи
            self.append(value)
            return
        temp = prev.next_node
        n = Node(value, None)
        prev.next_node = n  # II,III
        n.next_node = temp  # IV

    def remove_first_elem(self):
        current_node = self.head # found first elem
        self.head = current_node #  set a new head = nex elem after current
# self.head.next_node = Node(value, self.head.next_node)



lst = LinkedList()
lst.append(10)
print(lst)
lst.append(20)
print(lst)
lst.append(30)
print(lst)
lst.append(40)
print(lst)
#
# lst.appfront(0)
# print(lst)
# lst.appfront(-10)
# print(lst)
#
# lst.insert(0, -20)
# print(lst)
#
# lst.insert(100, 50)
# print(lst)
lst.delete_by_index(10)
print(lst)







