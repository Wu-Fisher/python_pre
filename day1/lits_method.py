# numbers = [5,2,1,7,4]
# numbers.append(20)
# print(numbers)
# numbers.insert(1,23)
# print(numbers)
# numbers.remove(len(numbers))
# print(numbers)
# numbers.pop()
# print(numbers)
# # safe use
# print(2 in numbers)
# print(numbers.sort())
# #return None
# print(numbers)
# numbers.reverse()
# n2 = numbers.copy()
# print(n2)

# execrise
numbers = [2,2,3,1,4,5,5,6,7,7,8,8,8,8]
n2= set(numbers)
print(n2) 

uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)