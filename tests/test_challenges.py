from sample import challenges


def test_two_sum_valid():
    nums = [2, 7, 11, 15]
    target = 9
    ans = challenges.two_sum(nums, target)
    assert ans == [0,1]


def test_two_sum_empty():
    nums = []
    target = 9
    ans = challenges.two_sum(nums, target)
    assert ans == []
