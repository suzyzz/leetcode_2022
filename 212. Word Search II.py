# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example 1:

# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:

# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []


#关答
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
class Solution:
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []

        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        result = set()
        for i in range(len(board)): #从每个开头节点开始遍历
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(board, i, j, board[i][j], word_set, prefix_set, set([(i, j)]), result, )
                
        return list(result)
        
    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set: #剪枝1： 如果prefix不对就不用再继续了
            return
        
        if word in word_set:
            result.add(word)
        
        for delta_x, delta_y in DIRECTIONS: 
            x_ = x + delta_x
            y_ = y + delta_y
            
            if not self.inside(board, x_, y_): #剪枝2： 如果出界就不用再继续了
                continue
            if (x_, y_) in visited: #剪枝3： 去重，避免绕圈
                continue
            
            visited.add((x_, y_))
            self.search(board, x_, y_, word + board[x_][y_], word_set, prefix_set, visited, result, )
            visited.remove((x_, y_))
            
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])













