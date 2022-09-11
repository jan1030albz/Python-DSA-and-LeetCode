"""Tests for singly linked lists"""
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
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.insert_at_beginning("Insert At Beginning")
        Output: LinkedList["Insert At Beginning", "Item 1", "Item 2", "Item 3", "Item 4"]
        """
        data_to_insert = "Insert At Beginning"

        singly_linked_list.insert_at_beginning(data_to_insert)
        assert singly_linked_list.head.data == data_to_insert

    def test_insert_many_at_beginning(self, singly_linked_list: ll.LinkedList):
        """
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.insert_at_beginning("Insert 1", "Insert 2", "Insert 3")
        Output: LinkedList["Insert 1", "Insert 2", "Insert 3", "Item 1", "Item 2", "Item 3", "Item 4"]
        """
        datas_to_insert = ["Insert 1", "Insert 2", "Insert 3"]

        singly_linked_list.insert_at_beginning(*datas_to_insert)
        assert singly_linked_list.head.data == datas_to_insert[0]
        assert singly_linked_list.head.next.data == datas_to_insert[1]
        assert singly_linked_list.head.next.next.data == datas_to_insert[2]

    def test_insert_one_at_end(self, singly_linked_list: ll.LinkedList):
        """
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.insert_at_end("Insert At End")
        Output: LinkedList["Item 1", "Item 2", "Item 3", "Item 4", "Insert At End"]
        """
        data = "Insert At End"
        singly_linked_list.insert_at_end(data)

        for i in singly_linked_list:
            last = i

        assert last.data == data

    def test_insert_many_at_end(self, singly_linked_list: ll.LinkedList):
        """
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.insert_at_end("Insert 1", "Insert 2", "Insert 3")
        Output: LinkedList["Item 1", "Item 2", "Item 3", "Item 4", "Insert 1", "Insert 2", "Insert 3"]
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

        TEST 4
        Initial: len(singly_linked_list) == 4
        Input: singly_linked_list.insert_at_beginning("An Item"),
               len(singly_linked_list)
        Output: 5

        TEST 5
        Initial: len(singly_linked_list) == 4
        Input: singly_linked_list.remove_at_index(0),
               len(singly_linked_list)
        Output: 4

        TEST 6
        Initial: len(singly_linked_list) == 4
        Input: singly_linked_list.insert_at_index(2, "An Item"),
               len(singly_linked_list)
        Output: 5

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

        # TEST 4
        singly_linked_list.insert_at_beginning("An Item")
        assert len(singly_linked_list) == initial_length + 1

        # TEST 5
        singly_linked_list.remove_at_index(0)
        assert len(singly_linked_list) == initial_length

        # TEST 6
        singly_linked_list.insert_at_index(2, "An Item")
        assert len(singly_linked_list) == initial_length + 1

    def test_remove_at_index(self, singly_linked_list: LinkedList):
        """
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.remove_at_index(1)
        Output: LinkedList["Item 1", "Item 3", "Item 4"]
        """
        data_to_remove = "Item 2"
        singly_linked_list.remove_at_index(1)
        for i in singly_linked_list:
            # assert "Item 2" does not exist in the linked list
            assert i.data != data_to_remove

    def test_remove_at_index_exceptions(self, singly_linked_list: LinkedList):
        """
        TEST 1
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.remove_at_index(4)
        Output: Exception: IndexError

        TEST 2
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
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
            Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
            Input: singly_linked_list[1]
            Output: "Item 2"

        TEST 2
            Using negative index.
            Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
            Input: singly_linked_list[-2]
            Output: "Item 3"
        """
        # TEST 1
        get_item_test_1 = "Item 2"
        assert singly_linked_list[1] == get_item_test_1

        # TEST 2
        get_item_test_2 = "Item 3"
        assert singly_linked_list[-2] == get_item_test_2

    def test_getitem_by_index_exceptions(self, singly_linked_list: LinkedList):
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

    def test_slice_linked_list(self, singly_linked_list: LinkedList):
        """
        TEST 1
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list[1:3]
        Output: LinkedList["Item 2", "Item 3"]

        TEST 2
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list[0:2]
        Output: LinkedList["Item 1", "Item 2"]
        
        TEST 3
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list[:2]
        Output: LinkedList["Item 1", "Item 2"]

        TEST 4
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list[2:]
        Output: LinkedList["Item 1", "Item 2"]
        """
        # TEST 1 - If slice start and stop is between 0 and length of linked list.
        linkedlist_data_test_1 = ["Item 2", "Item 3"]
        assert [i.data
                for i in singly_linked_list[1:3]] == linkedlist_data_test_1

        # TEST 2 - If slice stop is within length of linked list.
        linkedlist_data_test_2 = ["Item 1", "Item 2"]
        assert [i.data
                for i in singly_linked_list[0:2]] == linkedlist_data_test_2

        # TEST 3 - If slice start is not passed.
        linkedlist_data_test_3 = ["Item 1", "Item 2"]
        assert [i.data
                for i in singly_linked_list[:2]] == linkedlist_data_test_3

        # TEST 4 - If slice stop is not passed.
        linkedlist_data_test_4 = ["Item 3", "Item 4"]
        assert [i.data
                for i in singly_linked_list[2:]] == linkedlist_data_test_4

    def test_slice_linked_list_2(self, singly_linked_list: LinkedList, datas):
        """
        TEST 5
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list[0:4]
        Output: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]

        TEST 6
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list[0:5]
        Output: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]

        TEST 7
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list[:]
        Output: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]

        TEST 8
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list[0:0]
        Output: LinkedList[]
        """

        # TEST 5 - If explicit slice start = 0 and stop = length of linked list.
        assert [i.data for i in singly_linked_list[0:4]] == datas

        # TEST 6 - If explicit slice start = 0 and stop > length of linked list.
        assert [i.data for i in singly_linked_list[0:5]] == datas

        # TEST 7 - If explicit slice start = 0 and stop > length of linked list.
        assert [i.data for i in singly_linked_list[:]] == datas

        # TEST 8 - If explicit slice start = 0 and stop > length of linked list.
        assert [i.data for i in singly_linked_list[0:0]] == []

    def test_insert_at_index(self, singly_linked_list: ll.LinkedList):
        """
        TEST 1
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.insert_at_index(0, "Inserted Item")
        Output: LinkedList["Inserted Item", "Item 1", "Item 2", "Item 3", "Item 4"]

        TEST 2
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.insert_at_index(4, "Inserted Item")
        Output: LinkedList["Item 1", "Item 2", "Item 3", "Item 4", "Inserted Item"]

        TEST 3
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.insert_at_index(5, "Inserted Item")
        Output: LinkedList["Item 1", "Item 2", "Item 3", "Item 4", "Inserted Item"]

        TEST 4
        Initial: LinkedList["Item 1", "Item 2", "Item 3", "Item 4"]
        Input: singly_linked_list.insert_at_index(2, "Inserted Item")
        Output: LinkedList["Item 1", "Item 2", "Inserted Item", "Item 3", "Item 4"]
        """
        data_to_insert = "Inserted Item"

        # TEST 1 - If inserted at index 0 (beginning).
        singly_linked_list.insert_at_index(0, data_to_insert)
        assert singly_linked_list[0] == data_to_insert
        singly_linked_list.remove_at_index(0)

        # TEST 2 - If inserted at index 4 (last).
        singly_linked_list.insert_at_index(4, data_to_insert)
        assert singly_linked_list[4] == data_to_insert
        singly_linked_list.remove_at_index(4)

        # TEST 3 - If inserted at index 5 (greater than length of linked list).
        singly_linked_list.insert_at_index(5, data_to_insert)
        assert singly_linked_list[4] == data_to_insert
        singly_linked_list.remove_at_index(4)

        # TEST 3 - If inserted at index 5 (greater than length of linked list).
        singly_linked_list.insert_at_index(2, data_to_insert)
        assert singly_linked_list[2] == data_to_insert
        singly_linked_list.remove_at_index(2)
