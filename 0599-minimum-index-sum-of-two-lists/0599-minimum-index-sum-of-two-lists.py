class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_dict = {}
        mapping = {}
        min_index_sum = float('inf')
        
        for i, n in enumerate(list1):
            list1_dict[n] = i
        
        for i, n in enumerate(list2):
            if n in list1_dict:
                curr_sum = i + list1_dict[n]
                min_index_sum = min(min_index_sum, curr_sum)
                if curr_sum in mapping:
                    mapping[curr_sum].append(n)
                else:
                    mapping[curr_sum] = [n]
        
        return mapping[min_index_sum]