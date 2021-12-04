class DLNode:

    def __init__(self,val):
        self.value = val
        self.next = None
        self.prev = None

class DList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_front(self, val):
        new_node = DLNode(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return self
        else:
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
            self.length += 1
            return self


    def add_to_back(self, val):
        new_node = DLNode(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return self
        else:
            current_tail = self.tail
            new_node.prev = current_tail
            self.tail = new_node
            current_tail.next = new_node
            self.length += 1
            return self

    def print_values(self):
        if not self.head:
            raise IndexError("List is empty.")

        pointer = self.head
        while (pointer != None):
            print(pointer.value)
            pointer = pointer.next
        return self

    def remove_from_front(self):
        if self.length == 0:
            raise IndexError("List is empty.")

        result = self.head.value
        self.head = self.head.next
        self.length -= 1
        return result

    def remove_from_back(self):
        if self.length == 0:
            raise IndexError("List is empty.")

        result = self.tail.value
        self.tail = self.tail.prev
        self.length -= 1
        return result

    def remove_value(self, val):
        if self.length == 0:
            raise IndexError("List is empty.")

        if self.head.value == val:
            return self.remove_from_front()

        pointer = self.head
        while (pointer.next and pointer.next.value != val):
            pointer = pointer.next
        
        result = pointer.next.value
        pointer.next = pointer.next.next
        return result


    def insert_at(self, val, n):
        pass

    def reverse(self):
        pass


if __name__ == "__main__":
    my_list = DList()
    my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()

    my_list.remove_from_front()
    my_list.print_values()

    my_list.remove_from_back()
    my_list.print_values()

    my_list.remove_from_back()
    try:
        my_list.print_values()
    except IndexError:
        print("Oops! the list is empty now!")

    my_list.add_to_back(42)
    my_list.add_to_front("The universe: ")
    my_list.print_values()

    my_list.add_to_back("I'm a little teapot")
    my_list.remove_value(42)
    my_list.print_values()

    try:
        my_list.remove_value(42)
    except IndexError:
        print("Oops! I already took that one out!")
    my_list.print_values()

    my_list.remove_value("The universe: ")
    my_list.print_values()

    my_list.remove_value("I'm a little teapot")
    try:
        my_list.print_values()
    except IndexError:
        print("Oops! the list is empty now!")

    my_list.insert_at("I love linked lists!", 6)
    my_list.print_values()

    my_list.insert_at(22, 0)
    my_list.print_values()

    my_list.insert_at(44, 1)
    my_list.print_values()

    my_list.insert_at(33, 1)
    my_list.print_values()

    my_list.insert_at("But this one is a little far out maybe?", 12345)
    my_list.print_values()