# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses
# substring is "()()", which has length = 4.


class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        max = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                j = i - dp[i-1] -1
                if j>=0 and s[j] == '(':
                    dp[i] = dp[i-1] + 2
                    if j-1 >= 0:
                        dp[i] += dp[j-1]
            if max < dp[i]:
                max = dp[i]

        return max


