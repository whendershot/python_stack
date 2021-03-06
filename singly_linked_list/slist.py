class SLNode:

    def __init__(self, val):
        self.value = val
        self.next = None


class SList:

    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        if not self.head:
            raise IndexError("List is empty.")

        pointer = self.head
        while (pointer != None):
            print(pointer.value)
            pointer = pointer.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        else:
            new_node = SLNode(val)
            pointer = self.head
            while (pointer.next != None):
                pointer = pointer.next
            pointer.next = new_node
        return self

    def remove_from_front(self):
        if not self.head:
            raise IndexError("List is empty.")
        
        result = self.head.value
        self.head = self.head.next
        return result

    def remove_from_back(self):
        if not self.head:
            raise IndexError("List is empty.")
        
        result = None
        if self.head.next:
            pointer = self.head
            while (pointer.next.next != None):
                pointer = pointer.next
            result = pointer.next.value
            pointer.next = None
        #I am a single node in the list
        else: 
            result = self.remove_from_front()
        
        return result

    def remove_value(self, val):
        if not self.head:
            raise IndexError("List is empty.")

        if self.head.value == val:
            return self.remove_from_front()

        pointer = self.head
        while (pointer.next and pointer.next.value != val):
            pointer = pointer.next

        if pointer.next:
            result = pointer.next.value
            pointer.next = pointer.next.next
            return result        
        raise IndexError(f"Value ({val}) does not exist in the list.")

    def insert_at(self, val, n):
        if n < 0:
            raise IndexError("n must be 0 or a positive integer.")

        if not self.head or n == 0:
            self.add_to_front(val)
        else:
            pointer = self.head
            n -= 1
            while pointer.next and n > 0:
                n -= 1
                pointer = pointer.next
            new_node = SLNode(val)
            new_node.next = pointer.next
            pointer.next = new_node

if __name__ == "__main__":
    my_list = SList()
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