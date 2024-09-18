class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_dict = {}
        mapping = {}
        least_index_sum = float('inf')

        for i, restaurant in enumerate(list1):
            list1_dict[restaurant] = i
        
        for i, restaurant in enumerate(list2):
            if restaurant in list1_dict:
                diff = abs(list1_dict[restaurant] + i)
                least_index_sum = min(least_index_sum, diff)
                if diff in mapping:
                    mapping[diff].append(restaurant)
                else:
                    mapping[diff] = [restaurant]
        
        return mapping[least_index_sum]