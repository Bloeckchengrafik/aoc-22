from dec20 import mix, find_solution


def stage(data: list[str]):
    ints = [int(x) for x in data]

    nums = [(0, 0)] * len(ints)  # Preallocate list of tuples for speed.

    for i, theint in enumerate(ints):
        nums[i] = (i, theint)

    output = mix(nums, nums.copy())

    print(find_solution(output))

