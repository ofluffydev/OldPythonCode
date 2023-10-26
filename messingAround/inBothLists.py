numbers1 = [1,2,3,4,5,2,1,2,3,4,2,2,3,4,5]
numbers2 = [3,7,5,3,32,2,3,4,5,2,2,1,3,4,2]
commons = []

for num in numbers1:
    if num in numbers2:
        commons.append(num)
print(commons)