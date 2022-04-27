# Description
# Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.

# Example
# Example 1:
# 	Input:  [3, 2, 1, 4, 5]
# 	Output: [1, 2, 3, 4, 5]
	
# 	Explanation: 
# 	return the sorted array.

# Example 2:
# 	Input:  [1, 1, 2, 1, 1]
# 	Output: [1, 1, 1, 1, 2]
	
# 	Explanation: 
# 	return the sorted array.

# 十大排序算法实现 冒泡排序、选择排序、插入排序、希尔排序、归并排序、快速排序、堆排序、计数排序、桶排序、基数排序（适用于正数排序）

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        if A == None or len(A) == 0:
            return
        A.sort()
        
# Bubble Sort
class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        
        for i in range(len(A) - 1):
            for j in range(len(A) - 1 - i):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    
# Selection Sort
class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        for i in range(len(A)):
            tmp = i
            for j in range(i + 1, len(A)):
                if A[j] < A[tmp]:
                    tmp = j
            A[i], A[tmp] = A[tmp], A[i]

# Insertion Sort
class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        for i in range(1, len(A)):
            for j in range(i - 1, -1, -1):
                if A[i] < A[j]:
                    A[i], A[j] = A[j], A[i]
                    i = j
                else:
                    break


# Shell Sort
class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        dk = len(A) // 2
        while dk >= 1:
            self.InsertSort(A, dk)
            dk = dk // 2
            
    def InsertSort(self, A, dk):
        for i in range(dk):
            for j in range(i, len(A), dk):
                for k in range(j - 1, -1, -dk):
                    if A[j] < A[k]:
                        A[j], A[k] = A[k], A[j]
                        j = k
                    else:
                        break

