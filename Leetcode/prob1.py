# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}  # Step 1
#         for i, num in enumerate(nums):  # Step 2
#             complement = target - num  # Step 3
#             if complement in hashmap: 
#                 return [hashmap[complement], i]  
#             hashmap[num] = i  # Step 6