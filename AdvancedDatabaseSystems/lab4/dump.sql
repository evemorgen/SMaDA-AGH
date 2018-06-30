psql (9.5.12)
Type "help" for help.

ads2018=> create schema pgaczynski;
CREATE SCHEMA
ads2018=> set search_path TO pgalczynski, public;
SET
ads2018=> CREATE EXTENSION postgis;
ERROR:  extension "postgis" already exists
ads2018=> create table cities (
ads2018(> name text,
ads2018(> coordinate GEOMETRY
ads2018(> );
CREATE TABLE
ads2018=> \d
               List of relations
 Schema |       Name        | Type  |  Owner
--------+-------------------+-------+----------
 public | cities            | table | ads2018
 public | geography_columns | view  | postgres
 public | geometry_columns  | view  | postgres
 public | raster_columns    | view  | postgres
 public | raster_overviews  | view  | postgres
 public | spatial_ref_sys   | table | postgres
(6 rows)

ads2018=> insert into cities values ('montreal', POINT(-73.566667, 45.500000)), ('edinburgh', POINT(-3.188889, 55.953056));
ERROR:  column "coordinate" is of type geometry but expression is of type point
LINE 1: insert into cities values ('montreal', POINT(-73.566667, 45....
                                               ^
HINT:  You will need to rewrite or cast the expression.
ads2018=> insert into cities values ('montreal', st_geofromtext('POINT(-73.566667 45.500000)')), ('edinburgh', st_geofromtext('POINT(-3.188889 55.953056)'));
ERROR:  function st_geofromtext(unknown) does not exist
LINE 1: insert into cities values ('montreal', st_geofromtext('POINT...
                                               ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
ads2018=> select st_geofromtext('POINT(1 1)')
ads2018-> ;
ERROR:  function st_geofromtext(unknown) does not exist
LINE 1: select st_geofromtext('POINT(1 1)')
               ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
ads2018=> insert into cities values ('montreal', st_geomfromtext('POINT(-73.566667 45.500000)')), ('edinburgh', st_geomfromtext('POINT(-3.188889 55.953056)'));
INSERT 0 2
ads2018=> select * from cities ;
   name    |                 coordinate
-----------+--------------------------------------------
 montreal  | 01010000003C2EAA45446452C00000000000C04640
 edinburgh | 0101000000D9976C3CD88209C0D7A02FBDFDF94B40
(2 rows)

ads2018=> select st_distance(select coordinate from cities where name = 'montreal', select coordinate from cities where name = 'edinburgh');
ERROR:  syntax error at or near "select"
LINE 1: select st_distance(select coordinate from cities where name ...
                           ^
ads2018=> select st_distance(mt_c, ed_c) union select coordinates as mt_c from cities where name = 'montreal' union select coordinates as ed_c from cities where name = 'edinburgh';
ERROR:  column "mt_c" does not exist
LINE 1: select st_distance(mt_c, ed_c) union select coordinates as m...
                           ^
ads2018=> select st_distance((select coordinate from cities where name = 'montreal', select coordinate from cities where name = 'edinburgh'));
ERROR:  syntax error at or near ","
LINE 1: ...ect coordinate from cities where name = 'montreal', select c...
                                                             ^
ads2018=> select st_distance((select coordinate from cities where name = 'montreal'), (select coordinate from cities where name = 'edinburgh'));
   st_distance
------------------
 71.1498279404555
(1 row)

ads2018=> select ST_DistanceSphere((select coordinate from cities where name = 'montreal'), (select coordinate from cities where name = 'edinburgh'));
 st_distancesphere
-------------------
  4861083.92394741
(1 row)

ads2018=> select ST_DistanceSphere((select coordinate from cities where name = 'montreal'), (select coordinate from cities where name = 'edinburgh'))/1000 as "distance in km";
  distance in km
------------------
 4861.08392394741
(1 row)

ads2018=>
