
class SelectSort(object):

    @staticmethod
    def sort(arr):
        for i in range(0, len(arr)):
            minj = i
            for j in range(i, len(arr)):
                if arr[minj] > arr[j]:
                    minj = j
            arr[i], arr[minj] = arr[minj], arr[i]

