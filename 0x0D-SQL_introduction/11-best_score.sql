-- Lists all records of the table "second_table" of the database hbtn_0c_0 with score >= 10
-- ordered by score starting with the highest
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score desc;
