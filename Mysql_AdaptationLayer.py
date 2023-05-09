import pymysql

class Mysql_AdaptationLayer:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database)
        self.cursor = self.connection.cursor()

    def execute(self, sql, params=None):
        self.cursor.execute(sql,params)

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, table, data):
        keys = ", ".join(data[0].keys())
        values = [tuple(d.values()) for d in data]
        placeholders = ", ".join(["%s"] * len(data[0]))
        sql = f"insert into {table} ({keys}) values ({placeholders})"
        self.cursor.executemany(sql, values)
        self.commit()
    # 增添数据注意参数包装在列表中

    def delete(self, table, where):
        sql = f"delete from {table} where {where}"
        self.execute(sql)
        self.commit()

    def update(self, table, data, where):
        sets = ", ".join([f"{k}=%s" for k in data.keys()])
        values = tuple(data.values())
        sql = f"update {table} set {sets} where {where}"
        self.execute(sql, values)
        self.commit()

    def select(self, table, where=None):
        sql = f"select * from {table}"
        if where:
            sql += f" where {where}"
        self.execute(sql)
        return self.fetchall()
# mysql.connector.errors.NotSupportedError: Authentication plugin 'caching_sha2_password' is not supported
# 用mysql.connector会出现上述错误，但是使用pymysql不会报错。