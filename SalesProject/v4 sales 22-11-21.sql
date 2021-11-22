/* ToC
0) Cleaning
	1) Check for Typos
	2) Check for Nulls
	3) Check for duplicate rows ?1
I)  Most recent 5 orders showing item type and Order_ID
II) Oldest 5 orders
III) Most selling 5 prodcuts  
IV) Most profitable 5 products
V) Total profit by location 
VI) Best location for sales
VII) Revenue by year
VIII) Best month for profit
IX) Sales performed each date
X) Best selling product


/
--0) Cleaning

--1)Typos
--There are no typos in Region, Item_type, Order_Priority (DISTINCT -> No similar entries found)
--OK Check for typos by using DISTINCT

--Regions   
SELECT DISTINCT Region
FROM [Sales].[dbo].[SalesTable]
--Item types
SELECT DISTINCT Item_Type
FROM [Sales].[dbo].[SalesTable]
--Priority ratings
SELECT DISTINCT Order_Priority
FROM [Sales].[dbo].[SalesTable]


2) Nulls
No nulls
*/
SELECT *
FROM [Sales].[dbo].[SalesTable]
WHERE Region IS NULL
OR Country is null
or Item_type is null
or Sales_Channel is null
or Order_Priority is null
or Order_ID is null
or Ship_Date is null
or Units_Sold is null
or Unit_Price is null
or Unit_Cost is null
or Total_Revenue is null
or Total_Cost is null
or Total_Profit is null

-----3) Duplicate rows                        

SELECT *,
ROW_NUMBER () OVER (
PARTITION BY 
Order_ID
ORDER BY Order_ID) row_num
FROM [Sales].[dbo].[SalesTable]

*/



--A)Preview

--Most recent 5 orders               

SELECT TOP 5
Item_Type,  Order_ID, Order_date, Country
FROM [Sales].[dbo].[SalesTable]
Order by Order_date desc

--Oldest 5 orders 

SELECT TOP 5
Item_Type,  Order_ID, Order_date, Country
FROM [Sales].[dbo].[SalesTable]
Order by Order_date asc

--Most sold 5 products

Select TOP 5
Item_type, sum(Units_sold)
FROM [Sales].[dbo].[SalesTable]
Group by item_type
Order by sum(units_sold) desc

 --Most profitable 5 products 
SELECT TOP 5
Item_Type, sum(Total_profit)
 FROM [Sales].[dbo].[SalesTable]
Group by item_type
ORDER BY sum(total_profit) desc

--General profit by location for each item  ????

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
order by item_type desc

--Best Location for sales for each item

SELECT TOP 1
Sum(Total_Profit) as LocationProfit ,
		Country, item_type
FROM [Sales].[dbo].[SalesTable]
group by country, Item_type
-- Having Item_type =  .......
Order by LocationProfit desc


--Yearly revenue for each item type

SELECT Item_type, Sum(total_revenue) as YearlyRevenue,
YEAR(Order_Date) as Year
FROM [Sales].[dbo].[SalesTable]
GROUP BY YEAR(Order_Date),Item_type
Order by Year asc, item_type asc


-- Most profittable month each year for each item typ

SELECT  Item_type, Sum(total_profit) as monthly_profit,Year(Order_Date) as Year, Month(Order_Date) as Month
FROM [Sales].[dbo].[SalesTable]
GROUP BY Year(Order_date), Month (order_date), item_type 
Order by year asc,item_type asc,monthly_profit desc


-- Daily sales


SELECT Item_type, Sum (units_sold) as daily_sales,
	Order_Date
FROM [Sales].[dbo].[SalesTable]
GROUP BY Item_type, Order_date
Order by Order_date asc, item_type asc 



-- Most profitable product for each year

SELECT 
--TOP 1
Item_type, Year(Order_Date) as year, sum(units_sold) as most_sales
FROM [Sales].[dbo].[SalesTable]
GROUP BY item_type,  Year(Order_Date)
order by year desc, most_sales desc