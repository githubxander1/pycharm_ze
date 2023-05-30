from pprint import pprint

import pymysql
from prettytable import PrettyTable

# connect to the database
db_conn = pymysql.Connect(host='192.168.7.84', port=3306,
                          user='product_statistics', password='OwDXEIs*8eIeED23s',
                          database='product_statistics')

try:
    # create a cursor object
    cursor = db_conn.cursor()

    # fetch the latest record from t_product_statistics
    cursor.execute(
        "SELECT * FROM t_product_statistics WHERE product_id=1 AND uid=1008247 ORDER BY create_time DESC LIMIT 1;")
    product_statistics_result = cursor.fetchone()
    # print(product_statistics_result)

    # fetch the corresponding record from t_classname_mapping
    class_name_mapping_id = product_statistics_result[3]
    # print(class_name_mapping_id)# assuming class_name_mapping_id is at index 3
    cursor.execute(f"SELECT * FROM t_classname_mapping WHERE id='{class_name_mapping_id}';")
    class_name_mapping_result = cursor.fetchone()
    print(class_name_mapping_result)

    # create a pretty table with headers
    x = PrettyTable()
    x.field_names = ["id", "product_id", "uid", "class_name_mapping_id", "create_time"]

    # add rows to the table
    x.add_row(product_statistics_result)
    x.add_row(class_name_mapping_result)

    # print the table
    print(x)

    # close cursor and database connection
    cursor.close()
    db_conn.close()

except Exception as ex:
    print(f"Error: {ex}")
