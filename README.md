# TeleBot
```bash
Zz0xOis9NiBWCAAeCB9IEAIJHR9ICggaBhcKHEseRQQQGxwdBg8dEBBFBhYAczcnPCIqJj9YS11LRVdpNicrJSQ0KEQXAAUTEBgfARtnPTE6NiEgJlYEDwMYFwgKHG8wKTopLCogMiwgIUkqMzc+JkJUADEGMVoCFwoRLCwwFCoaHQNzKTssJiszNycuMUQYDRVdDhBRfi8nJjkwPiAsJzFJWlVzLCk6Oig3PEkDAyYrPQQuDhgQHToHNSkhBCALJQo+IwccIz87AjoAJxc9NToHczQgLjsrPTQkKSQmOCA6TyQ9EQQqFDtKUjEwIiZbJhUfSD0wNggtTAEOMAcLFyQ0Bz8gIz8JXXM=
```

### Sample Output:
```                                Teleco AI bot
Enter your user name: jane
Enter your password: 
                                Welcome to Teleco AI bot
----------------------------------------------------------------------------------------------------
Enter your choice:
        1.Show user details
        2.Billing Issues
        3.Network Problems
        5.Plan Recommendations
        6.Usage Insights
        0.Exit
        6
Usage Insights
jane Usage Insights
Describe your query: tell about my uasges

🔹 **Generated SQL Query:**

SELECT
    c.name,
    c.phone_number,
    c.email,
    cr.call_duration,
    cr.call_type,
    cr.call_cost,
    cr.timestamp AS call_timestamp,
    du.data_used_mb,
    du.usage_date,
    b.bill_amount,
    b.payment_status,
    b.bill_date,
    b.due_date,
    sc.issue_type,
    sc.complaint_text,
    sc.status,
    sc.complaint_date
FROM
    Customers c
LEFT JOIN
    CallRecords cr ON c.customer_id = cr.customer_id
LEFT JOIN
    DataUsage du ON c.customer_id = du.customer_id
LEFT JOIN
    Billing b ON c.customer_id = b.customer_id
LEFT JOIN
    ServiceComplaints sc ON c.customer_id = sc.customer_id
WHERE
    c.name LIKE 'jane%';

🗣️ **AI Response:**

Based on our records, Jane Smith, your usage on July 2nd, 2024 included 700 MB of data and a 45-minute incoming call.  Your bill for this period is $30.00 and is currently pending payment.  The due date for your previous bill (issued June 5th, 2024) was June 15th, 2024.  You have an open billing complaint regarding incorrect charges on your last bill, which is currently under investigation.
----------------------------------------------------------------------------------------------------
```