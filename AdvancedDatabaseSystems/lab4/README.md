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
