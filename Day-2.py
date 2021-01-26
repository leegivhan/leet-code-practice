# 1
# 1603. Design Parking System

# class ParkingSystem:
#
#     def __init__(self, big: int, medium: int, small: int):
#         self.left = [0, big, medium, small]
#
#     def addCar(self, carType: int) -> bool:
#         self.left[carType] -= 1
#
#         return self.left[carType] >= 0

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# 2
# 1720. Decode XORed Array

# class Solution:
#     def decode(self, encoded: List[int], first: int) -> List[int]:
#         # a ^ x = b
#         # a = b ^ x
#
#         ans = [first]
#         for x in encoded:
#             # the ^ means exclusive or bitwise
#             ans.append(ans[-1] ^ x)
#         return ans

# 3
# 1528. Shuffle String
# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         """:cvar
#         Given a string s and an integer array indices of the same length.
#         The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#         :Return: the shuffled string.
#         """
#         N = len(s)
#         a = [""] * N
#
#         for i, x in enumerate(indices):
#             a[x] = s[i]
#         return "".join(a)

# 4
# 1342. Number of Steps to Reduce a Number to Zero

# class Solution:
#     def numberOfSteps (self, num: int) -> int:
#         """
#         :num: non-negative integer integer,
#         :return: int - the number of steps to reduce it to zero.
#         If the current number is even, you have to divide it by 2,
#         otherwise, you have to subtract 1 from it.
#         """
#         count = 0
#         while num != 0:
#             if num % 2 == 0:
#                 num = num // 2
#             else:
#                 num -= 1
#             count += 1
#         return count

# 5
# 1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """
        :n: integer
        :return: difference between product of n's digits and sum of its digits.
        """
        # first attempt
        # digitSum = 0
        # digitProduct = 1
        # newList = str(n).split('')
        # for i in newList:
        #     digitSum += int(i)
        # for z in newList:
        #     digitSum *= z
        # return digitProduct - digitSum

        # working solution
        # nProd = 1
        # nSum = 0
        # num_as_str = str(n)
        # for i in num_as_str:
        #     nProd *= int(i)
        #     nSum += int(i)
        # return nProd - nSum

# 6
# 1313. Decompress Run-Length Encoded List
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        """
        Consider each adjacent pair of elements [freq, val] = [nums[2*i],
        nums[2*i+1]] (with i >= 0).
        For each such pair, there are freq elements
        with value val concatenated in a sublist.
        Concatenate all the sublists from left to right
        to generate the decompressed list.
        :nums: list[int]
        :return: decompressed list
        """
        # res = []
        #     i = 0
        #     while i < len(nums):
        #         for j in range(nums[i]):
        #             res.append(nums[i+1])
        #         i += 2
        #     return res

# 7
# 1389. Create Target Array in the Given Order
# first try
# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#         result = []
#         for i in nums:
#             num = nums[i]
#             idx = index[i]
#             result.splice(idx, 0, num)
#         return result

# 8
# 1486. XOR Operation in an Array
# class Solution:
#     def xorOperation(self, n: int, start: int) -> int:
#         x = 0
#
#         for y in range(n):
#             # research more what ^= does as "bitwise XOR operator." might be CS
#             x ^= (start + 2 * y)
#         return x

# 9
# 1221. Split a String in Balanced Strings

# Review more for logic on 22 min video

# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         left_cnt = 0
#         right_cnt = 0
#         out = 0
#         if len(s) == 1:
#             return 0
#         for char in s:
#             if char == 'L':
#                 left_cnt += 1
#             else:
#                 right_cnt += 1
#             if left_cnt == right_cnt:
#                 out += 1
#         return out

# faster solution
# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         cnts = {'R':0, 'L':0}
#         res = 0
#         for i in s:
#             cnts[i] += 1
#             if cnts['R'] == cnts['L']:
#                 res += 1
#                 cnts['R'] = cnts['L'] = 0
#         return res

# 10
# 1684. Count the Number of Consistent Strings

# one solution
# class Solution:
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         appearances = 0
#         sallowed = set(allowed)
#
#         for word in words:
#             if all(x in sallowed for x in word):
#                 appearances += 1
#
#         return appearances

# another solution in one line
#         return sum(all(c in allowed for c in w) for w in words)

