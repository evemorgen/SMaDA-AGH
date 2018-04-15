## Lab 3 - creating indexes

### Disclaimer - I'm running Postgres 10 in Docker

## 1. Load data
  - easy enough
  - `cat 1-ascii.sql| PGPASSWORD=mysecretpassword psql -h localhost -U postgres`
  - `cat 3-ascii.sql| PGPASSWORD=mysecretpassword psql -h localhost -U postgres`
  - `postgres=# \d`
```
            List of relations
 Schema |     Name     | Type  |  Owner
--------+--------------+-------+----------
 public | clients      | table | postgres
 public | compositions | table | postgres
 public | orders       | table | postgres
 public | recipients   | table | postgres
(4 rows)
```

## 2. Meet my friends:
  - ANALYZE - this command help Postgres to learn about your data, and optimize its queries against it. We can analyze `tables` or `columns`. [Docs](https://www.postgresql.org/docs/9.1/static/sql-analyze.html)
  - EXPLAIN - shows us query plan - that is how postgres handles provided query, what indexes it uses, estimates time etc. [Docs](https://www.postgresql.org/docs/9.1/static/using-explain.html)

## 3. Jump into it:
1. Hash-based indexes 
  - Execute a query which displays all orders for the buk1 composition. Check the execution plan and take note of the execution times.  
```
postgres=# explain select * from orders where composition_id = 'buk1 ';
                        QUERY PLAN
-----------------------------------------------------------
 Seq Scan on orders  (cost=0.00..167.19 rows=424 width=52)
   Filter: (composition_id = 'buk1 '::bpchar)
(2 rows)
```
    
  -  [Add a hash-based index](https://www.postgresql.org/docs/9.1/static/sql-createindex.html) which can accelerate the aforementioned query to the orders table. Take note of the plan and execution plan.

```
postgres=# create index composition_id_hash_idx on orders using hash (composition_id);
CREATE INDEX
postgres=# explain select * from orders where composition_id = 'buk1 ';
                                       QUERY PLAN
-----------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=15.29..87.59 rows=424 width=52)
   Recheck Cond: (composition_id = 'buk1 '::bpchar)
   ->  Bitmap Index Scan on composition_id_hash_idx  (cost=0.00..15.18 rows=424 width=0)
         Index Cond: (composition_id = 'buk1 '::bpchar)
(4 rows)
```  

  - we are using `=` operator, when checking for `buk1` because `hash index` can only handle check for equality

2. B-tree indexes
- Delete the index created in the previous exercise and create a similar one, but using B-trees. Repeat the previous query and take a note of the results.
```
postgres=# drop index composition_id_hash_idx;
DROP INDEX
postgres=# create index composition_id_btree_idx on orders using btree (composition_id);
CREATE INDEX
postgres=# explain select * from orders where composition_id = 'buk1 ';
                                        QUERY PLAN
------------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=11.57..83.87 rows=424 width=52)
   Recheck Cond: (composition_id = 'buk1 '::bpchar)
   ->  Bitmap Index Scan on composition_id_btree_idx  (cost=0.00..11.46 rows=424 width=0)
         Index Cond: (composition_id = 'buk1 '::bpchar)
(4 rows)
```  

- Execute a query displaying orders of all compositions with IDs beginning with letters appearing before the letter 'b' in the alphabet. Is the index in use? - YEP IT IS
```
postgres=# explain select * from orders where composition_id < 'c';
                                        QUERY PLAN
-------------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=39.39..130.77 rows=1950 width=52)
   Recheck Cond: (composition_id < 'c'::bpchar)
   ->  Bitmap Index Scan on composition_id_btree_idx  (cost=0.00..38.91 rows=1950 width=0)
         Index Cond: (composition_id < 'c'::bpchar)
```  

- Run another query, displaying the remaining orders (beginning with 'b' and so on). Is the index in use now? - NOPE IT IS NOT
```
postgres=# explain select * from orders where composition_id > 'c';
                         QUERY PLAN
------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..167.19 rows=6065 width=52)
   Filter: (composition_id > 'c'::bpchar)
(2 rows)
```  

- Try forcing the use of indexes by switching the enable_seqscan parameter:
```
postgres=# SET ENABLE_SEQSCAN TO OFF;
SET
postgres=# explain select * from orders where composition_id > 'c';
                                         QUERY PLAN
--------------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=123.29..266.10 rows=6065 width=52)
   Recheck Cond: (composition_id > 'c'::bpchar)
   ->  Bitmap Index Scan on composition_id_btree_idx  (cost=0.00..121.77 rows=6065 width=0)
         Index Cond: (composition_id > 'c'::bpchar)
(4 rows)
```  

- This will "encourage" PostgreSQL to use indexes – this kind of optimisation may be useful when using mass storage with short seek times, such as SSD drives. Repeat the two queries and compare their execution plans and times. **YEAH, THATS COOL**


3. Indexes and pattern matching
- Create an index for the remarks column and query the database for all orders with remarks beginning with the "do" string. Is the index in use? **NOPE**
```
postgres=# create index remarks_btree_idx on orders using btree (remarks);
CREATE INDEX
postgres=# explain select * from orders where remarks ~ '^do';
                                 QUERY PLAN
----------------------------------------------------------------------------
 Seq Scan on orders  (cost=10000000000.00..10000000167.19 rows=10 width=52)
   Filter: ((remarks)::text ~ '^do'::text)
(2 rows)
```

- Delete the index and create a new one, but this time explicitly set its operator class (varchar_pattern_ops):
```
postgres=# drop index remarks_btree_idx;
DROP INDEX
postgres=# CREATE INDEX orders_remarks_idx ON orders (remarks varchar_pattern_ops);
CREATE INDEX
postgres=# explain select * from orders where remarks ~ '^do';
                                          QUERY PLAN
----------------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=4.40..35.16 rows=11 width=52)
   Filter: ((remarks)::text ~ '^do'::text)
   ->  Bitmap Index Scan on orders_remarks_idx  (cost=0.00..4.39 rows=11 width=0)
         Index Cond: (((remarks)::text ~>=~ 'do'::text) AND ((remarks)::text ~<~ 'dp'::text))
(4 rows)
```

- Repeat the exercise and compare the results. **YEP THIS TIME IT IS USING INDEX**

4. Multi-column indexes
- Create a multi-column index covering the client_id, recipient_id and composition_id columns.
```
postgres=# create index on orders (client_id, recipient_id, composition_id);
CREATE INDEX
```
- Choose one value existing in these columns and run:
  - a query which joins the constraints for the three columns using the AND operator,
  - a similar query, but using OR.

```
postgres=# explain select * from orders where client_id = 'msowins' and recipient_id = 1 and composition_id = 'buk1 ';
                                                     QUERY PLAN
---------------------------------------------------------------------------------------------------------------------
 Index Scan using orders_client_id_recipient_id_composition_id_idx on orders  (cost=0.28..8.30 rows=1 width=52)
   Index Cond: (((client_id)::text = 'msowins'::text) AND (recipient_id = 1) AND (composition_id = 'buk1 '::bpchar))
(2 rows)
postgres=# explain select * from orders where client_id = 'msowins' or recipient_id = 1 or composition_id = 'buk1 ';
                                                       QUERY PLAN
-------------------------------------------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=462.91..545.17 rows=843 width=52)
   Recheck Cond: (((client_id)::text = 'msowins'::text) OR (recipient_id = 1) OR (composition_id = 'buk1 '::bpchar))
   ->  BitmapOr  (cost=462.91..462.91 rows=872 width=0)
         ->  Bitmap Index Scan on orders_client_id_recipient_id_composition_id_idx  (cost=0.00..5.49 rows=161 width=0)
               Index Cond: ((client_id)::text = 'msowins'::text)
         ->  Bitmap Index Scan on orders_client_id_recipient_id_composition_id_idx  (cost=0.00..228.40 rows=287 width=0)
               Index Cond: (recipient_id = 1)
         ->  Bitmap Index Scan on orders_client_id_recipient_id_composition_id_idx  (cost=0.00..228.40 rows=424 width=0)
               Index Cond: (composition_id = 'buk1 '::bpchar)
(9 rows)
```

- Now query the database for all orders of the buk1 composition.
```
postgres=# explain select * from orders where composition_id = 'buk1 ';
                                                    QUERY PLAN
-------------------------------------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=228.50..300.80 rows=424 width=52)
   Recheck Cond: (composition_id = 'buk1 '::bpchar)
   ->  Bitmap Index Scan on orders_client_id_recipient_id_composition_id_idx  (cost=0.00..228.40 rows=424 width=0)
         Index Cond: (composition_id = 'buk1 '::bpchar)
(4 rows)
```
- Remove the index and create separate indexes for each of the three columns. Re-run the previous queries and compare the results.
```
postgres=# drop index orders_client_id_recipient_id_composition_id_idx;
DROP INDEX
postgres=# create index client_id_idx ON orders (client_id);
CREATE INDEX
postgres=# create index recipient_id_idx ON orders (recipient_id);
CREATE INDEX
postgres=# create index composition_id_idx ON orders (composition_id);
CREATE INDEX

postgres=# explain select * from orders where client_id = 'msowins' and recipient_id = 1 and composition_id = 'buk1 ';
                                                      QUERY PLAN
-----------------------------------------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=23.89..27.91 rows=1 width=52)
   Recheck Cond: (((client_id)::text = 'msowins'::text) AND (recipient_id = 1) AND (composition_id = 'buk1 '::bpchar))
   ->  BitmapAnd  (cost=23.89..23.89 rows=1 width=0)
         ->  Bitmap Index Scan on client_id_idx  (cost=0.00..5.49 rows=161 width=0)
               Index Cond: ((client_id)::text = 'msowins'::text)
         ->  Bitmap Index Scan on recipient_id_idx  (cost=0.00..6.43 rows=287 width=0)
               Index Cond: (recipient_id = 1)
         ->  Bitmap Index Scan on composition_id_idx  (cost=0.00..11.46 rows=424 width=0)
               Index Cond: (composition_id = 'buk1 '::bpchar)
(9 rows)

postgres=# explain select * from orders where client_id = 'msowins' or recipient_id = 1 or composition_id = 'buk1 ';
                                                     QUERY PLAN
---------------------------------------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=24.02..106.28 rows=843 width=52)
   Recheck Cond: (((client_id)::text = 'msowins'::text) OR (recipient_id = 1) OR (composition_id = 'buk1 '::bpchar))
   ->  BitmapOr  (cost=24.02..24.02 rows=872 width=0)
         ->  Bitmap Index Scan on client_id_idx  (cost=0.00..5.49 rows=161 width=0)
               Index Cond: ((client_id)::text = 'msowins'::text)
         ->  Bitmap Index Scan on recipient_id_idx  (cost=0.00..6.43 rows=287 width=0)
               Index Cond: (recipient_id = 1)
         ->  Bitmap Index Scan on composition_id_idx  (cost=0.00..11.46 rows=424 width=0)
               Index Cond: (composition_id = 'buk1 '::bpchar)
(9 rows)

postgres=# explain select * from orders where composition_id = 'buk1 ';
                                     QUERY PLAN
------------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=11.57..83.87 rows=424 width=52)
   Recheck Cond: (composition_id = 'buk1 '::bpchar)
   ->  Bitmap Index Scan on composition_id_idx  (cost=0.00..11.46 rows=424 width=0)
         Index Cond: (composition_id = 'buk1 '::bpchar)
(4 rows)
```

5. Indexes and sorting
- Run a query which returns all orders sorted by their composition ID. Is the index in use? **I GUESS?**
```
postgres=# explain select * from orders order by composition_id ;
                                      QUERY PLAN
---------------------------------------------------------------------------------------
 Index Scan using composition_id_idx on orders  (cost=0.28..484.02 rows=8015 width=52)
(1 row)
```

- Now delete the index and repeat the query. Compare results. **DEFINITLY NOT**
```
postgres=# drop index composition_id_idx ;
DROP INDEX
postgres=# explain select * from orders order by composition_id ;
                                     QUERY PLAN
------------------------------------------------------------------------------------
 Sort  (cost=10000000666.86..10000000686.90 rows=8015 width=52)
   Sort Key: composition_id
   ->  Seq Scan on orders  (cost=10000000000.00..10000000147.15 rows=8015 width=52)
(3 rows)
```
- Drop all indexes. **YEP**
```
postgres=# DROP INDEX client_id_idx, recipient_id_idx;
DROP INDEX
```

6. Partial indexes
- Create an index on the client_id column, but only for orders which have been paid. Check it by retrieving all paid orders for a given client. Repeat the query for unpaid orders.
```
postgres=# create index client_id_idx ON orders (client_id) where paid = true;
CREATE INDEX
postgres=# explain select * from orders where client_id = 'msowins' and paid = true;
                                  QUERY PLAN
------------------------------------------------------------------------------
 Bitmap Heap Scan on orders  (cost=5.53..74.54 rows=161 width=52)
   Recheck Cond: (((client_id)::text = 'msowins'::text) AND paid)
   ->  Bitmap Index Scan on client_id_idx  (cost=0.00..5.49 rows=161 width=0)
         Index Cond: ((client_id)::text = 'msowins'::text)
(4 rows)

postgres=# explain select * from orders where client_id = 'msowins' and paid = false;
                                QUERY PLAN
---------------------------------------------------------------------------
 Seq Scan on orders  (cost=10000000000.00..10000000167.19 rows=1 width=52)
   Filter: ((NOT paid) AND ((client_id)::text = 'msowins'::text))
(2 rows)
```
- Now calculate the sum of all unpaid orders. Is the index in use? **YES AND NO**
```
postgres=# explain select sum(price) from orders where client_id = 'msowins' and paid = true;
                                     QUERY PLAN
------------------------------------------------------------------------------------
 Aggregate  (cost=74.95..74.96 rows=1 width=32)
   ->  Bitmap Heap Scan on orders  (cost=5.53..74.54 rows=161 width=5)
         Recheck Cond: (((client_id)::text = 'msowins'::text) AND paid)
         ->  Bitmap Index Scan on client_id_idx  (cost=0.00..5.49 rows=161 width=0)
               Index Cond: ((client_id)::text = 'msowins'::text)
(5 rows)

postgres=# explain select sum(price) from orders where client_id = 'msowins' and paid = false;
                                   QUERY PLAN
--------------------------------------------------------------------------------
 Aggregate  (cost=10000000167.19..10000000167.20 rows=1 width=32)
   ->  Seq Scan on orders  (cost=10000000000.00..10000000167.19 rows=1 width=5)
         Filter: ((NOT paid) AND ((client_id)::text = 'msowins'::text))
(3 rows)
```

7. Indexes on expressions
- Create an index and write a query which retrieves clients living in a city which begins with a given string (e.g. "krak"), regardless of the case (e.g. "krak"="Krak"="KRAK", etc.).
```
postgres=# create index ON clients (lower(city));
CREATE INDEX
postgres=# explain select * from clients where lower(city) = 'krakow';
                                    QUERY PLAN
-----------------------------------------------------------------------------------
 Index Scan using clients_lower_idx on clients  (cost=0.14..8.16 rows=1 width=121)
   Index Cond: (lower((city)::text) = 'krakow'::text)
(2 rows)
postgres=# explain select * from clients where lower(city) ~ 'krakow';
                                 QUERY PLAN
-----------------------------------------------------------------------------
 Seq Scan on clients  (cost=10000000000.00..10000000001.75 rows=1 width=121)
   Filter: (lower((city)::text) ~ 'krakow'::text)
(2 rows)
```
- Check if the index runs properly. **SO IT WORKS BUT ONLY WITH `=` COMPARASION**

8. GiST indexes
- Add a column called location of type point to the orders table. Populate this column with random data within the (0,0)–(100,100) range:
```
postgres=# ALTER TABLE orders ADD COLUMN location point;
ALTER TABLE
postgres=# UPDATE orders SET location=point(random()*100, random()*100);
UPDATE 8015
```
- Write queries, which:
  - retrieve all orders within 10 units from the city centre (50, 50), **IM UNABLE TO INSTALL GIST SO SCREW IT :)**
  - retrieve all orders for the north-west quarter of the city.

- Check the execution plan and times.
- Create a GiST index supporting these queries and repeat the analysis.




