'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

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
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

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
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

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
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

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
Given an integer array nums and an integer k, return the k most frequent elements within the array.

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
'''