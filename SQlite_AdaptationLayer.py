import sqlite3

class SQlite_AdaptationLayer:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params)

    def executemany(self, sql, data):
        self.cursor.executemany(sql, data)
        self.conn.commit()
    # 相对于pymysql而言需要再引用一下executemany方法，sqlite3中并没有提供。
    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def insert(self, table, data):
        if isinstance(data, dict):
            data = [data]  # 将单行数据转换为列表形式
        keys = ", ".join(data[0].keys())
        placeholders = ", ".join(["?"] * len(data[0]))
        sql = f"insert into {table} ({keys}) values ({placeholders})"
        values = [tuple(row.values()) for row in data]
        self.executemany(sql, values)
        self.commit()

    def delete(self, table, where):
        sql = f"delete from {table} where {where}"
        self.execute(sql,())
        self.commit()

    def update(self, table, data, where):
        sets = ", ".join([f"{k}=?" for k in data.keys()])
        values = tuple(data.values())
        sql = f"update {table} set {sets} where {where}"
        self.execute(sql, values)
        self.commit()

    def select(self, table, where=None):
        sql = f"select * from {table}"
        if where:
            sql += f" where {where}"
        self.execute(sql,())
        return self.fetchall()



