







/* 0) Cleaning

1)Typos
There are no typos in Region, Item_type, Order_Priority (DISTINCT -> No similar entries found)

2) Nulls
No nulls

SELECT *
FROM [Sales].[dbo].PortfolioSales
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

3) Duplicate rows




SELECT *,
ROW_NUMBER () OVER (
PARTITION BY 
Order_ID
ORDER BY Order_ID) row_num
FROM [Sales].[dbo].PortfolioSales






*/


/*
A) PREVIEW


  
*/
--Regions   
SELECT DISTINCT Region
FROM [Sales].[dbo].PortfolioSales
--Item types
SELECT DISTINCT Item_Type
FROM [Sales].[dbo].PortfolioSales

--Priority ratings
SELECT DISTINCT Order_Priority
FROM [Sales].[dbo].PortfolioSales

--Most recent 5 orders
SELECT TOP 5
Order_Date as latest_date , Item_Type,Units_Sold,Total_Profit, Item_Type,Units_Sold,Total_Profit
  FROM [Sales].[dbo].PortfolioSales
--GROUP BY Order_date
Order by Order_Date DESC

--Oldest 5 orders
SELECT TOP 5
Order_Date as oldest_date,Item_Type,Units_Sold,Total_Profit, Item_Type,Units_Sold,Total_Profit
FROM [Sales].[dbo].PortfolioSales
Order by Order_Date ASC

--Most selling 5 products
SELECT TOP 5 
 Units_Sold as best_selling_units, Item_Type,Units_Sold,Total_Profit
FROM [Sales].[dbo].PortfolioSales
Order by Units_Sold , Order_Date DESC

--Most profitable 5 products
SELECT DISTINCT TOP 5
 Total_Revenue, Item_Type,Units_Sold,Total_Profit
FROM [Sales].[dbo].PortfolioSales
ORDER BY total_profit desc

/*
Revenue by location 

SELECT Total_Revenue ,Country
      ,Item_Type,Order_date
FROM [Sales].[dbo].PortfolioSales
GROUP BY Country -- Invalid in select list

Best location for sales
SELECT TOP 1
Total_Revenue ,Country
      ,Item_Type,Order_date
FROM [Sales].[dbo].PortfolioSales
GROUP BY Country -- Invalid in select list
ORDER BY Total_Revenue

Revenue by year
SELECT
Total_Revenue ,Country
      ,Item_Type,Order_date
FROM [Sales].[dbo].PortfolioSales
GROUP BY YEAR(Order_date)


Best month for sales

SELECT TOP 1 

Total_Revenue ,Country
      ,Item_Type,Order_date
FROM [Sales].[dbo].PortfolioSales
GROUP BY MONTH(Order_date)

Sales performed each date

SELECT
Units_Sold, Item_Type,Units_Sold,Total_Profit, Item_Type,Units_Sold,Total_Profit
FROM [Sales].[dbo].PortfolioSales
Group BY Order_date



Best selling product


SELECT * 
FROM [Sales].[dbo].PortfolioSales
Group BY Item_type
ORDER BY Total_revenue DESC



Average deal size
*/



