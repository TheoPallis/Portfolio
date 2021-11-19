--A) PREVIEW
SELECT TOP (1000) [Region]
      ,[Country]
      ,[Item_Type]
      ,[Sales_Channel]
      ,[Order_Priority]
      ,[Order_Date]
      ,[Order_ID]
      ,[Ship_Date]
      ,[Units_Sold]
      ,[Unit_Price]
      ,[Unit_Cost]
      ,[Total_Revenue]
      ,[Total_Cost]
      ,[Total_Profit]
  FROM [Sales].[dbo].PortfolioSales
--I) 

--Regions   date lowest, date max, total)revenue, total profit, tot
SELECT DISTINCT Region, Item_Type, Order_ID
FROM PortfolioSales

--Item types
SELECT DISTINCT Item_Type
FROM PortfolioSales

--Priority ratings
SELECT DISTINCT Order_Priority
FROM PortfolioSales

--Most recent 5 orders
SELECT TOP 5
Order_Date
FROM PortfolioSales
Order by Order_Date DESC

--Oldest 5 orders
SELECT TOP 5
Order_Date
FROM PortfolioSales
Order by Order_Date ASC

--Most selling 5 products
SELECT TOP 5 
 Units_Sold
FROM PortfolioSales
Order by Order_Date DESC

--Most profitable 5 products
SELECT DISTINCT TOP 5
 Total_Revenue
FROM PortfolioSales


