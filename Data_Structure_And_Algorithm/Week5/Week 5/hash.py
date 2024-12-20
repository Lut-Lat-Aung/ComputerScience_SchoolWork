from sys import stdin


# Read the sequence of operations to be operated on the hash table
operations = []
'''''
for line in stdin:
    line = line.split()
    if len(line) > 2:
        line[2] = int(line[2])
    operations.append(line)
'''

table_size = 10    # set table size here
hash_table = [[] for i in range(table_size)]

def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')

def hash_func(s):
    # return the hash value
   return len(s) % table_size

def insert(s, v):
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table
    hash_value = hash_func(s)
    for item in hash_table[hash_value]:
        if item[0] == s:
            return -1  # Key already exists
    hash_table[hash_value].append((s, v))
    return 0

def search(s):
    # return value of the key or
    # return -1 if s does not exists in hash table
    hash_value = hash_func(s)
    for item in hash_table[hash_value]:
        if item[0] == s:
            return item[1]
    return -1

def delete(s):
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table
    hash_value = hash_func(s)
    for item in hash_table[hash_value]:
        if item[0] == s:
            hash_table[hash_value].remove(item)
            return 0
    return -1  # Key does not exist


# The main program to execute the sequence of operations
for op in operations:
    # op[0] is "insert" or "search" or "delete"

    if op[0] == "insert":
        result = insert(op[1], op[2])
        if result == -1:
            print("Key already exists:", op[1])
    elif op[0] == "search":
        result = search(op[1])
        if result == -1:
            print("Key not found:", op[1])
        else:
            print("Value for key", op[1], "is", result)
    elif op[0] == "delete":
        result = delete(op[1])
        if result == -1:
            print("Key not found:", op[1])
        else:
            print("Key", op[1], "deleted successfully")




    

