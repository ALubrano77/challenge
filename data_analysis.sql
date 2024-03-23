/*
**Third task**
Test your database by writing queries to answer as closely as possible the following questions:
* Total number of trips across all the years, grouped by travel method and by level of urbanization for
people who went shopping for groceries
* Top 10 users based in west Netherlands, who travelled the most by bike (in terms of km) to go to
work
* Among the top 8 users who travel the most km by bike, show the 3 least common reasons for
travelling in year 2022
* Among the top 10 users who spend the least number of hours travelling to attend education/courses,
show for every year the average number of trips made by these users.
*/


--* Total number of trips across all the years, grouped by travel method and by level of urbanization for people who went shopping for groceries
select 
	sum(e."Trips_4") 
	, td."Title" , r."Title" 
from public."84710e_tds_vw" e 
join margins m on m."Key" =e."Margins" 
join periods pe on pe."Key" =e."Periods"
join population po on po."Key" =e."Population" 
join regioncharacteristics r ON r."Key" =e."RegionCharacteristics" 
join travelmodes td on td."Key" = e."TravelModes" 
join travelmotives tt on tt."Key" = e."TravelMotives" 
where tt."Title" = 'Shopping, groceries, funshopping.'
and r."Title" like '%urban%'
group by td."Title" , r."Title" 
;

--* Top 10 users based in west Netherlands, who travelled the most by bike (in terms of km) to go to work   
select 
	e."ID" , sum(e."DistanceTravelled_5") as "DistanceTravelled_bike" 
from public."84710e_tds_vw" e 
join margins m on m."Key" =e."Margins" 
join periods pe on pe."Key" =e."Periods"
join population po on po."Key" =e."Population" 
join regioncharacteristics r ON r."Key" =e."RegionCharacteristics" 
join travelmodes td on td."Key" = e."TravelModes" 
join travelmotives tt on tt."Key" = e."TravelMotives" 
where r."Title" = 'West-Nederland (LD)'
and td."Title" = 'Bike'
and tt."Title" = 'Travel to/from work, (non)-daily commute'
group by e."ID" 
order by 2 desc
limit 10
;

--* Among the top 8 users who travel the most km by bike, show the 3 least common reasons for travelling in year 2022
with top10_bike as (
	select x.id 
	from (
		select 
			e."ID" as id, sum(e."DistanceTravelled_5") as "DistanceTravelled_bike" 
			,row_number() over ( order by sum(e."DistanceTravelled_5") desc )   as rn			
		from public."84710e_tds_vw" e 			
		join regioncharacteristics r ON r."Key" =e."RegionCharacteristics" 
		join travelmodes td on td."Key" = e."TravelModes" 
		join travelmotives tt on tt."Key" = e."TravelMotives" 
		where r."Title" = 'West-Nederland (LD)'
		and td."Title" = 'Bike'
		and tt."Title" = 'Travel to/from work, (non)-daily commute'
		group by e."ID" 
		order by 2 desc )
		as x
	where x.rn <= 10 
	)
select pe."Title"  ---- ????????????????????  2018-2019  ??????????????
from public."84710e_tds_vw" e 
join margins m on m."Key" =e."Margins" 
join periods pe on pe."Key" =e."Periods"
join population po on po."Key" =e."Population" 
join regioncharacteristics r ON r."Key" =e."RegionCharacteristics" 
join travelmodes td on td."Key" = e."TravelModes" 
join travelmotives tt on tt."Key" = e."TravelMotives" 
join top10_bike tb on tb.id = e."ID" 
--where pe."Title" = '2022'

;




--* Among the top 10 users who spend the least number of hours travelling to attend education/courses, show for every year the average number of trips made by these users.


