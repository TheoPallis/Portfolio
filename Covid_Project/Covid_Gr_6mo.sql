
/* ToC

A)Cleaning the data
	1) Replace nulls,blanks with 0s
	2) Create temporary table containing only the Greek records
	3) Create temporary table containing only the Greek records for the last six months
B) Last six months in Greece
	1) Number of total deaths.
	2) Number of new deaths.
	3) Average number of new deaths per day.
	4) Highest number of new deaths per day
	5) Number of deaths per day on October 2021.
	6) Current vaccinated percentage of the population.
	7) Average number of  new deaths for each of the last six months
	8) Which months was the percentage of the vaccinated under 20 perecent?
	
*/




----------------------------------------------------------------A) Cleaning the data--------------------------------------------------------------

--1) Replace nulls,blanks with 0

UPDATE [dbo].[owid-covid-data]
SET [total_deaths] = 0
WHERE [total_deaths] IS NULL 
OR [total_deaths] = ' '

--2) Create temporary table containing only the Greek records

DROP TABLE IF EXISTS #CovidGreece
USE Covid_Db
SELECT *
INTO #CovidGreece
FROM Covid_Db..[owid-covid-data] 
WHERE Location = 'Greece'
AND continent is not null

-- View contents of temp table sorted by latest date

SELECT * 
FROM #CovidGreece
ORDER BY DATE DESC

--3) Create temporary table containing only the Greek records for the last six months

DROP TABLE IF EXISTS #CovidGreece6 --Remove the previously created temp table in case the query is re-executed
USE Covid_Db
SELECT *
INTO #CovidGreece6
FROM Covid_Db..[owid-covid-data] 
WHERE Location = 'Greece'
	AND continent is not null
	AND date > dateadd(m,-6,getdate())              --> Substract 7 months from current date
	- datepart(d,getdate())			                --> Substract current date's number of days to reach the beginning of the starting  month 
                                                    --> Starting date : 0q-07-021
	AND date < getdate() -datepart(d,getdate()-1)   --> Likewise, to reach the beginning of the ending month ( substract 1 to include 01-01-2022)

-- View contents of temp table sorted by latest date

SELECT *
FROM #CovidGreece6
order by date asc

----------------------------------------------------------------B) Last six months in Greece--------------------------------------------------------------

----1) Number of total deaths.

SELECT	
MAX(Cast(total_deaths as float)) as total_deaths
FROM #CovidGreece6
	
----2) Number of new deaths

SELECT	
Sum(Cast(new_deaths as float)) as new_deaths_sum
FROM #CovidGreece6

--3) Average number of new deaths each day

SELECT 	
cast(
Avg(Cast(new_deaths as float)) as int) as aver_deaths_day --Round the average of deaths by casting as decimal
FROM #CovidGreece6

-- 4) Highest number of new deaths per day

SELECT 	
cast(
Max(Cast(new_deaths as float)) as int) as max_deaths_day
FROM #CovidGreece6

-- 5) Number of deaths per day on December 2021.

SELECT Date, Location, total_deaths
FROM #CovidGreece
WHERE MONTH(Date) = 12
AND YEAR(Date) = 2021

-- 6) Vaccinated percentage of the population

SELECT
Cast(
MAX(
(Cast(people_vaccinated as float))/ (Cast (population as float))
)  * 100  as decimal) as vac_to_pop_ratio
FROM #CovidGreece

-- 7) Average number of  new deaths for each of the last six months

SELECT month(date), cast(
AVG(CAST(new_deaths as float)) 
as DECIMAL)
as avg_new_deaths_months 
FROM #CovidGreece6
WHERE MONTH(DATE)!= month(getdate())
GROUP BY MONTH(DATE)



-- 8) Which months in 2021 was the percentage of the vaccinated under 20 perecent?

--With statement 

With Vac_CTE (vactopop, months) as (
SELECT 
CAST(
MAX(
(Cast(people_vaccinated as float))
/ (Cast (population as float))
	) as decimal(10,2))
* 100, month(date) 
FROM #CovidGreece
GROUP BY MONTH(DATE)
)

SELECT cast (vactopop as float), months
FROM Vac_CTE
WHERE cast (vactopop as float)  < 20.00








