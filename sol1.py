class Solution:
    def isCovered(self, ranges, left, right):
        numbercov = []

        for start, end in ranges:
            for i in range(start, end + 1):
                numbercov.append(i)

        for i in range(left, right + 1):
            if i not in numbercov:
                return False

        return True
