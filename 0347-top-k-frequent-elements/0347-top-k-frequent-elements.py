import random
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        unique = list(count.keys())
        
        def quick_select(unique, k):
            pivot = random.choice(unique)
            left, mid, right = [], [], []

            for num in unique:
                if count[num] > count[pivot]:
                    left.append(num)
                elif count[num] < count[pivot]:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quick_select(left, k)

            if len(left) + len(mid) == k:
                return left + mid

            if len(left) + len(mid) < k:
                return left + mid + quick_select(right, k - len(left) - len(mid))

        return quick_select(unique, k)
