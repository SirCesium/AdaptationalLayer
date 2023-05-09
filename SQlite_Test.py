from SQlite_AdaptationLayer import SQlite_AdaptationLayer
# 创建适配器实例
db_path = 'D:/SQlite/test.db'
SQlite_test = SQlite_AdaptationLayer(db_path)

# 插入数据
# data = {'id': 10, 'name': 'Tom', 'age': 28}
# SQlite_test.insert('example_table', data)

# data = [{'id': 8, 'name': 'jkh', 'age': 21},{'id': 9, 'name': 'qc', 'age': 22}]
# SQlite_test.insert('example_table', data)

# 更新数据
# data = {'age': 31}
# where = 'id = 1'
# SQlite_test.update('example_table', data, where)

# 删除数据
# where = 'id = 1'
# SQlite_test.delete('example_table', where)
#
# 查询数据
result = SQlite_test.select('example_table')
print(result)
