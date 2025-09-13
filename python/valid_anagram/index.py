# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


class ValidAnagram:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Sort both strings and compare
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))
        
        return sorted_s == sorted_t


if __name__ == "__main__":
    valid_anagram = ValidAnagram()
    
    # Test case 1
    s1 = 'anagram'
    t1 = 'nagaram'
    print(f"Input: s='{s1}', t='{t1}'")
    print(f"Output: {valid_anagram.is_anagram(s1, t1)}")  # Output: True
    
    # Test case 2
    s2 = 'rat'
    t2 = 'car'
    print(f"Input: s='{s2}', t='{t2}'")
    print(f"Output: {valid_anagram.is_anagram(s2, t2)}")  # Output: False