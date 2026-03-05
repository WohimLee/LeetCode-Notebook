
import numpy as np

def partion(data, loIdx, hiIdx):

    pivot = data[loIdx]
    lPointer = loIdx - 1
    rPointer = hiIdx + 1
    while True:

        lPointer += 1
        while data[lPointer] < pivot:
            lPointer += 1

        rPointer -= 1
        while data[rPointer] > pivot:
            rPointer -= 1

        if lPointer >= rPointer:
            return rPointer
        
        data[lPointer], data[rPointer] = data[rPointer], data[lPointer]

def quick_sort(data):

    def _qs(loIdx, hiIdx):
        if loIdx >= hiIdx:
            return
        
        partionPointer = partion(data, loIdx, hiIdx)

        _qs(loIdx, partionPointer)
        _qs(partionPointer+1, hiIdx)
    _qs(0, len(data)-1)
    return data

if __name__ == "__main__":
    data = [5, 1, 8, 3, 2, 7, 4, 6, 3, 11, 5, 23]
    data = np.random.randint(0, 50, size=20).tolist()

    print("原数组:\t\t\t", data)
    print("快排结果:\t\t", quick_sort(data))
    print("Python sorted结果:\t", sorted(data))
    print("原数组已修改:\t\t", data)