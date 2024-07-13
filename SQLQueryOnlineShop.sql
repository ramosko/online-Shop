----CREATE DATABASE SHOP;

----CREATE TABLE [User] (
----    id INT IDENTITY(1,1) PRIMARY KEY,
----    username VARCHAR(50) NOT NULL,
----    email VARCHAR(100) NOT NULL,
----    phone_number VARCHAR(15),
----    address VARCHAR(255),
----    password VARCHAR(50) NOT NULL
----);

----CREATE TABLE Category (
----    id INT IDENTITY(1,1) PRIMARY KEY,
----    name VARCHAR(50) NOT NULL
----);

----CREATE TABLE Brand (
----    id INT IDENTITY(1,1) PRIMARY KEY,
----    name VARCHAR(50) NOT NULL
----);

----CREATE TABLE Item (
----    id INT IDENTITY(1,1) PRIMARY KEY,
----    brand_id INT,
----    category_id INT,
----    name VARCHAR(100) NOT NULL,
----    produce_date DATE,
----    expire_date DATE,
----    price DECIMAL(10, 2),
----    amount INT,
----    FOREIGN KEY (brand_id) REFERENCES Brand(id),
----    FOREIGN KEY (category_id) REFERENCES Category(id)
----);

----CREATE TABLE Cart (
----    id INT IDENTITY(1,1) PRIMARY KEY,
----    user_id INT NOT NULL,
----    total_price DECIMAL(10, 2),
----    FOREIGN KEY (user_id) REFERENCES [User](id)
----);

----CREATE TABLE [Order] (
----    id INT IDENTITY(1,1) PRIMARY KEY,
----    user_id INT NOT NULL,
----    date DATE,
----    total_price DECIMAL(10, 2),
----    FOREIGN KEY (user_id) REFERENCES [User] (id)
----);

----CREATE TABLE Transportation (
----    id INT IDENTITY(1,1) PRIMARY KEY,
----    order_id INT NOT NULL,
----    tracking_number VARCHAR(50),
----    carrier VARCHAR(50),
----    date_of_shipment DATE,
----    date_of_delivery DATE,
----    FOREIGN KEY (order_id) REFERENCES [Order] (id)
----);


----CREATE TABLE Manager (
----    id INT IDENTITY(1,1) PRIMARY KEY,
----    username VARCHAR(50) NOT NULL,
----    email VARCHAR(100) NOT NULL,
----    password VARCHAR(50) NOT NULL
----);

----CREATE TABLE Comments (
----    id INT IDENTITY(1,1) PRIMARY KEY,
----    user_id INT NOT NULL,
----    item_id INT NOT NULL,
----    text TEXT,
----    date DATE,
----    FOREIGN KEY (user_id) REFERENCES [User] (id),
----    FOREIGN KEY (item_id) REFERENCES Item(id),
----);

----CREATE TABLE Discount (
----    id INT IDENTITY(1,1) PRIMARY KEY,
----    item_id INT NOT NULL,
----    start_date DATE,
----    end_date DATE,
----    amount DECIMAL(5, 2),
----    FOREIGN KEY (item_id) REFERENCES Item(id)
----);

----CREATE TABLE ItemOrder (
----    item_id INT,
----    order_id INT,
----    PRIMARY KEY (item_id, order_id),
----    FOREIGN KEY (item_id) REFERENCES Item(id),
----    FOREIGN KEY (order_id) REFERENCES [Order] (id)
----);

----CREATE TABLE ItemCart (
----    item_id INT,
----    cart_id INT,
----    PRIMARY KEY (item_id, cart_id),
----    FOREIGN KEY (item_id) REFERENCES Item(id),
----    FOREIGN KEY (cart_id) REFERENCES Cart(id)
----);

----CREATE TABLE ManagerComment (
----    manager_id INT,
----    comment_id INT,
----    PRIMARY KEY (manager_id, comment_id),
----    FOREIGN KEY (manager_id) REFERENCES Manager(id),
----    FOREIGN KEY (comment_id) REFERENCES Comments(id)
----);

--INSERT INTO [User] (username, email, phone_number, address, password)
--VALUES ('john_doe', 'john@example.com', '1234567890', '123 Main St', 'password123');

--INSERT INTO Category (name)
--VALUES ('Electronics');

--INSERT INTO Brand (name)
--VALUES ('Samsung');

