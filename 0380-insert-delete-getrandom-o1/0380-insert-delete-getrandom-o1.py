class RandomizedSet:

    def __init__(self):
        self.num_list = []  
        self.val_to_index = {}  
    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False  
        self.num_list.append(val)
        self.val_to_index[val] = len(self.num_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False  
        
        idx_to_remove = self.val_to_index[val]
        last_val = self.num_list[-1]

        self.num_list[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove

        self.num_list.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)
