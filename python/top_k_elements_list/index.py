# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

from collections import Counter
from typing import List


class TopKElementsList:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        # Sort by frequency in descending order and get the keys
        sorted_items = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
        
        # Return the first k elements
        return [item[0] for item in sorted_items[:k]]


if __name__ == "__main__":
    top_k_elements = TopKElementsList()
    
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Input: {nums1}, k={k1}")
    print(f"Output: {top_k_elements.top_k_frequent(nums1, k1)}")  # Output: [1, 2]
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    print(f"Input: {nums2}, k={k2}")
    print(f"Output: {top_k_elements.top_k_frequent(nums2, k2)}")  # Output: [1]