-- Creates a table "second_table" in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
-- Inserts the first row
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
-- Inserts the second row
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
-- Inserts the third row
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
-- Inserts the fourth row
INSERT INTO second_table(id, name, score) VALUES (4, "George", 8);
