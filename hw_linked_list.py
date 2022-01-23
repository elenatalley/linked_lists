# create class with Node with elem and link on next elem
class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    # возвращает элем текущего нода
    def get_data(self):
        return self.data
    # возвращает след элем текущего нода
    def get_next_node(self):
        return self.next_node
    # задавать заданную дату для текущего  нода
    def set_data(self, data):
        self.data = data
    #to set next node
    def set_next_node(self,next_node):
        self.next_node = next_node

#create class where will be method for list
class LinkedList:
    def __init__(self):
        self.head = None
#to create list need append elements
    def append(self, data):
        new_node = Node(data)
        current_node = self.head #start
        if current_node == None: #when empty list, first run
            self.head = new_node
            return
        #  пока не дойдем до элемента у которого нет ссылки на нод
        while current_node.get_next_node() != None:
            current_node = current_node.get_next
        current_node.set_next_node(new_node)

# метод для того чтобы вывести список
# нужен цикл чтобы пройти по каждому элем, собрать данные и доавить их в переменную

    def show_up(self):
        current_node = self.head # тек элем = голове
        output = ""
        while current_node != None:
            output += str(current_node.get_data()) + " "
            current_node = current_node.get_next_node() #заменяем текущий нод на следующий
        print(output)

    def delete_first_element(self):
        current_node = self.head # определили первый элем
        self.head = current_node.get_next_node() # присвоили голове новое значение

    def delete_last_element(self):
        current_node = self.head  # определили первый элем
        # нужно дойти до предпоследнего элемента и удалить ссылку
        while current_node.get_next_node().get_next_node() != None:
            current_node = current_node.get_next_node() # двигаем current_node на след элем
        current_node.set_next_node(None) # задаем ссылку на None => удалили посл элем

    def delete_random(self,index):
        #поменять ссылку
        current_node = self.head
        count = 0
        while current_node.get_next_node() != None:
            if index == 0:
                self.delete_first_element()
                return
            elif count + 1 == index:
                node_to_delete = current_node.get_next_node()
                node_after_deleted = node_to_delete.get_next_node()
                current_node.set_next_node(node_after_deleted)
                return
            count += 1
            current_node = current_node.get_next_node()
        print("No such element")







l = LinkedList()
l.append(11)
l.append(18)
# l.delete_first_element()
l.delete_last_element()
l.show_up()


