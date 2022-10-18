class Maths:
    def __init__(self):
        pass

    def fit_methods(self, item_list):
        """Uses next-fit, first-fit and first-fit decreasing"""
        pass

    def sorting_methods(self, item_list):
        """Uses bubble sort, merge sort, quicksort"""
        pass

class Sorting:

    @staticmethod
    def bubble_sort(item_list):
        checks = 0
        swaps = 0
        for i in range(len(item_list)-1):
            for j in range(len(item_list)-1-i):
                checks += 1
                if item_list[j] > item_list[j+1]:
                    swaps += 1
                    item_list[j], item_list[j+1] = item_list[j+1], item_list[j]
        print(item_list)
        return item_list, checks, swaps

    @staticmethod
    def shuttle_sort(item_list):
        checks = 0
        swaps = 0
        for i in range(len(item_list) - 1):
            for j in range(i, -1, -1):
                checks += 1
                if item_list[j] > item_list[j+1]:
                    swaps += 1
                    item_list[j], item_list[j + 1] = item_list[j + 1], item_list[j]
                else:
                    break
        return item_list, checks, swaps


if __name__ == '__main__':
    print(Sorting.bubble_sort([3,5,8,0,9,6,8,4]))
    print(Sorting.shuttle_sort([3, 5, 8, 0, 9, 6, 8, 4]))
    print(Sorting.shuttle_sort([3.5, 4.2, 1.3, 0.8, 3.2, 0.5, 4.0, 0.6, 2.3, 2.8, 4.5, 1.9]))