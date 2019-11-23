a = [1,2,3,4,5,6,7,8,9,10]

# Find missing number from the sequence using binary search algorithm

def binary_search(a):
    mid = len(a) // 2
    if mid == 0:
        #print(a[0] + 1)
        return (a[0] + 1)
    if a[mid] ==  mid + a[0]:
        if mid == 1:
            return "No missing elements"
        return (binary_search(a[mid:]))
    else:
        return (binary_search(a[:mid]))

print(binary_search(a))