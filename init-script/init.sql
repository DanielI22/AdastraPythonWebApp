-- Users Table
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename  = 'users') THEN
    CREATE TABLE public.Users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        joined_date DATE NOT NULL
    );
    INSERT INTO Users (name, email, joined_date) VALUES
        ('Daniel Ivanov', 'daniel.ivanov@example.com', '2023-01-01'),
        ('Peter Petrov', 'peter.petrov@example.com', '2023-01-15'),
        ('Ivan Ivanov', 'ivan.ivanov@example.com', '2023-02-22');
    END IF;
END $$;

-- Products Table
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename  = 'products') THEN
    CREATE TABLE public.Products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        category VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        stock_quantity INTEGER NOT NULL
    );
    INSERT INTO Products (name, category, price, stock_quantity) VALUES
        ('Laptop Pro 17"', 'Electronics', 1200.00, 50),
        ('Smartphone X12', 'Electronics', 800.00, 100),
        ('Bluetooth Headphones', 'Accessories', 150.00, 200),
        ('Ergonomic Keyboard', 'Accessories', 70.00, 150),
        ('Wireless Mouse', 'Accessories', 40.00, 300);
    END IF;
END $$;

-- Orders Table
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename  = 'orders') THEN
    CREATE TABLE public.Orders (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES Users(id),
        order_date DATE NOT NULL,
        status VARCHAR(50)
    );
    INSERT INTO Orders (user_id, order_date, status) VALUES
        (1, '2023-02-01', 'Completed'),
        (1, '2023-02-15', 'Completed'),
        (1, '2023-03-20', 'Shipped'),
        (2, '2023-02-05', 'Completed'),
        (2, '2023-02-18', 'Completed'),
        (2, '2023-03-25', 'Shipped');
    END IF;
END $$;

-- OrderItems Table
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename  = 'orderitems') THEN
    CREATE TABLE public.OrderItems (
        id SERIAL PRIMARY KEY,
        order_id INTEGER NOT NULL REFERENCES Orders(id),
        product_id INTEGER NOT NULL REFERENCES Products(id),
        quantity INTEGER NOT NULL,
        price_at_purchase DECIMAL(10, 2) NOT NULL
    );
    INSERT INTO OrderItems (order_id, product_id, quantity, price_at_purchase) VALUES
        (1, 1, 1, 1200.00),
        (2, 2, 1, 800.00),
        (3, 3, 2, 150.00),
        (4, 4, 1, 70.00),
        (5, 5, 1, 40.00),
        (6, 1, 1, 1200.00),
        (6, 1, 1, 1200.00),
        (1, 3, 1, 600.00);
    END IF;
END $$;

-- Reviews Table
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename  = 'reviews') THEN
    CREATE TABLE public.Reviews (
        id SERIAL PRIMARY KEY,
        product_id INTEGER NOT NULL REFERENCES Products(id),
        user_id INTEGER NOT NULL REFERENCES Users(id),
        rating INTEGER NOT NULL,
        review_text TEXT,
        review_date DATE NOT NULL
    );
    INSERT INTO Reviews (product_id, user_id, rating, review_text, review_date) VALUES
    (1, 1, 5, 'Absolutely love my new laptop. Fast and reliable.', '2023-02-02'),
    (2, 2, 4, 'The smartphone is great, but battery life could be better.', '2023-02-06'),
    (2, 1, 5, 'Great smarthphone!', '2023-02-02');
    END IF;
END $$;