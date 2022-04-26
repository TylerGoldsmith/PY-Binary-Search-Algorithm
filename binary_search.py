# code your iterative algorithm here
def binary_search(data, el):
    first = 0
    last = len(data)-1 
    found = False
    while first <= last and not found:
        mid = (first+last)//2
        if data[mid] == el:
            found = True
    else:
        if el < data[mid]:
            last = mid-1
        else:
            first =mid+1
    return found


test_list = [2,5,6,8,23,543,24,645]
test_number = 8
#test
print('Number looking for: ' + f'{test_number}' + 'List searching: ' + f'{test_list}')
print('It is: ' + f'{binary_search(test_list, test_number)}' + ' the number is in the list.')