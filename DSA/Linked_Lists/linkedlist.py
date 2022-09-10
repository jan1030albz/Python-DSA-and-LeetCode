"""
Definition: Like arrays, Linked List is a linear data structure. Unlike
    arrays, linked list elements are not stored at a contiguous location;
    the elements are linked using pointers. They include a series of connected
    nodes. Here, each node stores the data and the address of the next node.

Advantages:
    - Dynamic Array.
    - Ease of Insertion/Deletion.

Disadvantages:
    - Random access is not allowed. We have to access elements sequentially
        starting from the first node(head node). So we cannot do a binary
        search with linked lists efficiently with its default implementation.
    - Extra memory space for a pointer is required with each element of the
        list.
    - Not cache friendly. Since array elements are contiguous locations, there
        is locality of reference which is not there in case of linked lists.
"""


class LinkNode:
    """A singly node class in a linked list."""

    def __init__(self, data, next_=None) -> None:
        self.data = data
        self.next = next_

    def __str__(self) -> str:
        return str(self.data)


class LinkedListIterator:
    """Iterator for LinkedList class."""

    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current
            self.current = self.current.next
            return item


class LinkedList:
    """A single linked list class that requires LinkNode class when adding
    data to the list.
    """

    def __init__(self) -> None:
        self.head = None
        self._current = self.head

    def __len__(self):
        count = 0
        node_iterable = self.head
        while node_iterable.next:
            node_iterable = node_iterable.next
            count += 1
        return count

    def __iter__(self):
        return LinkedListIterator(self.head)

    def insert_at_beginning(self, *datas):
        for data in reversed(datas):
            self.head = LinkNode(data, self.head)

    def insert_at_end(self, *datas):
        new_list = LinkedList()
        for i in reversed(datas):
            new_list.insert_at_beginning(i)

        node = self.head
        if node:
            while node.next:
                node = node.next
            node.next = new_list.head
        else:
            self.head = new_list.head

    # Recursive method
    def print_linked_list(self):

        def traverse_print(node):
            if node is not None:
                print(node)
                traverse_print(node.next)

        if self.head is None:
            print("Empty Linked List")
        else:
            traverse_print(self.head)

    # While Loop
    def print_linked_list2(self):
        if self.head is None:
            print("Empty Linked List")

        node_iterable = self.head
        while node_iterable:
            print(node_iterable)
            node_iterable = node_iterable.next


if __name__ == "__main__":

    single_linked_list = LinkedList()

    single_linked_list.insert_at_beginning("START")
    single_linked_list.insert_at_end("APPENDED2", 1, 2, 3)
    single_linked_list.print_linked_list()
