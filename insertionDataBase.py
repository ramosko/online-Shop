import pyodbc
from faker import Faker
import random
from datetime import datetime, timedelta


fake = Faker()


conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-BFSJPBH\\SQLEXPRESS;DATABASE=SHOP')
cursor = conn.cursor()

def insert_user(num_records):
    for _ in range(num_records):
        username = fake.user_name()[:20]
        email = fake.email()[:50]
        phone_number = fake.numerify(text='###-###-####')
        address = fake.address()[:100]
        password = fake.password(length=12)
        
        cursor.execute("INSERT INTO [User] (username, email, phone_number, address, password) VALUES (?, ?, ?, ?, ?)",
                       username, email, phone_number, address, password)
    conn.commit()

def insert_cart(num_records):
    cursor.execute("SELECT id FROM [User]")
    user_ids = [row.id for row in cursor.fetchall()]
    
    if not user_ids:
        print("No users found in the User table. Please insert users first.")
        return

    for _ in range(num_records):
        user_id = random.choice(user_ids)
        total_price = round(random.uniform(10, 1000), 2)
        
        cursor.execute("INSERT INTO Cart (user_id, total_price) VALUES (?, ?)",
                       user_id, total_price)
    conn.commit()

def insert_order(num_records):
    cursor.execute("SELECT id FROM [User]")
    user_ids = [row.id for row in cursor.fetchall()]
    
    if not user_ids:
        print("No users found in the User table. Please insert users first.")
        return

    for _ in range(num_records):
        user_id = random.choice(user_ids)
        date = fake.date_between(start_date='-1y', end_date='today')
        total_price = round(random.uniform(10, 1000), 2)
        
    cursor.execute("INSERT INTO [Order] (user_id, date, total_price) VALUES (?, '{}', ?)".format(date),
               user_id, total_price)
    conn.commit()

def insert_transportation(num_records):
    cursor.execute("SELECT id FROM [Order]")
    order_ids = [row.id for row in cursor.fetchall()]
    
    if not order_ids:
        print("No orders found in the Order table. Please insert orders first.")
        return

    for _ in range(num_records):
        order_id = random.choice(order_ids)
        tracking_number = fake.uuid4()[:20]
        carrier = fake.company()[:50]
        date_of_shipment = fake.date_between(start_date='-1y', end_date='today')
        date_of_delivery = date_of_shipment + timedelta(days=random.randint(1, 10))
        
        cursor.execute("INSERT INTO Transportation (order_id, tracking_number, carrier, date_of_shipment, date_of_delivery) VALUES (?, ?, ?, '{}', '{}')".format(date_of_shipment, date_of_delivery),
               order_id, tracking_number, carrier)
    conn.commit()

def insert_comments(num_records):
    cursor.execute("SELECT id FROM [User]")
    user_ids = [row.id for row in cursor.fetchall()]
    
    cursor.execute("SELECT id FROM Item")
    item_ids = [row.id for row in cursor.fetchall()]
    
    if not user_ids or not item_ids:
        print("No users or items found. Please insert users and items first.")
        return

    for _ in range(num_records):
        user_id = random.choice(user_ids)
        item_id = random.choice(item_ids)
        text = fake.text(max_nb_chars=200)[:200]
        date = fake.date_between(start_date='-1y', end_date='today')
        
        cursor.execute("INSERT INTO Comments (user_id, item_id, text, date) VALUES (?, ?, ?, '{}')"
               .format(date),user_id, item_id, text)
    conn.commit()

def insert_manager(num_records):
    for _ in range(num_records):
        username = fake.user_name()[:20]
        email = fake.email()[:50]
        password = fake.password(length=12)
        
        cursor.execute("INSERT INTO Manager (username, email, password) VALUES (?, ?, ?)",
                       username, email, password)
    conn.commit()

