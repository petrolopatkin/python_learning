#append method
numbers = [42, 52, 69, 67, 25, 3]
numbers.append(9)
print(numbers) 
#insert method
numbers2 = [66, 75, 4, 15, 6]
numbers2.insert(1, 56)
print(numbers2)
#remove method
numbers3 = [33, 22, 11, 10]
numbers3.remove(10)
print(numbers3)
#clear method
numbers4 = [7, 8, 12]
numbers4.clear()
print(numbers4)
#pop method
numbers5 = [77, 89, 1]
numbers5.pop()
print(numbers5)
#index method 
numbers6 = [86, 96, 76, 46, 26]
print(numbers6.index(76))
#in method
numbers7 = [41, 31, 21]
print(21 in numbers7)
#count method
numbers8 = [14, 16, 14, 18, 17, 14]
print(numbers8.count(14))
#sort method 
numbers9 = [65, 12, 0, 96, 506, 741, 54, 312]
numbers9.sort()
numbers9.reverse()
print(numbers9)
#task1
list_of_numbers = [5, 8, 8, 6, 9, 7, 8, 5, 4, 2, 2, 9]
unique = []
for item in list_of_numbers:
    if item not in unique:
        unique.append(item)
print(unique)


