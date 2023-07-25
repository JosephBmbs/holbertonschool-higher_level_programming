-- SQL script to list all records of 'second_table' excluding rows without a 'name' value,
-- displaying the score and name in descending order of score.

SELECT score, name FROM `second_table`
WHERE name IS NOT NULL
ORDER BY score DESC;
