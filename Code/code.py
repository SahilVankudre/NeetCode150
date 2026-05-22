'''
Q.1) [E] Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
'''
def hasDuplicate(self, nums: list[int]) -> bool:
    seen = {}

    for i in nums:
        seen[i] = seen.get(i, 0)+1 

    for j in seen:
        if seen[j] >= 2:
            return True
    return False      

'''
Q.2) [E] Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
'''
def isAnagram(self, s: str, t: str) -> bool:
    seen1, seen2 = {}, {}

    if len(s) != len(t):
        return False

    for i in s:
        seen1[i] = seen1.get(i, 0)+1

    for j in t:
        seen2[j] = seen2.get(j, 0)+1

    if seen1 == seen2:
        return True
    
    return False

'''
Q.3) [E] Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
'''
def twoSum(self, nums: list[int], target: int) -> list[int]:
    seen = {}
    
    for i,n in enumerate(nums):
        res = target - n

        if res in seen:
            return [seen[res], i]

        seen[n] = i
    return

'''
Q.4) [M] Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

    hm = {}

    for i in strs:

        key = ''.join(sorted(i))

        if key not in hm:
            hm[key] = []

        hm[key].append(i)

    return list(hm.values())

'''
Q.5) [M] Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
'''
def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    hm = {}

    # Frequency map
    for num in nums:
        hm[num] = hm.get(num,0)+1

    # Creating buckets
    Buckets = [[] for _ in range(len(nums)+1)]

    for idx, num in hm.items():
        Buckets[num].append(idx)

    res = []

    for i in range(len(Buckets)-1, -1, -1):
        for num in Buckets[i]:
            res.append(num)
            if len(res) == k:
                return res

    return res

'''
Q.6) [M] Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}
So Machine 1 does:

String encoded_string = encode(strs);
and Machine 2 does:

List<String> decoded_strs = decode(encoded_string);
decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: strs = ["Hello","World"]

Output: ["Hello","World"]
'''


'''
Q.7) [E] Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
'''
def isPalindrome(self, s: str) -> bool:
    res = "".join(char.lower() for char in s if char.isalnum())
    l,r = 0,len(res)-1
    while l<r:
        if res[l] != res[r]:
            return False
        l += 1
        r -= 1
    return True