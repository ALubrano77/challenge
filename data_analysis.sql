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
			e."ID" as id, sum(coalesce (e."DistanceTravelled_5",0)) as "DistanceTravelled_bike" 
			,row_number() over ( order by sum(coalesce (e."DistanceTravelled_5",0)) desc )   as rn			
		from public."84710e_tds_vw" e 			
		join regioncharacteristics r ON r."Key" =e."RegionCharacteristics" 
		join travelmodes td on td."Key" = e."TravelModes" 
		join travelmotives tt on tt."Key" = e."TravelMotives" 
		join periods pe on pe."Key" =e."Periods"
		where 1=1
		and td."Title" = 'Bike'
		and pe."Title" = '2022'
		and tt."Title"  != 'Total'
		group by e."ID" 
		order by 2 desc )
		as x
	where x.rn <= 8
	)
select tt."Title" , tb.id, sum("Trips_4")
from public."84710e_tds_vw" e 
--join margins m on m."Key" =e."Margins" 
join periods pe on pe."Key" =e."Periods"
--join population po on po."Key" =e."Population" 
--join regioncharacteristics r ON r."Key" =e."RegionCharacteristics" 
--join travelmodes td on td."Key" = e."TravelModes" 
join travelmotives tt on tt."Key" = e."TravelMotives" 
join top10_bike tb on tb.id = e."ID" 
where pe."Title" = '2022'
--and tt."Title"  != 'Total'
group by tt."Title" , tb.id
--order by 2 desc
--limit 3
;
-- non mi torna:
-- chiede gli utenti ma non ci sono utenti, solo aggregazioni per datamart
-- inoltre data la natura di datamart, se uso l'ID il travelmotives più comune sarà sempre Total
-- se elimino il Total non sono sicuro del risultato perchè confronto per ID e quindi anche per motivo e non per User


select *
from public."84710e_tds_vw" e 
join travelmodes td on td."Key" = e."TravelModes" 
where 1=1
		and td."Title" = 'Bike'
;



--* Among the top 10 users who spend the least number of hours travelling to attend education/courses, show for every year the average number of trips made by these users.


