
/* ToC

A)Cleaning the data
	1) Replace nulls,blanks with 0s
	2) Create temporary table containing only the Greek records
	3)Create temporary table containing only the Greek records for the last six months
B) Last six months in Greece
	1) Number of total deaths.
	2) Number of new deaths.
	3) Average number of new deaths per day.
	4) Highest number of new deaths per day
	5) Number of deaths per day on October 2021.
	6) Current vaccinated percentage of the population.

C) Additional metrics
	01) Average number of  new deaths for each of the last six months
	02) Which months was the percentage of the vaccinated under 20 perecent?
	
*/




----------------------------------------------------------------A) Cleaning the data--------------------------------------------------------------

--1) Replace nulls,blanks with 0

UPDATE [dbo].[owid-covid-data]
SET [total_deaths] = 0
WHERE [total_deaths] IS NULL 
OR [total_deaths] = ' '

--2) Create temporary table containing only the Greek records

DROP TABLE IF EXISTS #PortfolioCovid
USE PortfolioCovid 
SELECT *
INTO #CovidGreece
FROM PortfolioCovid..[owid-covid-data] 
WHERE Location = 'Greece'
AND continent is not null

--3) Create temporary table containing only the Greek records for the last six months


DROP TABLE IF EXISTS #PortfolioCovid6 --Remove the previously created temp table in case the query is re-executed
USE PortfolioCovid 
SELECT *
INTO #CovidGreece6
FROM PortfolioCovid..[owid-covid-data] 
WHERE Location = 'Greece'
	AND continent is not null
	AND date > dateadd(m,-6,getdate()  --date > 2021-05-01
	-datepart(d,getdate())) 
	AND date < getdate() --date < 2021-10-31
	-datepart(d,getdate())  
-- AND date < 2021-11-01





----------------------------------------------------------------B) Last six months in Greece--------------------------------------------------------------

--1) Number of total deaths.

SELECT	
MAX(Cast(total_deaths as float)) as total_deaths
FROM #CovidGreece6
	
--2) Number of new deaths

SELECT	
Sum(Cast(new_deaths as float)) as new_deaths_sum
FROM #CovidGreece6

--3) Average number of new deaths each day

SELECT 	
cast(
Avg(Cast(new_deaths as float)) as decimal) as aver_deaths_6mo --Round the average of deaths by casting as decimal
FROM #CovidGreece6

4) Highest number of new deaths per day

SELECT 	
cast(
Max(Cast(new_deaths as float)) as decimal) as max_deaths_6mo 
FROM #CovidGreece6

5) Number of deaths per day on October 2021.

SELECT Date, Location, total_deaths
FROM #CovidGreece
WHERE MONTH(Date) = 10
AND YEAR(Date) = 2021

6) Vaccinated percentage of the population

SELECT
Cast(
MAX(
(Cast(people_vaccinated as float))/ (Cast (population as float))
)  * 100  as decimal) as vac_to_pop_ratio
FROM #CovidGreece


--01)Which months was the percentage of the vaccinated under 20 perecent?



--With statement with Vac_CTE as (

SELECT 
CAST(
MAX(
	(Cast(people_vaccinated as float))
	/ (Cast (population as float))
	) as decimal(10,2))
* 100 
as vactopop 
FROM #CovidGreece
GROUP BY MONTH(DATE)
)
Select cast (vactopop as float)
from Vac_CTE
WHERE vactopop < 20

--WHERE vactopop  < 20.00
--GROUP BY MONTH(date)






--02) Average number of  new deaths for each of the last six months

SELECT cast(
AVG(CAST(new_deaths as float)) as DECIMAL) as months 
FROM #CovidGreece6
WHERE MONTH(DATE) != 11  --exclude november
GROUP BY MONTH(DATE)


