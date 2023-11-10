
CONNECT SYSTEM/fakepassword

-- MASTER user and grant -------------------------------------------------------------------
CREATE USER b_master IDENTIFIED BY b_master;

ALTER USER b_master  QUOTA UNLIMITED ON SYSTEM;

GRANT CREATE ANY TABLE TO b_master;
GRANT CREATE SESSION TO b_master;
GRANT CREATE DATABASE LINK TO b_master;
GRANT CREATE SYNONYM TO b_master;
GRANT CREATE ANY MATERIALIZED VIEW TO b_master;
GRANT CREATE ANY VIEW TO b_master;

GRANT UNLIMITED TABLESPACE TO b_master;
GRANT SELECT ANY TABLE TO b_master;

-- B_REGION1 user and grant -------------------------------------------------------------------
CREATE USER b_region1 IDENTIFIED BY b_region1;

ALTER USER b_region1 QUOTA UNLIMITED ON SYSTEM;

GRANT CREATE ANY TABLE TO b_region1;
GRANT CREATE SESSION TO b_region1;
GRANT CREATE DATABASE LINK TO b_region1;
GRANT CREATE SYNONYM TO b_region1;
GRANT CREATE ANY MATERIALIZED VIEW TO b_region1;
GRANT CREATE ANY VIEW TO b_region1;

GRANT UNLIMITED TABLESPACE TO b_region1;
GRANT SELECT ANY TABLE TO b_region1;

-- B_REGION2 user and grant -------------------------------------------------------------------
CREATE USER b_region2 IDENTIFIED BY b_region2;

ALTER USER b_region2 QUOTA UNLIMITED ON SYSTEM

GRANT CREATE ANY TABLE TO b_region2;
GRANT CREATE SESSION TO b_region2;
GRANT CREATE DATABASE LINK TO b_region2;
GRANT CREATE SYNONYM TO b_region2;
GRANT CREATE ANY MATERIALIZED VIEW TO b_region2;
GRANT CREATE ANY VIEW TO b_region2;

GRANT UNLIMITED TABLESPACE TO b_region2;
GRANT SELECT ANY TABLE TO b_region2;

-- B_REGION3 user, link and grant -------------------------------------------------------------------
CREATE USER b_region3 IDENTIFIED BY b_region3;

ALTER USER b_region3 QUOTA UNLIMITED ON SYSTEM;

GRANT CREATE ANY TABLE TO b_region3;
GRANT CREATE SESSION TO b_region3;
GRANT CREATE DATABASE LINK TO b_region3;
GRANT CREATE SYNONYM TO b_region3;
GRANT CREATE ANY MATERIALIZED VIEW TO b_region3;
GRANT CREATE ANY VIEW TO b_region3;

GRANT UNLIMITED TABLESPACE TO b_region3;
GRANT SELECT ANY TABLE TO b_region3;

-- B_REGION4 user, link and grant -------------------------------------------------------------------
CREATE USER b_region4 IDENTIFIED BY b_region4;

ALTER USER b_region4 QUOTA UNLIMITED ON SYSTEM;

GRANT CREATE ANY TABLE TO b_region4;
GRANT CREATE SESSION TO b_region4;
GRANT CREATE DATABASE LINK TO b_region4;
GRANT CREATE SYNONYM TO b_region4;
GRANT CREATE ANY MATERIALIZED VIEW TO b_region4;
GRANT CREATE ANY VIEW TO b_region4;

GRANT UNLIMITED TABLESPACE TO b_region4;
GRANT SELECT ANY TABLE TO b_region4;

-- Database LINKS  -------------------------------------------------------------------

CREATE DATABASE LINK systemTob_master CONNECT TO b_master IDENTIFIED by b_master using 'localhost:1521/XE';

CONNECT b_master/b_master
CREATE DATABASE LINK b_masterTob_region1 CONNECT TO b_region1 IDENTIFIED by b_region1 using 'localhost:1521/XE';
CREATE DATABASE LINK b_masterTob_region2 CONNECT TO b_region2 IDENTIFIED by b_region2 using 'localhost:1521/XE';
CREATE DATABASE LINK b_masterTob_region3 CONNECT TO b_region3 IDENTIFIED by b_region3 using 'localhost:1521/XE';
CREATE DATABASE LINK b_masterTob_region4 CONNECT TO b_region4 IDENTIFIED by b_region4 using 'localhost:1521/XE';

CONNECT b_region1/b_region1
CREATE DATABASE LINK b_region1Tob_master CONNECT TO b_master IDENTIFIED by b_master using 'localhost:1521/XE';

CONNECT b_region2/b_region2
CREATE DATABASE LINK b_region2Tob_master CONNECT TO b_master IDENTIFIED by b_master using 'localhost:1521/XE';

CONNECT b_region3/b_region3
CREATE DATABASE LINK b_region3Tob_master CONNECT TO b_master IDENTIFIED by b_master using 'localhost:1521/XE';

CONNECT b_region4/b_region4
CREATE DATABASE LINK b_region4Tob_master CONNECT TO b_master IDENTIFIED by b_master using 'localhost:1521/XE';