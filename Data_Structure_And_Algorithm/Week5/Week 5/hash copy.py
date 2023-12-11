from sys import stdin


# Read the sequence of operations to be operated on the hash table
operations = []
for line in stdin:
    line = line.split()
    if len(line) > 2:
        line[2] = int(line[2])
    operations.append(line)


table_size = 10    # set table size here
hash_table = [[] for i in range(table_size)]

def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')

def hash_func(s):
    # return the hash value
    total = 0
    for c in s:
        total += ord(c)
    return total % table_size

def insert(s, v):
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table
    
    if search(s) != -1:
        return -1
    else:
        hash_value = hash_func(s)
        l = hash_table[hash_value]
        l.append((s,v))
        return 0

def search(s):
    # return value of the key or
    # return -1 if s does not exists in hash table
    hash_value = hash_func(s)
    l = hash_table[hash_value]
    for i in range(len(l)):
        if l[0] ==s:
            return l[1]
    return -1

def delete(s):
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table
    if search(s) == -1:
        return -1
    
    else:
        hash

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


insert("I", 1)
show_hash_table()

    

