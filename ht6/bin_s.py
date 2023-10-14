def binary_search(list_for_search, value) -> int:
    first = 0
    last = len(list_for_search) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if list_for_search[mid] == value:
            index = mid
        elif value < list_for_search[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return index


list_of_int = (3, 6, 35, 7, 900, 77)
sorted_list_of_int = sorted(list_of_int)
print(binary_search(sorted_list_of_int, 6))
