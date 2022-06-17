import Node

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head = self.tail
        self.arr = []
        return

    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def output_list_forward(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data.get_name())
            current_node = current_node.next
        return

    def output_list_backward(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data.get_name())
            current_node = current_node.previous
        return

    def unordered_search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.has_value(value):
                return value
            current_node = current_node.next

    def add_list_item(self, item):
        if isinstance(item, Node.ListNode):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
        return

    def remove_list_item_by_id(self, item_id):
        current_id = 1
        current_node = self.head

        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                return
            current_node = next_node
            current_id = current_id + 1
        return



    def sorted_insert(self, head_ref, new_node):
        if (head_ref == None):
            head_ref = new_node

        elif (head_ref.data.get_stage() >= new_node.data.get_stage()):
            new_node.next = head_ref
            new_node.next.previous = new_node
            head_ref = new_node

        else:
            current = head_ref
            # find not after what we ant to indsrt something
            while (current.next != None and current.next.data.get_stage() < new_node.data.get_stage()):
                current = current.next

            new_node.next = current.next
            #if we not find place wher we want to put node put it at the and
            if (current.next != None):
                new_node.next.previous = new_node

            current.next = new_node
            new_node.previous = current

        return head_ref

    def insertion_sort(self, head_ref):
        sorted = None
        current = head_ref
        if(head_ref.data.get_stage() > current.next.data.get_stage()):
            temp = head_ref.data
            head_ref.data = current.next.data
            current.next.data = temp

        while (current != None):
            next = current.next
            current.previous = current.next = None

            #insert this shit in list
            sorted = self.sorted_insert(sorted, current)
            current = next
        head_ref = sorted

        return head_ref



