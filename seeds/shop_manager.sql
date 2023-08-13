-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS orders CASCADE;
DROP SEQUENCE IF EXISTS orders_id_seq;

-- Then, we recreate them (table without the foreign key first)
CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name text,
    order_date text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO orders (customer_name, order_date) VALUES ('Aang', '1870-08-01');
INSERT INTO orders (customer_name, order_date) VALUES ('Katara', '1870-06-01');


-- Then create the table with the foreign key second.
DROP TABLE IF EXISTS items CASCADE;
DROP SEQUENCE IF EXISTS items_id_seq;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name text,
    unit_price int,
    quantity int,
    order_id int, 
    constraint fk_order foreign key(order_id)
    references "orders"(id)
    on delete cascade
);

INSERT INTO items (name, unit_price, quantity, order_id) VALUES ('air bison whistle', 5, 1, 1);
INSERT INTO items (name, unit_price, quantity, order_id) VALUES ('waterbending scroll', 50, 1, 2);