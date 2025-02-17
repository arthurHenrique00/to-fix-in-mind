def bin_search(array, x, low, high):
    while low <= high: 
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1