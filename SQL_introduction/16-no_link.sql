-- Write a script that lists all records of the table second_table.

-- The script itself

SELECT score, name FROM second_table
    WHERE name IS NOT null
    ORDER BY score DESC;
