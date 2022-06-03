import Node
import DoubleLinkedList
import Person
node1 = Node.ListNode(Person.Person("Karl1", "LOLI", "LOLI_Boss", "2013", 5))
node2 = Node.ListNode(Person.Person("Karl3", "LOLI", "LOLI_Boss", "2013", 1))
node3 = Node.ListNode(Person.Person("Karl2", "LOLI", "LOLI_Boss", "2013", 3))
node4 = Node.ListNode(Person.Person("Karl4", "LOLI", "LOLI_Boss", "2013", 6))
node5 = Node.ListNode(Person.Person("Karl5", "LOLI", "LOLI_Boss", "2013", 2))
track = DoubleLinkedList.DoubleLinkedList()
for current_node in [node1, node2, node3, node4, node5]:
    track.add_list_item(current_node)

print(track.unordered_search("Karl1"))
# print(track.list_length())
#track.output_list_forward()
# head = track.insertionSort(track.head)
# track.remove_list_item_by_id(4)
# print("--------")
# track.output_list_forward()