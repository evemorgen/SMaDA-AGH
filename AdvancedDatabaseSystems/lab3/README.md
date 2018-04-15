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
