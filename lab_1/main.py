import HashTable

table = HashTable.HashTable()
with open('test_data.txt', 'r') as file:
    read_data = file.read().split(';')

for word in read_data:
    table.put(word)

table.print()