# Merge Sort
class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        tmp = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, tmp)
        
    def mergeSort(self, A, start, end, tmp):
        if start >= end:
            return
        
        self.mergeSort(A, start, (start + end) // 2, tmp) #左边排好序
        self.mergeSort(A, (start + end) // 2 + 1, end, tmp) #右边排好序
        
        self.merge(A, start, end, tmp) #归并两边
        
    def merge(self, A, start, end, tmp):
        mid = (start + end) // 2
        leftIndex = start
        rightIndex = mid + 1
        index = leftIndex
        
        while leftIndex <= mid and rightIndex <= end:
            if A[leftIndex] <= A[rightIndex]:
                tmp[index] = A[leftIndex]
                leftIndex += 1
            else:
                tmp[index] = A[rightIndex]
                rightIndex += 1
            index += 1
            
        while leftIndex <= mid:
            tmp[index] = A[leftIndex]
            index += 1
            leftIndex += 1
        while rightIndex <= end:
            tmp[index] = A[rightIndex]
            index += 1
            rightIndex += 1
            
        for index in range(start, end + 1):
            A[index] = tmp[index]

# B = [38,27,43,3,9,82,10]	
# mergeSort start, end, tmp 0 6 [0, 0, 0, 0, 0, 0, 0]
# mergeSort start, end, tmp 0 3 [0, 0, 0, 0, 0, 0, 0]
# mergeSort start, end, tmp 0 1 [0, 0, 0, 0, 0, 0, 0]
# mergeSort start, end, tmp 0 0 [0, 0, 0, 0, 0, 0, 0]
# mergeSort start, end, tmp 1 1 [0, 0, 0, 0, 0, 0, 0]
# merge start, end, tmp 0 1 [0, 0, 0, 0, 0, 0, 0]
# mergeSort start, end, tmp 2 3 [27, 38, 0, 0, 0, 0, 0]
# mergeSort start, end, tmp 2 2 [27, 38, 0, 0, 0, 0, 0]
# mergeSort start, end, tmp 3 3 [27, 38, 0, 0, 0, 0, 0]
# merge start, end, tmp 2 3 [27, 38, 0, 0, 0, 0, 0]
# merge start, end, tmp 0 3 [27, 38, 3, 43, 0, 0, 0]
# mergeSort start, end, tmp 4 6 [3, 27, 38, 43, 0, 0, 0]
# mergeSort start, end, tmp 4 5 [3, 27, 38, 43, 0, 0, 0]
# mergeSort start, end, tmp 4 4 [3, 27, 38, 43, 0, 0, 0]
# mergeSort start, end, tmp 5 5 [3, 27, 38, 43, 0, 0, 0]
# merge start, end, tmp 4 5 [3, 27, 38, 43, 0, 0, 0]
# mergeSort start, end, tmp 6 6 [3, 27, 38, 43, 9, 82, 0]
# merge start, end, tmp 4 6 [3, 27, 38, 43, 9, 82, 0]
# merge start, end, tmp 0 6 [3, 27, 38, 43, 9, 10, 82]


# Quick Sort
class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = A[(start+end)//2] # a) / operator aka classic division b) //operator aka floor division
        print('left, right, pivot', left, right, pivot)

        while left <= right:
            while left <= right and A[left] < pivot: #找一个不应该在左边的
                left += 1
            while left <= right and A[right] > pivot: #找一个不应该在右边的
                right -= 1

            if left <= right: #如果找到了任意一个或者两个就交换
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1 #交换完各自走一步
            
        #现在左右交换了 所以是（start, right） and （left, end）
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)

	
# 这种似懂非懂的感觉很不好 下次一定还是不会

# Quicksort 的原理 = partition by pivot + Recursion
#----------------------------------------------------------------------------------------------------------  
# partition的部分：
#     循环条件为什么要用 <= 不是 <
# 
#       1. 让partition之后的片段没有重复部分
# 
#        比如 如果是 left < right [3, -3, 5, 2, 1, -6]， piovt = 5， 
#                                 0,  1, 2, 3, 4,  5       
#           现在需要swap 5， -6
#            if left < right:                            （L = 2, R = 5）
#                a[left], a[right] = a[right], a[left]    ([3, -3, -6, 2, 1, -5])
#                left += 1
#                right -= 1                              （L = 3, R = 4）
#        while left < right:                             （False 下一个循环进不去 while loop结束）
#        self.quick_sort(a, start, right)                 (start = 0, right = 4) => [3, -3, -6, 2, 1]
#        self.quick_sort(a, left, end)                    (left = 3, end = 5)    => [2, 1, -5] 2,1 ！！！！！！重复出现了！！！！！！
# 
#       正确的做法是
#            if left <= right:                            （L = 2, R = 5）
#                a[left], a[right] = a[right], a[left]     ([3, -3, -6, 2, 1, -5])
#                left += 1
#                right -= 1                               （L = 3, R = 4）
#        while left <= right:                             （True)
#            while left <= right and a[left] < pivot:     （True）
#                left += 1                                 (L = 4, R = 4）
#            while left <= right and a[right] > pivot:    （True）
#                right -= 1                               （L = 4, R = 3）
#
#            if left <= right:                            （False）
#                a[left], a[right] = a[right], a[left]
#                left += 1
#                right -= 1                              
#        self.quick_sort(a, start, right)                 (start = 0, right = 3) => [3, -3, -6, 2]
#        self.quick_sort(a, left, end)                    (left = 4, end = 5)    => [1, -5] ！！！！！！没有重复的partition！！！！！！
#----------------------------------------------------------------------------------------------------------  
#           2. 最后的 if left <= right 避免StackOverflow：
#
#        比如 如果是 left < right 走到了 [1 , 2]， piovt = 1， L=1   R=2
#                                         
#        while left < right:                            （True）
#            while left < right and a[left] < pivot:    （False）
#                left += 1                              
#            while left < right and a[right] > pivot:   （True）
#                right -= 1                             （L = 1, R = 1）
#
#            if left < right:                            (False)
#                a[left], a[right] = a[right], a[left]
#                left += 1
#                right -= 1
#         self.quick_sort(a, start, right)               (start = 1, right = 1)
#         self.quick_sort(a, left, end)                  (left = 1, end = 2) => 又来一次一样的 [1 , 2]， piovt = 1， L=1   R=2
#
#        如果是 left <= right 走到了 [1 , 2]， piovt = 1， L=1   R=2
#                                         
#        while left <= right:                            （True）
#            while left <= right and a[left] < pivot:    （False）
#                left += 1                              
#            while left <= right and a[right] > pivot:   （True）
#                right -= 1                              （L = 1, R = 1）
#
#            if left <= right:                           （True）
#                a[left], a[right] = a[right], a[left]
#                left += 1
#                right -= 1                              （L = 2, R = 0）
#         self.quick_sort(a, start, right)                (start = 1, right = 0) => return None
#         self.quick_sort(a, left, end)                   (left = 2, end = 2)    => return None



#----------------------------------------------------------------------------------------------------------  
# Recursion 的部分：
#     1. 为什么要用start，end 和 left，right这两套？
#           因为start，end是放在stack里存储partition的， left，right是在partition里做指针的
#     2. 他们在recusion的时候分别的指向是怎么传递的
#           全，左，右
#           全 => 左 => 。。。 => 直到左边走到底 （剩1，2个不能走的） 
#           => 走倒数第一层的右 => 倒数第二层右 => 。。。=> 走到第一层的右 => 再分成左右往下走
#           从上到左下 再从右下到上 再走右上到右下
#     3. 判断recursion结束条件是怎么设计的
#           走到底端 - 没有元素（start > end) 或者只有一个元素 （start = end) 这种情况不用置换 直接退出
#     4. 这个return None 系统是怎么检测到a的值咋变化的呢
#           不知道 magic吧


# Heap Sort
class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        A.insert(0, 0)

        lenA = len(A) - 1
        dk = lenA // 2
        for i in range(dk):
            self.heapAdjust(A, dk - i, lenA)

        for i in range(lenA - 1):
            A[1], A[lenA - i] = A[lenA - i], A[1]
            self.heapAdjust(A, 1, lenA - i - 1)

        A.remove(0)

    def heapAdjust(self, A, start, end):
        tmp = A[start]

        i = start
        j = 2 * i

        while j <= end:
            if j < end and A[j] < A[j + 1]:
                j += 1
            if tmp < A[j]:
                A[i] = A[j]
                i = j
                j = 2 * i
            else:
                break

        A[i] = tmp

# Counting Sort
class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        
        minA = min(A)
        maxA = max(A)

        L = [0] * (maxA - minA + 1)

        for i in range(len(A)):
            L[A[i] - minA] += 1

        index = 0
        for i in range(len(L)):
            while L[i] > 0:
                A[index] = minA + i
                index += 1
                L[i] -= 1

# Bucket Sort
class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return

        n = 100
        new_list = [[] for _ in range(n)]
        minA = min(A)

        for data in A:
            index = (data - minA) // 100
            new_list[index].append(data)

        for i in range(n):
            new_list[i].sort()

        index = 0
        for i in range(n):
            for j in range(len(new_list[i])):
                A[index] = new_list[i][j]
                index += 1

# Radix Sort
# Suitable for positive sorting
class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        
        maxA = max(A)

        d = 0
        while maxA // 10 > 0:
            d += 1
            maxA = maxA // 10
        d += 1

        for i in range(d):
            s = [[] for _ in range(10)]
            for data in A:
                s[data // (10 ** i) % 10].append(data)
            index = 0
            for j in s:
                for k in j:
                    A[index] = k
                    index += 1
