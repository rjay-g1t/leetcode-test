# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

from typing import List


class TwoIntegerSum:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            num_a = nums[i]
            for j in range(i + 1, len(nums)):
                num_b = nums[j]
                if num_a + num_b == target:
                    result.append(i)
                    result.append(j)
                    return result  # Return immediately after finding the first pair
        return result


if __name__ == "__main__":
    two_integer_sum = TwoIntegerSum()
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: {nums}, target={target}")
    print(f"Output: {two_integer_sum.two_sum(nums, target)}")  # Output: [0, 1]
    
    # Additional test case
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: {nums2}, target={target2}")
    print(f"Output: {two_integer_sum.two_sum(nums2, target2)}")  # Output: [1, 2]