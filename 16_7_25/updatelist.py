lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("last Element:", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Updated List :", lst)

lst.sort()
print("Sorted List :", lst)

lst.pop(1)
print("Updated List :", lst)

lst.reverse()
print("Reversed list: ", lst)

print("Multiplication on lis: ", lst*2)

lst =lst[:4]
print("Sliced list :", lst)

lst.clear()
print("Updated list :", lst)