from SQlite_AdaptationLayer import SQlite_AdaptationLayer

db_path = 'D:/SQlite/test.db'
SQlite_test = SQlite_AdaptationLayer(db_path)

# data = {'id': 10, 'name': 'Tom', 'age': 28}
# SQlite_test.insert('example_table', data)

# data = [{'id': 8, 'name': 'jkh', 'age': 21},{'id': 9, 'name': 'qc', 'age': 22}]
# SQlite_test.insert('example_table', data)

# data = {'age': 31}
# where = 'id = 1'
# SQlite_test.update('example_table', data, where)

# where = 'id = 1'
# SQlite_test.delete('example_table', where)

result = SQlite_test.select('example_table')
print(result)
