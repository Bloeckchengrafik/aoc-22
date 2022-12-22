from dec20 import mix, find_solution

DECRYPTION_KEY = 811589153


def stage(data: list[str]):
    ints = [int(x) for x in data]

    nums = [[0, 0]] * len(ints)  # Preallocate list of tuples for speed.

    for i, theint in enumerate(ints):
        nums[i] = [i, theint]

    working_nums = nums.copy()

    for num in working_nums:
        num[1] = num[1] * DECRYPTION_KEY

    for i in range(10):
        working_nums = mix(nums, working_nums)

    print(find_solution(working_nums))
