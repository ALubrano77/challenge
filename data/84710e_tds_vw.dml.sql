
create or replace view public."84710e_tds_vw" as
select 
	e."ID" 
	, "TravelMotives", "Population", "TravelModes", "Margins", "RegionCharacteristics", "Periods"
	, case when isNumeric(e."Trips_1") then to_number( e."Trips_1",'99999999.99') else null end "Trips_1"
	, case when isNumeric(e."DistanceTravelled_2") then to_number( e."DistanceTravelled_2",'99999999.99') else null end "DistanceTravelled_2"
	, case when isNumeric(e."TimeTravelled_3") then to_number( e."TimeTravelled_3",'99999999.99') else null end "TimeTravelled_3"
	, case when isNumeric(e."Trips_4") then to_number( e."Trips_4",'99999999.99') else null end "Trips_4"
	, case when isNumeric(e."DistanceTravelled_5") then to_number( e."DistanceTravelled_5",'99999999.99') else null end "DistanceTravelled_5"
	, case when isNumeric(e."TimeTravelled_6") then to_number( e."TimeTravelled_6",'99999999.99') else null end "TimeTravelled_6"
from public."84710ENG_UntypedDataSet" e
;
