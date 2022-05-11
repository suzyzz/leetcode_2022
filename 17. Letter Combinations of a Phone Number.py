# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters. 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 
# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9']

# 自己写的 DFS - 基本一样
class Solution:
    def letter_combinations(self, digits):
        if not digits:
            return []
        string = list(map(int, list(digits)))
        mapping = [[], [], ['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l'], \
                    ['m','n','o'], ['p','q','r','s'], ['t','u','v'], ['w','x','y','z']]
        combs = []
        self.dfs(string, mapping, [], combs, 0)
        return combs

    def dfs(self, string, mapping, comb, combs, level):
        if level == len(string):           
            combs.append("".join(comb))
            return 

        for letter in mapping[string[level]]:            
            comb.append(letter)
            self.dfs(string, mapping, comb, combs, level + 1)
            comb.pop()

#关答：升级了keyboard
KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        results = []
        self.dfs(digits, 0, [], results)
        
        return results
    
    def dfs(self, digits, index, chars, results):
        if index == len(digits):
            results.append(''.join(chars))
            return
        
        for letter in KEYBOARD[digits[index]]:
            chars.append(letter)
            self.dfs(digits, index + 1, chars, results)
            chars.pop()
