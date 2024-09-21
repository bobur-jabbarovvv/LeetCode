SELECT user_id, name, mail
FROM Users
WHERE mail LIKE '%@leetcode.com'  -- Must end with '@leetcode.com'
    AND mail REGEXP '^[A-Za-z]'    -- Must start with a letter
    AND mail REGEXP '^[A-Za-z0-9._-]*@[A-Za-z0-9.-]+$'; -- May contain
