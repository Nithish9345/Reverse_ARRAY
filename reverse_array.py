""" Reverse array"""

""" use the same method used in REVERSE THE RANGE
    TIME COMPLEXITY - N/2"""


def reverse_array(array):
    i = 0
    j = len(array)-1
    while(i < j):
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

array = list(map(int, input().split()))

reverse_array(array)

print(array)