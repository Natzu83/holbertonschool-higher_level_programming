-- A script that lists all records of the table in the second_table
-- Results displayed both in the score and the name (in this order)
-- Records should be ordered by score (top first)
SELECT score, name
FROM second_table
ORDER BY score DESC;