import array

arr = array.array('i', [1, 2, 3, 4, 5])

first_element = arr[0]
last_element = arr[-1]

arr.append(6)

arr.insert(2, 10)

arr.remove(4)

popped_element = arr.pop(1)

sub_array = arr[1:4]

index_of_10 = arr.index(10)

count_of_5 = arr.count(5)

print("First element:", first_element)
print("Last element:", last_element)
print("Array after modifications:", arr)
print("Popped element:", popped_element)
print("Sliced array:", sub_array)
print("Index of 10:", index_of_10)
print("Count of 5s:", count_of_5)
