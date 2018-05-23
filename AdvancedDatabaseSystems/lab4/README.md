# ADS Lab 4
## Posgresql Transactions

Exercises:
  - Exercise 1: non-repeatable reads
```
-- terminal 1
galcpatr=> create table x (a integer, b integer);
CREATE TABLE
galcpatr=> begin transaction isolation level READ commited;
ERROR:  syntax error at or near "commited"
LINE 1: begin transaction isolation level READ commited;
                                               ^
galcpatr=> begin transaction isolation level READ;
ERROR:  syntax error at or near ";"
LINE 1: begin transaction isolation level READ;
                                              ^
galcpatr=> BEGIN TRANSACTION ISOLATION LEVEL READ committed;
BEGIN
galcpatr=> INSERT INTO x VALUES (1, 2);
INSERT 0 1
galcpatr=> rollback;
ROLLBACK
galcpatr=>
```

```
-- terminal 2
galcpatr=> BEGIN TRANSACTION ISOLATION LEVEL READ committed;
BEGIN
galcpatr=> commit;
COMMIT
galcpatr=> rollback;
WARNING:  there is no transaction in progress
ROLLBACK
```
  - Exercise 2: explicit locking
```
-- terminal 1
galcpatr=> BEGIN TRANSACTION ISOLATION LEVEL READ committed;
BEGIN
galcpatr=> select * from public.x for update;
 a | b
---+---
 1 | 2
(1 row)

galcpatr=> update public.x SET
a  b
galcpatr=> update public.x SET b = 2 where a = 1;
UPDATE 1
galcpatr=> update public.x SET b = 3 where a = 1;
UPDATE 1
galcpatr=> commit;
COMMIT
```

```
galcpatr=> select * from public.x ;
 a | b
---+---
 1 | 2
(1 row)

galcpatr=> select * from public.x ;
 a | b
---+---
 1 | 2
(1 row)

galcpatr=> select * from public.x ;
 a | b
---+---
 1 | 3
(1 row)
```
  - Exercise 3: repeatable read isolation level
  - Exercise 4: MVCC in PostgreSQL
  - Exercise 5: serialisation errors
  - Exercise 6: record-level locks
  - Exercise 7: true serialisation
