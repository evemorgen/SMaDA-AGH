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
=======
# ADS - Spatial Data Postgis

## Project desctiption  
  Spatial data version control system for Neo4j:  
    - git for neo4j changesets  
    - if we can handle spatial data without writing java code  
    - shell scripts are FINE, no gui is required, just md pages with docs  
    - assign things to existing "ways" (roads?) and resolve conflicts when merging new changeset,if there was lamp on a street and:  
        - it gets split - lamp should - assign to both with "temporary" property with warning for user that one have to resolve this conflict (ideal way would be to check by geometry)  
        - when merging with another road, it should assign lamp to new one  
        - when road deleted, all objects should be deleted recursively  
  
  
## Lab dump  

1. Log into server:
```
ssh ads2018@slartibartfast.kis.agh.edu.pl
```

2. Create your own schema, to prevent conflicts
```
create schema pgaczynski;
set search_path TO pgalczynski, public;
```

3. Create table `cities` with name and coordinates
```
create table cities (
    name text,
    coordinate GEOMETRY
);
```

4. Insert 2 cities (montreal and edinburgh in this case)
```
insert into cities values ('montreal', st_geomfromtext('POINT(-73.566667 45.500000)')), ('edinburgh', st_geomfromtext('POINT(-3.188889 55.953056)'));
```

5. Calculate distance between them
```
select st_distance((select coordinate from cities where name = 'montreal'), (select coordinate from cities where name = 'edinburgh'));
   st_distance
------------------
 71.1498279404555
(1 row)
```

6. Because `st_distance` treats points as it were on plain area, yet earth is not flat, hence `ST_DistanceSphere` is needed
```
ads2018=> select ST_DistanceSphere((select coordinate from cities where name = 'montreal'), (select coordinate from cities where name = 'edinburgh'))/1000 as "distance in km";
  distance in km
------------------
 4861.08392394741
(1 row)
```