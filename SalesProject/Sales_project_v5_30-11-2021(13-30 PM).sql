/* ToC
1) Cleaning
	A) Check for typos
	B) Check for nulls
	C)Check for blanks
	D) Check for duplicate rows
	E) Show outliers for units_sold column
	
2) Insights
	A)  Most recent 5 orders showing item type and Order_ID
	B) Oldest 5 orders
	C) Most sold 5 prodcuts  
	D) Most profitable 5 products
	E)Total profit by location
	F) Best location for sales for each item
	G) Revenue by year
	H) Best month for profit
	I) Sales performed each date
	L) Most sold product for each year
*/
--------------------------------------------------CLEANING------------------------------------------------------
--A) Check for typos on string entries

--Regions   
SELECT DISTINCT Region
FROM [Sales].[dbo].[SalesTable]
--Country
SELECT DISTINCT Country
FROM [Sales].[dbo].[SalesTable]
order by 1  asc 
--Item types
SELECT DISTINCT Item_Type
FROM [Sales].[dbo].[SalesTable]
order by 1 asc 
--Sales_channel
SELECT DISTINCT Sales_Channel
FROM [Sales].[dbo].[SalesTable]
order by 1 asc 
--Priority ratings
SELECT DISTINCT Order_Priority
FROM [Sales].[dbo].[SalesTable]
order by 1 asc 
--No typos found

--B)Check for nulls

SELECT *
FROM [Sales].[dbo].[SalesTable]
WHERE Region IS NULL
OR Country IS NULL
or Item_type IS NULL
or Sales_Channel IS NULL
or Order_Priority IS NULL
or Order_ID IS NULL
or Ship_Date IS NULL
or Units_Sold IS NULL
or Unit_Price IS NULL
or Unit_Cost IS NULL
or Total_Revenue IS NULL
or Total_Cost IS NULL
or Total_Profit IS NULL
--No nulls found

--C) Check for blanks

SELECT *
FROM [Sales].[dbo].[SalesTable]
WHERE Region = ' '
OR Country = ' '
or Item_type = ' '
or Sales_Channel = ' '
or Order_Priority = ' '
or Order_ID = ' '
or Ship_Date = ' '
or Units_Sold = ' '
or Unit_Price = ' '
or Unit_Cost = ' '
or Total_Revenue = ' '
or Total_Cost = ' '
or Total_Profit = ' '
--No blanks found	

--D) Check for duplicates                        

SELECT *,
ROW_NUMBER () OVER (
PARTITION BY 
Order_ID
ORDER BY Order_ID desc) row_num 
FROM [Sales].[dbo].[SalesTable]
-- No duplicates found

--E) Check for outliers on units sold

--Get average, standard deviation,range of acceptable values

Select avg(units_sold) as avg_units_sold
FROM [Sales].[dbo].[SalesTable]
SELECT STDEV(units_sold) as stddev_unit_sold
FROM [Sales].[dbo].[SalesTable]
SELECT avg(units_sold) -  STDEV(units_sold) AS lower_bound,
		avg(units_sold) +  STDEV(units_sold) AS upper_bound
FROM [Sales].[dbo].[SalesTable];

--Create one cte containing * from table and one cte for range of acceptable values
WITH units_sold_cte AS(
	SELECT * 
	FROM [Sales].[dbo].[SalesTable]
	),

	bounds AS 
	(SELECT avg(units_sold) -  STDEV(units_sold) AS lower_bound,
			avg(units_sold) +  STDEV(units_sold) AS upper_bound
	FROM [Sales].[dbo].[SalesTable]
	)
--Apply the columns of second cte as a fiter on the first cte	
SELECT item_type,Order_date,Units_Sold
FROM units_sold_cte,bounds
WHERE units_sold NOT BETWEEN lower_bound and upper_bound 
order by 3 asc



----------------------------------------------------------SELECT AND VIEW THE DATA-----------------------------------------------

--A)  Most recent 5 orders showing item type and Order_ID
SELECT TOP 5
Item_Type,  Order_ID, Order_date, Country
FROM [Sales].[dbo].[SalesTable]
Order by Order_date desc

--B) Oldest 5 orders
	
SELECT TOP 5
Item_Type,  Order_ID, Order_date, Country
FROM [Sales].[dbo].[SalesTable]
Order by Order_date asc

--C) Most sold 5 prodcuts  

Select TOP 5
Item_type, sum(Units_sold)
FROM [Sales].[dbo].[SalesTable]
Group by item_type
Order by sum(units_sold) desc

--D)Most profitable 5 products 

SELECT TOP 5
Item_Type, sum(Total_profit)
 FROM [Sales].[dbo].[SalesTable]
Group by item_type
ORDER BY sum(total_profit) desc

-- E)Total profit for each location for each item (applicable filters of country and item_type) 

SELECT Sum(Total_Profit) as LocationProfit,
		Country, 
		order_date, 
		Item_type,
		order_id
FROM [Sales].[dbo].[SalesTable]
group by 
		item_type,
		order_date,
		order_id,
		country
--having item_type = 'Household'
--AND having country = .......
order by item_type, LocationProfit desc

--F)Best Location for sales for each item

SELECT TOP 1
Sum(Total_Profit) as LocationProfit ,
		Country, item_type
FROM [Sales].[dbo].[SalesTable]
group by country, Item_type
-- Having Item_type =  "yourinputhere"
Order by LocationProfit desc

--G)Yearly revenue for each item type

SELECT Item_type, Sum(total_revenue) as YearlyRevenue,
YEAR(Order_Date) as Year
FROM [Sales].[dbo].[SalesTable]
GROUP BY YEAR(Order_Date),Item_type
Order by Year asc, item_type asc

-- H)Most profittable months (in descending order)  each year for each item type

SELECT  Item_type, Sum(total_profit) as monthly_profit,Year(Order_Date) as Year, Month(Order_Date) as Month
FROM [Sales].[dbo].[SalesTable]
GROUP BY Year(Order_date), Month (order_date), item_type 
Order by year asc,item_type asc,monthly_profit desc

-- I) Sales performed each date for each item


SELECT Item_type, Sum (units_sold) as daily_sales,
	Order_Date
FROM [Sales].[dbo].[SalesTable]
GROUP BY Item_type, Order_date
Order by Order_date asc, item_type asc 

-- L)Most sold product for each year

SELECT TOP 1
Item_type, Year(Order_Date) as year, sum(units_sold) as most_sales
FROM [Sales].[dbo].[SalesTable]
GROUP BY item_type,  Year(Order_Date)
order by year desc, most_sales desc
