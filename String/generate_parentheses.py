# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
#"((()))", "(()())", "(())()", "()(())", "()()()"


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []
        self.dfs(n, 0, 0 ,'', result)
        return result

    def dfs(self, n, left, right, s, result):

        if n == left and n == right:
            result.append(s)
            return

        if left == n:
            self.dfs(n, left, right+1, s+')', result)
            return
        if left == right:
            self.dfs(n, left+1, right, s+'(', result)
            return
        self.dfs(n, left+1, right, s+'(', result)
        self.dfs(n, left, right+1, s+')', result)
