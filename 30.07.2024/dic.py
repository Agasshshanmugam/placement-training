my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

name = my_dict['name']
age = my_dict.get('age')

my_dict['job'] = 'Engineer'

my_dict['age'] = 31

del my_dict['city']

has_job = 'job' in my_dict

keys = my_dict.keys()

values = my_dict.values()

items = my_dict.items()

print("Name:", name)
print("Age:", age)
print("Dictionary after updates:", my_dict)
print("Has 'job' key?", has_job)
print("Keys:", keys)
print("Values:", values)
print("Items:", items)
