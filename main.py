class Maths:
    def __init__(self):
        pass

    def fit_methods(self, item_list):
        """Uses next-fit, first-fit and first-fit decreasing"""
        pass

    def sorting_methods(self, item_list):
        """Uses bubble sort, merge sort, quicksort"""
        pass

    def _bubble_sort(self, item_list):
        checks = 0
        swaps = 0
        for i in range(len(item_list)-1):
            for j in range(len(item_list)-1):
                checks += 1
                if item_list[i] > item_list[j+1]:
                    swaps += 1
                    item_list[j], item_list[j+1] = item_list[j+1], item_list[j]
        print(item_list)
        return item_list, checks, swaps

if __name__ == '__main__':
    print(Maths()._bubble_sort([5,3,6,1]))