# You are given an integer array nums of length n where nums is a permutation of the integers in the range [1, n]. You are also given a 2D integer array sequences where sequences[i] is a subsequence of nums.

# Check if nums is the shortest possible and the only supersequence. The shortest supersequence is a sequence with the shortest length and has all sequences[i] as subsequences. There could be multiple valid supersequences for the given array sequences.

# For example, for sequences = [[1,2],[1,3]], there are two shortest supersequences, [1,2,3] and [1,3,2].
# While for sequences = [[1,2],[1,3],[1,2,3]], the only shortest supersequence possible is [1,2,3]. [1,2,3,4] is a possible supersequence but not the shortest.
# Return true if nums is the only shortest supersequence for sequences, or false otherwise.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 
# Example 1:

# Input: nums = [1,2,3], sequences = [[1,2],[1,3]]
# Output: false
# Explanation: There are two possible supersequences: [1,2,3] and [1,3,2].
# The sequence [1,2] is a subsequence of both: [1,2,3] and [1,3,2].
# The sequence [1,3] is a subsequence of both: [1,2,3] and [1,3,2].
# Since nums is not the only shortest supersequence, we return false.
# Example 2:

# Input: nums = [1,2,3], sequences = [[1,2]]
# Output: false
# Explanation: The shortest possible supersequence is [1,2].
# The sequence [1,2] is a subsequence of it: [1,2].
# Since nums is not the shortest supersequence, we return false.
# Example 3:

# Input: nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
# Output: true
# Explanation: The shortest possible supersequence is [1,2,3].
# The sequence [1,2] is a subsequence of it: [1,2,3].
# The sequence [1,3] is a subsequence of it: [1,2,3].
# The sequence [2,3] is a subsequence of it: [1,2,3].
# Since nums is the only shortest supersequence, we return true.

# BFS- topo 自己写对
import collections
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph, in_degree = self.get_graph_in_degree(seqs)
        order = []

        queue = collections.deque([])
        for key, val in in_degree.items():
            if val == 0:
                queue.append(key)
                if len(queue) > 1:
                    return False

        while queue:
            curr = queue.popleft()
            order.append(curr)
            for j in graph[curr]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
                    if len(queue) > 1:
                        return False

        return True if order == org else False

    def get_graph_in_degree(self, seqs):
        graph, in_degree = {}, {}
        for seq in seqs:
            for i in range(len(seq)):
                if i == 0:
                    in_degree[seq[i]] = in_degree.get(seq[i], 0)
                else:
                    in_degree[seq[i]] = in_degree.get(seq[i], 0) + 1
                    
                if seq[i] not in graph and i < len(seq) - 1:
                    graph[seq[i]] = [seq[i + 1]]
                elif seq[i] not in graph and i == len(seq) - 1:
                    graph[seq[i]] = []
                elif i < len(seq) - 1:
                    new = graph[seq[i]]
                    new.append(seq[i + 1])
                    graph[seq[i]] = new
        return graph, in_degree
