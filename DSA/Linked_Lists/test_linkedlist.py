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
        Input: singly_linked_list.insert_at_beginning("Insert At Beginning")
        Output: ["Insert At Beginning", "Item 1", "Item 2", "Item 3", "Item 4"]
        """
        data_to_insert = "Insert At Beginning"

        singly_linked_list.insert_at_beginning(data_to_insert)
        assert singly_linked_list.head.data == data_to_insert

    def test_insert_many_at_beginning(self, singly_linked_list: ll.LinkedList):
        """
        Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.insert_at_beginning("Insert 1", "Insert 2", "Insert 3")
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
        Input: singly_linked_list.insert_at_end("Insert At End")
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
        Input: singly_linked_list.insert_at_end("Insert 1", "Insert 2", "Insert 3")
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

        Iterating over the linked list must yield same data as initial data.
        """
        for i, j in zip_longest(singly_linked_list, datas):
            assert i.data == j

    def test_length(self, singly_linked_list: LinkedList):
        """
        TEST 1
        Initial: len(singly_linked_list) == 4
        Input: len(singly_linked_list)
        Output: 4

        TEST 2
        Initial: len(singly_linked_list) == 4
        Input: singly_linked_list.insert_at_end("An Item"),
               len(singly_linked_list)
        Output: 5

        TEST 3
        Initial: len(singly_linked_list) == 4
        Input: singly_linked_list.remove_at_index(4),
               len(singly_linked_list)
        Output: 4
        """
        # TEST 1
        initial_length = 4
        assert len(singly_linked_list) == initial_length

        # TEST 2
        singly_linked_list.insert_at_end("An Item")
        assert len(singly_linked_list) == initial_length + 1

        # TEST 3
        singly_linked_list.remove_at_index(4)
        assert len(singly_linked_list) == initial_length

    def test_remove_at_index(self, singly_linked_list: LinkedList):
        """
        Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.remove_at_index(1)
        Output: ["Item 1", "Item 3", "Item 4"]
        """
        data_to_remove = "Item 2"
        singly_linked_list.remove_at_index(1)
        for i in singly_linked_list:
            # assert "Item 2" does not exist in the linked list
            assert i.data != data_to_remove

    def test_remove_at_index_exception(self, singly_linked_list: LinkedList):
        """
        TEST 1
        Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.remove_at_index(4)
        Output: Exception: IndexError

        TEST 2
        Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.remove_at_index(-5)
        Output: Exception: IndexError
        """
        # TEST 1
        with pytest.raises(IndexError):
            singly_linked_list.remove_at_index(4)

        # TEST 2
        with pytest.raises(IndexError):
            singly_linked_list.remove_at_index(-5)

    def test_getitem_by_index(self, singly_linked_list: LinkedList):
        """
        TEST 1
            Using positive index.
            Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
            Input: singly_linked_list[1]
            Output: "Item 2"
        
        TEST 2
            Using negative index.
            Initial: ["Item 1", "Item 2", "Item 3", "Item 4"]
            Input: singly_linked_list[-2]
            Output: "Item 3"
        """
        # TEST 1
        get_item_test_1 = "Item 2"
        assert singly_linked_list[1] == get_item_test_1

        # TEST 2
        get_item_test_2 = "Item 3"
        assert singly_linked_list[-2] == get_item_test_2

    def test_getitem_exceptions(self, singly_linked_list: LinkedList):
        # pylint: disable=pointless-statement
        """
        TEST 1
        Initial: len(singly_linked_list) == 4
        Input: singly_linked_list[4]
        Output: Exception: IndexError

        TEST 2
        Initial: len(singly_linked_list) == 4
        Input: singly_linked_list[-5]
        Output: Exception: IndexError
        """
        # TEST 1
        out_of_range_index_test_1 = 4
        with pytest.raises(IndexError):
            singly_linked_list[out_of_range_index_test_1]

        # TEST 2
        out_of_range_index_test_2 = -5
        with pytest.raises(IndexError):
            singly_linked_list[out_of_range_index_test_2]
