import redis
# r = redis.Redis(host='localhost', port=6379, db=0)
# value = r.get('aa')
# print(value)
# string_value = value.decode('utf-8')
# print(string_value)
# 2-7行可忽略
class Redis_AdaptationLayer:
    def __init__(self,host,port,db):
        self.host = host
        self.port = port
        self.db = db
        self.connection = redis.Redis(host=self.host, port=self.port, db=self.db)
        
    def insert(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], dict):
            self.connection.mset(args[0])
        elif len(args) == 2:
            self.connection.set(args[0], args[1])
        elif kwargs:
            self.connection.mset(kwargs)

    def select(self, key):
        return self.connection.get(key)

    def delete(self, key):
        self.connection.delete(key)

    def update(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], dict):
            self.connection.mset(args[0])
        elif len(args) == 2:
            self.connection.set(args[0], args[1])
        elif kwargs:
            self.connection.mset(kwargs)

    def close(self):
        self.connection.close()

# 对insert与update做出了改进，使得对一个或多个键值对通用