def insert_category(num_records):
    categories = ["Dairy", "Beverages", "Nuts", "Cleaning Supplies", "Cosmetics", "Groceries", "Home Appliances", "Clothing"]
    for category in categories[:num_records]:
        cursor.execute("INSERT INTO Category (name) VALUES (?)", category[:50])
    conn.commit()

def insert_brand(num_records):
    for _ in range(num_records):
        name = fake.company()[:50]
        cursor.execute("INSERT INTO Brand (name) VALUES (?)", name)
    conn.commit()

def insert_item(num_records):
    cursor.execute("SELECT id FROM Brand")
    brand_ids = [row.id for row in cursor.fetchall()]
    
    cursor.execute("SELECT id FROM Category")
    category_ids = [row.id for row in cursor.fetchall()]
    
    if not brand_ids or not category_ids:
        print("No brands or categories found. Please insert brands and categories first.")
        return

    for _ in range(num_records):
        brand_id = random.choice(brand_ids)
        category_id = random.choice(category_ids)
        name = (fake.word() + " " + fake.word())[:50]
        produce_date = fake.date_between(start_date='-2y', end_date='-1y')
        expire_date = fake.date_between(start_date='today', end_date='+2y')
        price = round(random.uniform(1, 1000), 2)
        amount = random.randint(0, 1000)
        
        cursor.execute("INSERT INTO Item (brand_id, category_id, name, produce_date, expire_date, price, amount) VALUES (?, ?, ?, '{}', '{}', ?, ?)".format(produce_date, expire_date),
                   brand_id, category_id, name, price, amount)
    conn.commit()

def insert_discount(num_records):
    cursor.execute("SELECT id FROM Item")
    item_ids = [row.id for row in cursor.fetchall()]
    
    if not item_ids:
        print("No items found. Please insert items first.")
        return

    for _ in range(num_records):
        item_id = random.choice(item_ids)
        start_date = fake.date_between(start_date='-30d', end_date='today')
        end_date = fake.date_between(start_date='today', end_date='+30d')
        amount = round(random.uniform(5, 50), 2)
        
    cursor.execute("INSERT INTO Discount (item_id, start_date, end_date, amount) VALUES (?, '{}', '{}', ?)"
               .format(start_date, end_date),item_id, amount)
    conn.commit()

def insert_item_order(num_records):
    cursor.execute("SELECT id FROM Item")
    item_ids = [row.id for row in cursor.fetchall()]
    
    cursor.execute("SELECT id FROM [Order]")
    order_ids = [row.id for row in cursor.fetchall()]
    
    if not item_ids or not order_ids:
        print("No items or orders found. Please insert items and orders first.")
        return

    for _ in range(num_records):
        item_id = random.choice(item_ids)
        order_id = random.choice(order_ids)
        
        cursor.execute("INSERT INTO ItemOrder (item_id, order_id) VALUES (?, ?)",
                       item_id, order_id)
    conn.commit()

def insert_item_cart(num_records):
    cursor.execute("SELECT id FROM Item")
    item_ids = [row.id for row in cursor.fetchall()]
    
    cursor.execute("SELECT id FROM Cart")
    cart_ids = [row.id for row in cursor.fetchall()]
    
    if not item_ids or not cart_ids:
        print("No items or carts found. Please insert items and carts first.")
        return

    for _ in range(num_records):
        item_id = random.choice(item_ids)
        cart_id = random.choice(cart_ids)
        
        cursor.execute("INSERT INTO ItemCart (item_id, cart_id) VALUES (?, ?)",
                       item_id, cart_id)
    conn.commit()

def insert_manager_comment(num_records):
    cursor.execute("SELECT id FROM Manager")
    manager_ids = [row.id for row in cursor.fetchall()]
    
    cursor.execute("SELECT id FROM Comments")
    comment_ids = [row.id for row in cursor.fetchall()]
    
    if not manager_ids or not comment_ids:
        print("No managers or comments found. Please insert managers and comments first.")
        return

    for _ in range(num_records):
        manager_id = random.choice(manager_ids)
        comment_id = random.choice(comment_ids)
        
        cursor.execute("INSERT INTO ManagerComment (manger_id, commnet_id) VALUES (?, ?)",
                       manager_id, comment_id)
    conn.commit()


