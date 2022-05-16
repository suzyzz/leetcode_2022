# Description
# You are playing the following game with your friend: There is a pile of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove stones.

# Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones.

# For example, if there are 4 stones, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

# Example
# Example 1：

# Input：n = 4 
# Output：False
# Explanation：Take 1, 2 or 3 first, the other party will take the last one
# Example 2：

# Input：n = 5 
# Output：True
# Explanation：Take 1 first，Than，we can win the game

#Method 1: Memo - MLE
class Solution:
    def can_win_bash(self, n: int) -> bool:
        return self.memo_search(n, {})
    
    def memo_search(self, n, memo):
        if n <= 3:
            return True
        if n in memo:
            return memo[n]
        for i in range(1,4):
            if not self.memo_search(n - i, memo): 
                memo[n] = True #如果n-i失败了， n一定可以胜出，记录在本子上
                return True #返回给前一层
        memo[n] = False
        return False
      
      
#Method: simple      
class Solution:
    def can_win_bash(self, n):
        return n % 4 != 0
