import pyodbc

def connect_to_database(server, database):
    connection = None
    try:
        connection = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'
        )
        print("we are connected to the database")
    except pyodbc.Error as e:
        print(f"Error'{e}'accure")
    return connection

def add_data(connection, table_name, data):
    cursor = connection.cursor()
    placeholders = ", ".join(["?"] * len(data))
    columns = ", ".join(data.keys())
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    try:
        cursor.execute(sql, list(data.values()))
        connection.commit()
        print("add data successfully")
    except pyodbc.Error as e:
        print(f"Error'{e}'accure")

def delete_data(connection, table_name, condition):
    cursor = connection.cursor()
    sql = f"DELETE FROM {table_name} WHERE {condition}"
    try:
        cursor.execute(sql)
        connection.commit()
        print("delete data successfully")
    except pyodbc.Error as e:
        print(f"Error'{e}'accure")

if __name__ == "__main__":
    connection = connect_to_database("DESKTOP-BFSJPBH\SQLEXPRESS", "SHOP")
    
    # # مثال اضافه کردن داده
    # data_to_add = {
    #     "column1": "value1",
    #     "column2": "value2",
    #     "column3": "value3"
    # }
    # add_data(connection, "your_table", data_to_add)

    # add to category
    # data_to_add = {
    #     "name": "Nuts",
    # }
    # add_data(connection, "Category", data_to_add)
    
    # # delete from category 
    # condition_to_delete = "name = 'Nuts'"
    # delete_data(connection, "Category", condition_to_delete)

    # add to brand
    # data_to_add = {
    #     "name": "Ab Ali",
    # }
    # add_data(connection, "Brand", data_to_add)
    
    # # delete from brand  
    # condition_to_delete = "name = 'Ab Ali'"
    # delete_data(connection, "Brand", condition_to_delete)


    # add to Item
    # data_to_add = {
    #     "name": "Ab Ali",
    #     "brand_id": "102",
    #     "category_id": "2",
    #     "produce_date": "2023-01-01",
    #     "expire_date": "2023-02-02",
    #     "price": "25",
    #     "amount": "120"
    # }
    # add_data(connection, "Item", data_to_add)
    
    # # delete from Item
    # condition_to_delete = "name = 'Ab Ali'"
    # delete_data(connection, "Item", condition_to_delete)


    # add to comments
    # data_to_add = {
    #     "user_id": "1",
    #     "item_id": "4",
    #     "text": "fuck this shit",
    #     "date": "2023-02-02"
    # }
    # add_data(connection, "Comments", data_to_add)
    
    # delete from comments
    # condition_to_delete = " text LIKE '%fuck%'"
    # delete_data(connection, "Comments", condition_to_delete)
    
    if connection:
        connection.close()
        print("cloded connection")