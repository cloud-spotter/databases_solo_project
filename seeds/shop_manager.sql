-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- Create orders table
DROP TABLE IF EXISTS orders CASCADE;
DROP SEQUENCE IF EXISTS orders_id_seq;
CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name text,
    order_date text
);

-- Create items table
DROP TABLE IF EXISTS items CASCADE;
DROP SEQUENCE IF EXISTS items_id_seq;
CREATE SEQUENCE IF NOT EXISTS items_id_seq;
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name text,
    unit_price int,
    quantity int 
);

-- Create relationships table
DROP TABLE IF EXISTS items_orders CASCADE;
CREATE TABLE items_orders (
    item_id int,
    order_id int,
    -- TODO: Allow multiple of an item in an order.
    constraint fk_item foreign key(item_id) references items(id) ON DELETE CASCADE,
    constraint fk_order foreign key(order_id) references orders(id) ON DELETE CASCADE,
    PRIMARY KEY (item_id, order_id)
);

-- Add items
INSERT INTO items (name, unit_price, quantity) VALUES ('air bison whistle', 5, 1);
INSERT INTO items (name, unit_price, quantity) VALUES ('waterbending scroll', 50, 1);

-- Add metadata for each order
INSERT INTO orders (customer_name, order_date) VALUES ('Aang', '1870-08-01');
INSERT INTO orders (customer_name, order_date) VALUES ('Katara', '1870-06-01');

-- Add which items are in each order
INSERT INTO items_orders (item_id, order_id) VALUES (1, 1);
INSERT INTO items_orders (item_id, order_id) VALUES (2, 2);