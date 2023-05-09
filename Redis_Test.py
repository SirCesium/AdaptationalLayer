from Redis_AdaptationLayer import Redis_AdaptationLayer

redis_conn = Redis_AdaptationLayer(host='localhost', port=6379, db=0)

redis_conn.insert('key1', 'value1')

data = {'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
redis_conn.insert(data)

value1 = redis_conn.select('key1')
print(value1)

keys = ['key1', 'key2', 'key3', 'key4']
values1 = []
for key in keys:
    value = redis_conn.select(key)
    values1.append(value)
print(values1)

redis_conn.delete('key1')

redis_conn.update('key2', 'new_value2')

data = {'key3': 'new_value3', 'key4': 'new_value4'}
redis_conn.update(data)

value2 = redis_conn.select('key2')
print(value2)

values2 = []
for key in keys:
    value = redis_conn.select(key)
    values2.append(value)
print(values2)

redis_conn.close()

# 多个值查询时需要for循环依次调用get方法并将值保存在列表中