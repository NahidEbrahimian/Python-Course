
Array = list(map(int, input().split()))
Array_copy = Array.copy()
Array.sort()

if Array == Array_copy:
    print('Input array is sorted')

else:
    print('Input array is not sorted.')