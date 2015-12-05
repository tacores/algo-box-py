
class BubbleSort(object):

    @staticmethod
    def sort(arr):
        flag = True
        while flag:
            flag = False
            for j in range(len(arr) - 1, 0, -1):
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
                    flag = True

