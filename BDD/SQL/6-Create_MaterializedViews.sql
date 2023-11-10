-- GRANT a b_master -----------------------------------------

CONNECT SYSTEM/fakepassword
GRANT EXECUTE ANY TYPE to b_master;
GRANT CREATE ANY PROCEDURE TO b_master;
GRANT EXECUTE ANY PROCEDURE TO b_master;
GRANT MANAGE SCHEDULER TO b_master;

-- CREATE match local -----------------------------------------

CONNECT b_master/b_master
CREATE MATERIALIZED VIEW B_MASTER.Match BUILD IMMEDIATE REFRESH COMPLETE AS SELECT * FROM B_MASTER.MATCH_GLOBAL WHERE (CODE IN (SELECT MATCH FROM Calendrier));

CONNECT b_region1/b_region1
CREATE MATERIALIZED VIEW B_REGION1.Match BUILD IMMEDIATE REFRESH COMPLETE AS SELECT * FROM B_MASTER.MATCH_GLOBAL@b_region1Tob_master WHERE (CODE IN (SELECT MATCH FROM Calendrier));

CONNECT b_region2/b_region2
CREATE MATERIALIZED VIEW B_REGION2.Match BUILD IMMEDIATE REFRESH COMPLETE AS SELECT * FROM B_MASTER.MATCH_GLOBAL@b_region2Tob_master WHERE (CODE IN (SELECT MATCH FROM Calendrier));

CONNECT b_region3/b_region3
CREATE MATERIALIZED VIEW B_REGION3.Match BUILD IMMEDIATE REFRESH COMPLETE AS SELECT * FROM B_MASTER.MATCH_GLOBAL@b_region3Tob_master WHERE (CODE IN (SELECT MATCH FROM Calendrier));

CONNECT b_region4/b_region4
CREATE MATERIALIZED VIEW B_REGION4.Match BUILD IMMEDIATE REFRESH COMPLETE AS SELECT * FROM B_MASTER.MATCH_GLOBAL@b_region4Tob_master WHERE (CODE IN (SELECT MATCH FROM Calendrier));

-- CREATE Refresh Procedure -----------------------------------------

CONNECT b_master/b_master
CREATE OR REPLACE PROCEDURE RefreshRemoteCalendars AS
BEGIN
    DBMS_MVIEW.REFRESH('b_region1.Match', 'C');
    DBMS_MVIEW.REFRESH('b_region2.Match', 'C');
    DBMS_MVIEW.REFRESH('b_region3.Match', 'C');
    DBMS_MVIEW.REFRESH('b_region4.Match', 'C');
END RefreshRemoteCalendars;
BEGIN
  DBMS_SCHEDULER.create_job (
    job_name        => 'RefreshRemoteCalendarsJob',
    job_type        => 'PLSQL_BLOCK',
    job_action      => 'BEGIN RefreshRemoteCalendars; END;',
    start_date      => SYSTIMESTAMP,
    repeat_interval => 'FREQ=WEEKLY; BYDAY=WED; BYHOUR=15; BYMINUTE=0; BYSECOND=0',
    enabled         => TRUE
  );
END;
BEGIN
    RefreshRemoteCalendars();
end;