#finding the maximum depth of parenthesis in a string
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr_dep = 0
        max_dep = 0

        for ch in s:
            if ch == '(':
                curr_dep +=1
                if curr_dep > max_dep:
                    max_dep = curr_dep
            elif ch ==')':
                curr_dep -= 1

        return max_dep    