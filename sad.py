class ReversedList:
    def __init__(self, lst):
        self.r_lst = lst[::-1]

    def __getitem__(self, index):
        return self.r_lst[index]

    def __len__(self):
        return len(self.r_lst)