--INSERT INTO Item (brand_id, category_id, name, produce_date, expire_date, price, amount)
--VALUES (1, 1, 'Samsung Galaxy S21', '2023-01-01', '2025-01-01', 999.99, 100);

SELECT * FROM [User];

--DELETE  FROM [User]
--WHERE id = 209;

--SELECT * FROM Item;

--DELETE  FROM Item
--WHERE id = 5;

--SELECT * FROM Brand;

--DELETE  FROM Brand
--WHERE id = 104;

--SELECT * FROM Category;

--DELETE  FROM Category
--WHERE id = 12;


--INSERT INTO Cart (user_id, total_price)
--VALUES (1, 999.99);

--SELECT * FROM Cart;

--DELETE  FROM Cart
--WHERE id = 5;

--INSERT INTO [Order] (user_id, date, total_price)
--VALUES (1,'2023-01-01', 999.99);

--SELECT * FROM [Order];

--DELETE FROM [Order]
--WHERE id = 3;

--INSERT INTO Transportation (order_id, tracking_number, carrier, date_of_shipment, date_of_delivery)
--VALUES (1,'102546874','truck','2023-02-02', '2023-03-02');

--SELECT * FROM Transportation; 

--DELETE FROM Transportation
--WHERE id = 2;

--SELECT * FROM Manager;

--INSERT INTO Comments (user_id, item_id, text, date)
--VALUES (1, 1,'good but expensive','2023-03-02');

--SELECT * FROM Comments;
--DELETE FROM Comments
--WHERE id = 5;

--INSERT INTO Discount (item_id, start_date, end_date, amount)
--VALUES (1,'2022-03-02', '2023-03-02', 25.00);

--INSERT INTO Discount (item_id, start_date, end_date, amount)
--VALUES (2,'2022-03-02', '2025-03-02', 25.00);

--SELECT * FROM Discount;

--DELETE FROM Discount
--WHERE id = 5 or id = 6 or id = 4 or id = 3;

--INSERT INTO ItemOrder(item_id, order_id)
--VALUES (1,1);

--SELECT * FROM ItemOrder;


--INSERT INTO ItemCart(item_id, cart_id)
--VALUES (2, 3);


--SELECT * FROM ItemCart;

--INSERT INTO ManagerComment(manager_id, comment_id)
--VALUES (1,1);

--SELECT * FROM ManagerComment;

--SELECT username, email FROM [User];

--SELECT * FROM Item WHERE category_id = 1;

--UPDATE [User]
--SET email = 'new_email@example.com'
--WHERE username = 'john_doe';

--UPDATE Item
--SET price = 899.99
--WHERE name = 'Samsung Galaxy S21';

--SELECT i.name, i.price, ic.cart_id
--FROM Item i
--JOIN ItemCart ic ON i.id = ic.item_id
--WHERE ic.cart_id = 3;

--SELECT o.id, o.date, o.total_price
--FROM [Order] o
--JOIN [User] u ON o.user_id = u.id
--WHERE u.username = 'john_doe';

--SELECT c.text, c.date, i.name AS item_name
--FROM Comments c
--JOIN [User] u ON c.user_id = u.id
--JOIN Item i ON c.item_id = i.id
--WHERE u.username = 'john_doe';


--SELECT i.name, i.price, d.amount AS discount
--FROM Item i
--JOIN Discount d ON i.id = d.item_id
--WHERE d.start_date <= CAST(GETDATE() AS DATE) AND d.end_date >= CAST(GETDATE() AS DATE);

--SELECT COUNT(*) AS user_count FROM [User];

--SELECT SUM(i.price) AS total_price
--FROM Item i
--JOIN ItemCart ic ON i.id = ic.item_id
--JOIN Cart c ON ic.cart_id = c.id
--JOIN [User] u ON c.user_id = u.id
--WHERE u.username = 'john_doe';

--SELECT i.name, i.price, u.username, c.text
--FROM Comments c 
--JOIN [User] u ON u.id = c.user_id
--JOIN Item i ON i.id = c.item_id
--WHERE c.text LIKE '%good%'; 

--SELECT i.name AS ItemName, b.name as BrandName, c.name as CategoryName, i.price
--FROM Item i
--JOIN Brand b ON b.id = i.brand_id
--Join Category c ON c.id = i.category_id
--WHERE i.price < 700;