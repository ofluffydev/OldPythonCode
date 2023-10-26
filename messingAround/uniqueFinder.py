def find_unique(input):
    uniques = []
    for elem in input:
        if input.count(elem) == 1 and  elem not in  uniques:
            uniques.append(elem)
    return uniques

lst = [1, 2, 3, 4, 5, 1, 3, 4, 6, 7, 5, 8, 9, 9, 10, 2]

print(find_unique(lst))