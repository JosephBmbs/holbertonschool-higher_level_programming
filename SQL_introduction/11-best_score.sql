-- SQL script to list all records with a score >= 10 in 'second_table' of the specified database, ordered by score.

SELECT score, name FROM `second_table` WHERE score >= 10 ORDER BY score DESC;
