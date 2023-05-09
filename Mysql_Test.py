from Mysql_AdaptationLayer import Mysql_AdaptationLayer

Mysql_test = Mysql_AdaptationLayer(host='127.0.0.1',
                            user='root',
                             password='Cs171877',
                             database='test2')

# data_test = [{"SId": 11, "Sname": "cc", "Sex": "boy", "RId": 666}]
# Mysql_test.insert("suzhouwanyihao", data_test)

# result_test = Mysql_test.select("suzhouwanyihao",where="SId<4")
# print(result_test)

# data_test = [{"SId": 8, "Sname": "cc", "Sex": "boy", "RId": 666},{"SId": 9, "Sname": "cc", "Sex": "boy", "RId": 666}]
# Mysql_test.insert("suzhouwanyihao", data_test)

result = Mysql_test.select("suzhouwanyihao")
for row in result:
    print(row)
