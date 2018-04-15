## Lab 3 - creating indexes

### Disclaimer - I'm running Postgres 10 in Docker

1. Load data
  - easy enough
  - `cat 1-ascii.sql| PGPASSWORD=mysecretpassword psql -h localhost -U postgres`
  - `cat 3-ascii.sql| PGPASSWORD=mysecretpassword psql -h localhost -U postgres`
  - 
```
postgres=# \d
            List of relations
 Schema |     Name     | Type  |  Owner
--------+--------------+-------+----------
 public | clients      | table | postgres
 public | compositions | table | postgres
 public | orders       | table | postgres
 public | recipients   | table | postgres
(4 rows)
```

2. Meet my friends:
  - ANALYZE - this command help Postgres to learn about your data, and optimize its queries against it. We can analyze `tables` or `columns`. [Docs](https://www.postgresql.org/docs/9.1/static/sql-analyze.html)
  - EXPLAIN - shows us query plan - that is how postgres handles provided query, what indexes it uses, estimates time etc. [Docs](https://www.postgresql.org/docs/9.1/static/using-explain.html)

3. Jump into it:
  - Hash-based indexes
    - Execute a query which displays all orders for the buk1 composition. Check the execution plan and take note of the execution times.  
```
postgres=# explain select * from orders where composition_id like 'buk1%';
                        QUERY PLAN
-----------------------------------------------------------
 Seq Scan on orders  (cost=0.00..167.19 rows=424 width=52)
   Filter: (composition_id ~~ 'buk1%'::text)
```