num_records = 100


insert_user(num_records)
# insert_manager(10) 
# insert_category(8)  
# insert_brand(num_records)
# insert_item(num_records)
# insert_cart(num_records)
# insert_order(num_records)
# insert_transportation(num_records)
# insert_comments(num_records)
# insert_discount(num_records)
# insert_item_order(num_records)
# insert_item_cart(num_records)
# insert_manager_comment(num_records)

# print(f"{num_records} records inserted for each table (except for specific cases).")


# SQL query to insert data
# sql = "INSERT INTO [User] (username, email, phone_number, address, password) VALUES (?, ?, ?, ?, ?)"
# values = ('John Does', 'ram@email.com', '113-456-7890', '123 Main St', 'password123')

# # Execute the SQL query
# cursor.execute(sql, values)

# # Commit the transaction
# conn.commit()

# print(cursor.rowcount, "record inserted.")


# sql = "INSERT INTO Comments (user_id, item_id, text, date) VALUES (?, ?, ?, ?)"
# values = (1, 1, 'This is a comment text', '2024-07-06')

# # Execute the SQL query
# cursor.execute(sql, values)

# # Commit the transaction
# conn.commit()

# print(cursor.rowcount, "record inserted.")


# sql = "INSERT INTO Manager (username, email, password) VALUES (?, ?, ?)"
# values = ('manager1', 'manager1@example.com', 'securepassword')

# # Execute the SQL query
# cursor.execute(sql, values)

# # Commit the transaction
# conn.commit()

# print(cursor.rowcount, "record inserted.")

# sql = "INSERT INTO Transportation (order_id, tracking_number, carrier, date_of_shipment, date_of_delivery) VALUES (?, ?, ?, ?, ?)"
# values = (1, 'TRK123456789', 'truck', '2024-07-01', '2024-07-05')
# # Execute the SQL query
# cursor.execute(sql, values)

# # Commit the transaction
# conn.commit()
# print(cursor.rowcount, "record inserted.")



# sql = "INSERT INTO [Order] (user_id, date, total_price) VALUES (?, ?, ?)"
# values = (1, '2024-07-06', 99.99)

# # Execute the SQL query
# cursor.execute(sql, values)

# # Commit the transaction
# conn.commit()
# print(cursor.rowcount, "record inserted.")


# sql = "INSERT INTO Cart (user_id, total_price) VALUES (?, ?)"
# values = (1, 59.99)

# # Execute the SQL query
# cursor.execute(sql, values)

# # Commit the transaction
# conn.commit()
# print(cursor.rowcount, "record inserted.")


# sql = "INSERT INTO Item (brand_id, category_id, name, produce_date, expire_date, price, amount) VALUES (?, ?, ?, ?, ?, ?, ?)"
# values = (1, 1, 'Item Name', '2024-01-01', '2025-01-01', 19.99, 100)

# # Execute the SQL query
# cursor.execute(sql, values)

# # Commit the transaction
# conn.commit()
# print(cursor.rowcount, "record inserted.")


# sql = "INSERT INTO Category (name) VALUES (?)"
# values = ('Category Name')

# # Execute the SQL query
# cursor.execute(sql, values)

# # Commit the transaction
# conn.commit()
# print(cursor.rowcount, "record inserted.")

# sql = "INSERT INTO Brand (name) VALUES (?)"
# values = ('Brand Name')
# # Execute the SQL query
# cursor.execute(sql, values)

# # Commit the transaction
# conn.commit()
# print(cursor.rowcount, "record inserted.")


# بستن اتصال
cursor.close()
conn.close()