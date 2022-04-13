# For a given source string and a target string, you should output the first index(from 0) of target string in the source string.
# If the target does not exist in source, just return -1.

# method: Brute Force
class Solution:
    def str_str(self, source, target):
        if not target:
          return 0
        
        for i in range(len(source) - len(target) + 1):
            if source[i: i + len(target)] == target:
                return i
        return -1

# method: Brute Force optimal O(n^2)
class Solution:
    def str_str(self, source, target):
        if not target:
          return 0
        
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else: 
                return i
        return -1
      
# method: Rabin-Karp O(n) - Hash Code
class Solution:
    def str_str(self, source, target):
        if source == None or target == None:
            return -1

        size = len(target)
        if size == 0:
            return 0

        BASE = 10 ** 8

        hash_target = 0
        for t in target:
            hash_target = (hash_target * 31 + ord(t)) % BASE

        hash_source = 0
        for i in range(len(source)):
            print(i, hash_source)
            hash_source = (hash_source * 31 + ord(source[i])) % BASE

            if i < size -1: #如果substring没有目标大，不要判断下面的 继续往上加hash
                continue

            if hash_source == hash_target and source[i - size + 1: i+1] == target: #如果找到答案了直接return
                return i - size + 1 

            hash_source = (hash_source - ord(source[i-size+1]) * (31 ** (size-1)) ) % BASE #没找到就往下slide

            if hash_source < 0:
                hash_source += BASE
        return -1




