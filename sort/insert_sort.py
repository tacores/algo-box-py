
class InsertSort(object):

    def sort(self, arr):
        for i in range(1, len(arr)):
            j = i - 1
            v = arr[i]
            while j >= 0 and arr[j] > v:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = v

