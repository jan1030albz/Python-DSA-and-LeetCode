from twosum import bf_two_sum, nr_two_sum, hm_two_sum, bs_two_sum


class TestBFTwoSum:

    def test_base_case(self):
        assert bf_two_sum([1, 2, 3], 4) == [0, 2]

    def test_order_case(self):
        assert bf_two_sum([1, 2, 3], 4) == [0, 2]
        assert bf_two_sum([1, 3, 2], 4) == [0, 1]
        assert bf_two_sum([2, 1, 3], 4) == [1, 2]
        assert bf_two_sum([2, 3, 1], 4) == [1, 2]
        assert bf_two_sum([3, 1, 2], 4) == [0, 1]
        assert bf_two_sum([3, 2, 1], 4) == [0, 2]

    def test_duplicate_case(self):
        assert bf_two_sum([1, 2, 2], 4) == [1, 2]
        assert bf_two_sum([2, 1, 2], 4) == [0, 2]
        assert bf_two_sum([2, 2, 1], 4) == [0, 1]
        assert bf_two_sum([1, 2, 2, 2], 4) == [1, 2]
        assert bf_two_sum([2, 1, 2, 2], 4) == [0, 2]
        assert bf_two_sum([2, 2, 1, 2], 4) == [0, 1]
        assert bf_two_sum([2, 2, 2, 1], 4) == [0, 1]

    def test_multiple_solutions(self):
        assert bf_two_sum([2, 1, 3, 4, 5], 7) == [0, 4]

    def test_single_element(self):
        assert bf_two_sum([1, 2, 3, 4, 5], 2) != [0, 0]
        assert bf_two_sum([1, 2, 3, 4, 5], 4) != [1, 1]
        assert bf_two_sum([1, 2, 3, 4, 5], 2) != [1]

    def test_no_solution(self):
        assert bf_two_sum([1, 2, 3, 4, 5], 10) is None

class TestNRTwoSum:
    def test_base_case(self):
        assert nr_two_sum([1, 2, 3], 4) == [0, 2]

    def test_order_case(self):
        assert nr_two_sum([1, 2, 3], 4) == [0, 2]
        assert nr_two_sum([1, 3, 2], 4) == [0, 1]
        assert nr_two_sum([2, 1, 3], 4) == [1, 2]
        assert nr_two_sum([2, 3, 1], 4) == [1, 2]
        assert nr_two_sum([3, 1, 2], 4) == [0, 1]
        assert nr_two_sum([3, 2, 1], 4) == [0, 2]

    def test_duplicate_case(self):
        assert nr_two_sum([1, 2, 2], 4) == [1, 2]
        assert nr_two_sum([2, 1, 2], 4) == [0, 2]
        assert nr_two_sum([2, 2, 1], 4) == [0, 1]
        assert nr_two_sum([1, 2, 2, 2], 4) == [1, 2]
        assert nr_two_sum([2, 1, 2, 2], 4) == [0, 2]
        assert nr_two_sum([2, 2, 1, 2], 4) == [0, 1]
        assert nr_two_sum([2, 2, 2, 1], 4) == [0, 1]

    def test_multiple_solutions(self):
        assert nr_two_sum([2, 1, 3, 4, 5], 7) == [0, 4]

    def test_single_element(self):
        assert nr_two_sum([1, 2, 3, 4, 5], 2) != [0, 0]
        assert nr_two_sum([1, 2, 3, 4, 5], 4) != [1, 1]
        assert nr_two_sum([1, 2, 3, 4, 5], 2) != [1]

    def test_no_solution(self):
        assert nr_two_sum([1, 2, 3, 4, 5], 10) is None
        

class TestHMTwoSum:
    def test_base_case(self):
        assert hm_two_sum([1, 2, 3], 4) == [2, 0]

    def test_order_case(self):
        assert hm_two_sum([1, 2, 3], 4) == [2, 0]
        assert hm_two_sum([1, 3, 2], 4) == [1, 0]
        assert hm_two_sum([2, 1, 3], 4) == [2, 1]
        assert hm_two_sum([2, 3, 1], 4) == [2, 1]
        assert hm_two_sum([3, 1, 2], 4) == [1, 0]
        assert hm_two_sum([3, 2, 1], 4) == [2, 0]

    def test_duplicate_case(self):
        assert hm_two_sum([1, 2, 2], 4) == [2, 1]
        assert hm_two_sum([2, 1, 2], 4) == [2, 0]
        assert hm_two_sum([2, 2, 1], 4) == [1, 0]
        assert hm_two_sum([1, 2, 2, 2], 4) == [2, 1]
        assert hm_two_sum([2, 1, 2, 2], 4) == [2, 0]
        assert hm_two_sum([2, 2, 1, 2], 4) == [1, 0]
        assert hm_two_sum([2, 2, 2, 1], 4) == [1, 0]

    def test_multiple_solutions(self):
        assert hm_two_sum([2, 1, 3, 4, 5], 7) == [3, 2]

    def test_single_element(self):
        assert hm_two_sum([1, 2, 3, 4, 5], 2) != [0, 0]
        assert hm_two_sum([1, 2, 3, 4, 5], 4) != [1, 1]
        assert hm_two_sum([1, 2, 3, 4, 5], 2) != [1]

    def test_no_solution(self):
        assert hm_two_sum([1, 2, 3, 4, 5], 10) is None


class TestBSTwoSum:
    def test_base_case(self):
        assert bs_two_sum([1, 2, 3], 4) == [0, 2]

    def test_order_case(self):
        assert bs_two_sum([1, 2, 3], 4) == [0, 2]
        assert bs_two_sum([1, 3, 2], 4) == [0, 1]
        assert bs_two_sum([2, 1, 3], 4) == [1, 2]
        assert bs_two_sum([2, 3, 1], 4) == [2, 1]
        assert bs_two_sum([3, 1, 2], 4) == [0, 1]
        assert bs_two_sum([3, 2, 1], 4) == [0, 2]

    def test_duplicate_case(self):
        assert bs_two_sum([1, 2, 2], 4) == [1, 2]
        assert bs_two_sum([2, 1, 2], 4) == [0, 2]
        assert bs_two_sum([2, 2, 1], 4) == [0, 1]
        assert bs_two_sum([1, 2, 2, 2], 4) == [1, 2]
        assert bs_two_sum([2, 1, 2, 2], 4) == [0, 2]
        assert bs_two_sum([2, 2, 1, 2], 4) == [0, 1]
        assert bs_two_sum([2, 2, 2, 1], 4) == [0, 1]

    def test_multiple_solutions(self):
        assert bs_two_sum([2, 1, 3, 4, 5], 7) == [0, 4]

    def test_single_element(self):
        assert bs_two_sum([1, 2, 3, 4, 5], 2) != [0, 0]
        assert bs_two_sum([1, 2, 3, 4, 5], 4) != [1, 1]
        assert bs_two_sum([1, 2, 3, 4, 5], 2) != [1]

    def test_no_solution(self):
        assert bs_two_sum([1, 2, 3, 4, 5], 10) is None