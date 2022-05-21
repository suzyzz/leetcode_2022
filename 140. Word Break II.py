# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:

# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:

# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
 
# Constraints:

# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

# Method 1: DFS
class Solution:
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})
    
    # 找到 s 的所有切割方案并 return
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
            
        if len(s) == 0:
            return []
            
        partitions = []
        
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)
                
        if s in wordDict:
            partitions.append(s)
            
        memo[s] = partitions
        return partitions

# Method 1 short version:
class Solution:
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})
        
    def dfs(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []
        res = []
        if s in wordDict: res.append(s)
        for i in range(1, len(s)+1):
            if s[:i] not in wordDict: continue
            for sg in self.dfs(s[i:], wordDict, memo):
                res.append(s[:i] + ' ' + sg)
        memo[s] = res
        return res
       
# Method 2: DP*2
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        if not wordDict:
            return []

        results = []
        max_len = len(max(wordDict, key=len))
        memo = {}
        self.is_possible(s, wordDict, 0, max_len, memo)
        print(memo.items())
        self.dfs(s, wordDict, 0, max_len, [], results, memo)
        return results

    def dfs(self, s, wordDict, start, max_len, comb, results, memo):
        if start == len(s):
            results.append(" ".join(comb))
            return

        if memo[start] is False:
            return

        for end in range(start, len(s)):
            if end + 1 - start > max_len:
                break 
            
            word = s[start: end + 1]
            if word not in wordDict:
                continue
            comb.append(word)
            self.dfs(s, wordDict, end + 1, max_len, comb, results, memo)
            comb.pop()

    def is_possible(self, s, wordDict, start, max_len, memo):
        if start in memo:
            return memo[start]
        
        if start == len(s):
            memo[start] = True
            return True

        for end in range(start, len(s)):
            if end + 1 - start > max_len:
                break
            
            word = s[start: end + 1]
            if word not in wordDict:
                continue
            if self.is_possible(s, wordDict, end + 1, max_len, memo):
                memo[start] = True
                
        if start not in memo: 
            memo[start] = False
        return memo[start]
