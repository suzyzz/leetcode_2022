# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

# 使用分层遍历的BFS版本。

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])
        
        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance
                
                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word) 

        return 0
        
    # O(26 * L^2)
    # L is the length of word
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words

       
       
# 2022-10-12 类似关答 但是慢
from typing import (
    Set,
)
import collections
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        used = {start}
        level = 1
        queue = collections.deque([start])
        while queue:            
            for _ in range(len(queue)):
                node = queue.popleft()
                for i in range(len(node)):
                    flag = self.replace_letter(node, i, queue, used, end, dict, level)
                    if flag:
                        return level + 1
            level += 1
        return 0
    
    def replace_letter(self, node, i, queue, used, end, dict, level):
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            new = node[0:i] + letter + node[i + 1:]
            if new == end:
                return True
            if new in used:
                continue
            if new in dict:
                used.add(new)
                queue.append(new)
        return False

       
#        20221121 双向BFS chatch
from typing import (
    Set,
)
import collections
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        dict.add(end)
        forward_queue = collections.deque([start])
        forward_set = {start}
        backward_queue = collections.deque([end])
        backward_set = {end}
        distance = 0
        graph = {}
        self.get_next_word(graph, dict, start)
        self.get_next_word(graph, dict, end)
        print(graph)
        while forward_queue and backward_queue:
            distance += 1
            if self.enter_queue(dict, graph, forward_queue, forward_set, backward_set):
                return distance
            distance += 1
            if self.enter_queue(dict, graph, backward_queue, backward_set, forward_set):
                return distance
        return -1
    
    def get_next_word(self, graph, dict, word):
        graph[word] = []
        for i in range(len(word)):
            for x in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == x:
                    continue
                if word[:i] + x + word[i + 1:] in dict:
                    graph[word].append(word[:i] + x + word[i + 1:])
        
    def enter_queue(self, dict, graph, current_queue, current_visited, opposite_visited):
        for _ in range(len(current_queue)):
            curr_word = current_queue.popleft()
            if curr_word in opposite_visited:
                return True
            if curr_word not in graph:
                self.get_next_word(graph, dict, curr_word)
            for next_word in graph[curr_word]:
                if next_word in current_visited:
                    continue
                current_queue.append(next_word)
                current_visited.add(next_word)
        return False
