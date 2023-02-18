select 
    Email
from
    (
        SELECT 
            email as Email,
            COUNT(email) as count
        FROM Person
        GROUP BY email
    ) x
where count > 1;