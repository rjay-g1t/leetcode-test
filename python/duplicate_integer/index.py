# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


class DuplicateInteger:
    def has_duplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    duplicate_integer = DuplicateInteger()
    nums = [1, 2, 3, 4, 5, 1]
    print(duplicate_integer.has_duplicate(nums))  # Output: True