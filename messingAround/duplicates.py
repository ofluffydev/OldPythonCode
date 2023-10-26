def find_duplicates(lst):
    d = {}
    duplicates = []
    for item in lst:
        if item in d:
            if d[item] == 1:
                duplicates.append(item)
            d[item] += 1
        else:
            d[item] = 1
    return duplicates

print(find_duplicates([1,2,3,4,5,3,2,1,3,4,5,3,2,1,4]))