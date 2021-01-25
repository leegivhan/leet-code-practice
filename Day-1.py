# 1
# 771. Jewels and Stones
# def numJewelsInStones(jewels, stones):
#     same = 0
#     for letter in jewels:
#         for letter2 in stones:
#             if letter == letter2:
#                 same += 1
#     return same

# def numJewelsInStones(jewels, stones):
#     same = 0
#     for letter in stones:
#         if letter in jewels:
#             same += 1
#     return same
#
# print(numJewelsInStones("aA", "aAAbbbb"))

# 2
# 202. Happy Number
#  Need to spend more time understanding this

# def isHappy(n):
#     visit = set()
#
#     while n not in visit:
#         visit.add(n)
#         n = sumOfSquares(n)
#
#         if n == 1:
#             return True
#     return False
#
# def sumOfSquares(n):
#     output = 0
#
#     while n:
#         digit = n % 10
#         digit = digit ** 2
#         output += digit
#         n = n // 10
#     return output
#
# print(isHappy(34))
# 3
# 141. Linked List Cycle
# Need to spend more time understanding this

# def hasCycle(head):
#     if head is None:
#         return False
#
#     ptr = head
#     fastPtr = head.next
#
#     while ptr is not None and fastPtr is not None and fastPtr.next is not None:
#         if ptr == fastPtr:
#             return True
#         ptr = ptr.next
#         fastPtr = fastPtr.next.next
#
#     return False
# print(hasCycle([3,2,0,-4]))
# 4
# 155. Min Stack

# class MinStack:

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #
    # def push(self, x: int) -> None:
    #
    # def pop(self) -> None:
    #
    # def top(self) -> int:
    #
    # def getMin(self) -> int:

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 5
# 1603. Design Parking System



# 6
# 1528. Shuffle String

# Input: s = "aiohn", indices = [3,1,4,2,0]
# Output: "nihao"
# need more time on this, too.

# def restoreString(s, indices):
#     N = len(s)
#     a = [""] * N
#
#     for i, x in enumerate(indices):
#         a[x] = s[i]
#     return "".join(a)
#
# print(restoreString('aiohn', [3,1,4,2,0]))

# 7
# 1365. How Many Numbers Are Smaller Than the Current Number
# def smallerNumbersThanCurrent(nums):
#     newList = []
#     numSmaller = 0
#     for i in nums:
#         for j in nums:
#             if i > j:
#                 numSmaller += 1
#         newList.append(numSmaller)
#         numSmaller = 0
#     return newList
#
# print(smallerNumbersThanCurrent([8,1,2,2,3]))
#expected output = [4,0,1,1,3]
# 8
# 1678. Goal Parser Interpretation

# G -> G
# () -> o
# (al) -> al

# class Solution:
#     def interpret(self, command: str) -> str:
#         return command.replace("()", "o").replace("(al)", "al")
#
# s = Solution()
# print(s.interpret("G()(al)"))
# Input: "G()(al)"
# Expected output: "Goal"

# 9
# 1720. Decode XORed Array



# 10
# 1684. Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        appearances = 0
        sallowed = set(allowed)

        for word in words:
            if all(x in sallowed for x in word):
                appearances += 1

        return appearances