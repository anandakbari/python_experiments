my_dict = {}
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'
my_dict['country'] = 'USA'
print("Original Dictionary:", my_dict)
print("Accessing values by keys:")
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])
print("Getting keys and values:")
keys = my_dict.keys()
values = my_dict.values()
print("Keys:", list(keys))
print("Values:", list(values))
del my_dict['age']
print("Dictionary after removing 'age':")
print(my_dict)
print("Length of the dictionary:", len(my_dict))
new_dict = my_dict.copy()
print("Copied dictionary:")
print(new_dict)
my_dict.clear()
print("Cleared dictionary:")
print(my_dict)

def histogram(l):
    count_dict = {}
    for num in l:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    pairs = [(num, count) for num, count in count_dict.items()]
    sorted_pairs = sorted(pairs, key=lambda x: (x[1], x[0]))
    return sorted_pairs
l = [3, 1, 2, 3, 2, 2, 4, 5, 4]
result = histogram(l)
print(result)

def perfect(n):
    if n <= 0:
        return False

    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n
n = 28
result = perfect(n)
print(result)

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    else:
        tower_of_hanoi(n - 1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n - 1, auxiliary, source, target)
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')
greater = lambda x, y: max(x, y)
result = greater(5, 10)
print(result)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
add_elements = lambda x, y: x + y
result = list(map(add_elements, list1, list2))
print(result)

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cube = lambda x: x**3
cubed_numbers = list(map(cube, input_list))
odd_cubed_numbers = list(filter(lambda x: x % 2 != 0, cubed_numbers))
print(odd_cubed_numbers)

