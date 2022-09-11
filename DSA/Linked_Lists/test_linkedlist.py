from itertools import zip_longest
import pytest

from linkedlist import LinkedList

import linkedlist as ll


class TestSinglyLinkedList:
    """Tests for use of class LinkedList (singly)."""

    @pytest.fixture
    def datas(self):
        datas = ["Item 1", "Item 2", "Item 3", "Item 4"]
        return datas

    @pytest.fixture
    def singly_linked_list(self, datas):
        linked_list = ll.LinkedList()

        for item in datas:
            linked_list.insert_at_end(item)
        return linked_list

    def test_insert_one_at_beginning(self, singly_linked_list: ll.LinkedList):
        """
        Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: "Insert At Beginning"
        Output: ["Insert At Beginning", "Item 1", "Item 2", "Item 3", "Item 4"]
        """
        data_to_insert = "Insert At Beginning"

        singly_linked_list.insert_at_beginning(data_to_insert)
        assert singly_linked_list.head.data == data_to_insert

    def test_insert_many_at_beginning(self, singly_linked_list: ll.LinkedList):
        """
        Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: ["Insert 1", "Insert 2", "Insert 3"]
        Output: ["Insert 1", "Insert 2", "Insert 3", "Item 1", "Item 2", "Item 3", "Item 4"]
        """
        datas_to_insert = ["Insert 1", "Insert 2", "Insert 3"]

        singly_linked_list.insert_at_beginning(*datas_to_insert)
        assert singly_linked_list.head.data == datas_to_insert[0]
        assert singly_linked_list.head.next.data == datas_to_insert[1]
        assert singly_linked_list.head.next.next.data == datas_to_insert[2]

    def test_insert_one_at_end(self, singly_linked_list: ll.LinkedList):
        """
        Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: "Insert At End"
        Output: ["Item 1", "Item 2", "Item 3", "Item 4", "Insert At End"]
        """
        data = "Insert At End"
        singly_linked_list.insert_at_end(data)

        for i in singly_linked_list:
            last = i

        assert last.data == data

    def test_insert_many_at_end(self, singly_linked_list: ll.LinkedList):
        """
        Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: ["Insert 1", "Insert 2", "Insert 3"]
        Output: ["Item 1", "Item 2", "Item 3", "Item 4", "Insert 1", "Insert 2", "Insert 3"]
        """
        datas_to_insert = ["Insert 1", "Insert 2", "Insert 3"]

        for i in singly_linked_list:
            current_last = i

        singly_linked_list.insert_at_end(*datas_to_insert)

        assert current_last.next.data == datas_to_insert[0]
        assert current_last.next.next.data == datas_to_insert[1]
        assert current_last.next.next.next.data == datas_to_insert[2]

    def test_iterate_over_items(self, singly_linked_list: ll.LinkedList,
                                datas):
        """
        Test the 'for loop'. LinkedList class has it own iterator class.

        With initial data:
            datas = ["Item 1", "Item 2", "Item 3", "Item 4"]

        Iterating over the linked list must yield same data.
        """
        for i, j in zip_longest(singly_linked_list, datas):
            assert i.data == j

    def test_remove_at_node(self, singly_linked_list: LinkedList):
        """
        Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: Remove "Item 2" at index 1
        Output: ["Item 1", "Item 3", "Item 4"]
        """
        data_to_remove = "Item 2"
        singly_linked_list.remove_at_index(1)
        for i in singly_linked_list:
            # assert "Item 2" does not exist in the linked list
            assert i.data != data_to_remove