def find_duplicates(input_list):
    counts = {}
    duplicates = []
    for elem in input_list:
        if elem in counts:
            counts[elem] += 1
            if counts[elem] == 2:
                duplicates.append(elem)
        else:
            counts[elem] = 1
    return duplicates

list = (1,2,3,4,5,6,3,4,6,7,2,3,4,12,345,345,2,3,235,)
print(find_duplicates(list))