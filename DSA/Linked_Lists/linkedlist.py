# Thank you for the knowledge. https://www.youtube.com/c/codebasics
#   on the video at https://www.youtube.com/watch?v=qp8u-frRAnU&t=696s
#
# As well as https://www.geekforgeeks.org
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

    source: https://www.geeksforgeeks.org/data-structures/linked-list/
"""
from copy import deepcopy


class LinkNode:
    """
    A singly node class in a linked list.
    """

    def __init__(self, data, next_=None) -> None:
        self.data = data
        self.next = next_

    def __str__(self) -> str:
        return str(self.data)


class LinkedListIterator:
    """
    Iterator for LinkedList class.
    """

    def __init__(self, head: LinkNode):
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
    """
    A single linked list class that requires LinkNode class when adding
    data to the list.
    """

    def __init__(self) -> None:
        self.head = None

        # Using len(self) will return this length
        # Every add/removal of nodes will its value.
        self._length = 0

    def __len__(self):
        # Time Complexity of O(1) as length is incremented/decremented
        #   every time a node is added/removed.
        return self._length

    # # This is the previous len(), traversing and counting.
    # # It is a bit expensive for a simple task so I changed implementation.
    # def __len__(self):
    #     # Time Complexity of O(n) for incrementing count.
    #     count = 0
    #     node_iterable = self.head
    #     while node_iterable.next:
    #         node_iterable = node_iterable.next
    #         count += 1
    #     return count

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __str__(self):
        return f"LinkedList{[i.data for i in self]}"

    def __getitem__(self, index_or_slice):
        if isinstance(index_or_slice, slice):
            start, stop = self.__validate_slice(index_or_slice)

            new_list = LinkedList()

            if start == stop:
                return new_list

            previous_node = None

            for node_index, node in enumerate(self):

                if node_index == start:
                    new_list.head = deepcopy(node)
                    previous_node = new_list.head
                    continue

                elif node_index == stop:
                    previous_node.next = None
                    return new_list

                elif node_index == len(self) - 1:
                    return new_list

                else:
                    if previous_node:
                        deep_copy_node = deepcopy(node)
                        previous_node.next = deep_copy_node
                        previous_node = previous_node.next

        elif isinstance(index_or_slice, int):
            index_or_slice = self.__validate_index(index_or_slice)

            for node_index, node in enumerate(self):
                if node_index == index_or_slice:
                    return node.data

        else:
            raise TypeError("Use slice or int types only.")

    def __validate_slice(self, slice_):
        """Validate slice if start and/or stop is None."""
        start = slice_.start if slice_.start is not None else 0
        stop = slice_.stop if slice_.stop is not None else len(self)
        return start, stop

    def __validate_index(self, index):
        if not isinstance(index, int):
            raise TypeError("Integers only.")

        if abs(index) >= len(self):
            raise IndexError("Index out of range")

        if index < 0:
            index = index + len(self)

        return index

    def __increment_length(self):
        self._length += 1

    def __decrement_length(self):
        self._length -= 1

    def insert_at_beginning(self, *datas):
        """Insert data at the beginning. Accept multiple datas at once.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        for data in reversed(datas):
            self.head = LinkNode(data, self.head)
            self.__increment_length()

    def insert_at_end(self, *datas):
        """Append data to the end. Accept multiple datas at once.

        Time Complexity: O(n) (for traversing to last node)
        Space Complexity: O(1)
        """

        # Time Complexity is O(n) for multiple datas (for very large data
        #   insertion).
        # Create a linked list from datas.
        new_list = LinkedList()
        for i in reversed(datas):
            new_list.insert_at_beginning(i)
            self.__increment_length()

        # Time Complexity is O(n) when getting the last node.
        # Append only the head of the created linked list from
        #   datas.
        node = self.head
        # If current linked list has already a head, add the
        #   linked list from datas to the end of the current
        #   linked list.
        if node:
            while node.next:
                node = node.next
            # At the last node.
            node.next = new_list.head

        # If current linked list is empty, set the head node of
        #   the linked list from data as the current linked list's
        #   head node.
        else:
            self.head = new_list.head

    def insert_at_index(self, index: int, data):
        """Append data to the end. Accept multiple datas at once.

        Time Complexity: O(n) (for traversing to index of target node)
        Space Complexity: O(1)
        """
        last_index = len(self) - 1
        if index == 0:
            self.insert_at_beginning(data)
        elif index >= last_index:
            self.insert_at_end(data)
        else:
            new_node = LinkNode(data)
            for node_index, node in enumerate(self):
                if node_index == index:
                    previous_node.next = new_node
                    new_node.next = node
                    self.__increment_length()
                    return
                previous_node = node

    def remove_at_index(self, index: int):
        """
        Remove item at index number.

        Time Complexity: O(n) (for traversing and finding node)
        Space Complexity: O(1)
        """
        index = self.__validate_index(index)  # pylint: disable=pointless-statement

        if index == 0:
            self.head = self.head.next
            self.__decrement_length()
            return

        previous_node = None
        for node_index, node in enumerate(self):
            if node_index == index:
                previous_node.next = node.next
                self.__decrement_length()
                return
            previous_node = node

    # Recursive Method
    def print_linked_list(self):

        def traverse_print(node):
            if node is not None:
                print(node)
                traverse_print(node.next)

        if self.head is None:
            print("Empty Linked List")
        else:
            traverse_print(self.head)

    # 'While Loop' Method
    def print_linked_list2(self):
        if self.head is None:
            print("Empty Linked List")

        node_iterable = self.head
        while node_iterable:
            print(node_iterable)
            node_iterable = node_iterable.next


if __name__ == "__main__":

    a = LinkedList()

    single_linked_list = LinkedList()
    single_linked_list.insert_at_beginning("Item 1", "Item 2", "Item 3",
                                           "Item 4")
    single_linked_list.insert_at_index(4, "NEW iNSERT")
    print(single_linked_list)
    print(len(single_linked_list))
    print(len(a))