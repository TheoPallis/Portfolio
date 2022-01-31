#ToC 
#KPIs
#Top 10 customers
# Top products dataframes
# Most sold chart
# Most profitable chart


##Issues


# 1) Customer chart -> none
# 2) Create subplots
# 4) Map chart -> lat/long columns
# 5-> NFXJ) Do the calculations in the notebook
# 6) Make plotly graphs more aesthetically pleasing


#!/usr/bin/env python
# coding: utf-8

#------- -------------------------------------------Packages--------------------------------------------------------------------------------------------------------------------
import pandas as pd
import streamlit as st
import plotly.express as px 
#import make_subplots
st.set_page_config (page_title="Sales Analysis", layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'>Sales Dashboard</h1>", unsafe_allow_html=True)


@st.cache(allow_output_mutation=True)	
def get_data():
	path = r'clean_data31.csv'
	return pd.read_csv(path)
data = get_data()



# -- Sidebar configuration

st.sidebar.header("Filters")

# Year

year_select  = st.sidebar.multiselect('Year', data['Year'].unique())

# Country

country_select  = st.sidebar.multiselect('Country', data['Country'].unique())

# Month

month_slider =  [str(st.sidebar.select_slider('Month', data['MonthYear'].unique()))]

data = data[data['Year'].isin(year_select)]
data = data[data['Country'].isin(country_select)]
data = data[data['MonthYear'].isin(month_slider)]


st.dataframe(data)
















#--------------------------------------------------Calculating KPIs--------------------------------------------------------------------
data['Profit'] = data.Quantity * data.UnitPrice
total_profit =  data['Profit'].sum().astype('int') 
total_sales = data['Quantity'].sum().astype('int') 
best_seller = data.groupby(['Description']).sum()['Quantity'].reset_index().sort_values(by = 'Quantity', ascending = False)['Description'].head(1)
most_profitable = data.groupby(['Description']).sum()['Profit'].reset_index().sort_values(by = 'Profit', ascending = False)['Description'].head(1) 
#NFXJ -> remove unnecessary characters

#-----------------------------------------------------Displaying KPIs-------------------------------------------------------------------------------

st.markdown("<h1 style='text-align: center; color: black;'>KPIs</h1>", unsafe_allow_html=True)

st.markdown("##")

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Total Profit :")
    st.subheader(f" {total_profit:,} $")

with middle_column:
    st.subheader("Total Sales:")
    st.subheader(f"  {total_sales:,}")


with right_column:
    st.subheader("Best Seller:")
    st.subheader(f"{best_seller,}")

#--------------------------------------------------Top 10 customers-------------------------------------------------------------------------------------------------------------------------
data['CustomerID'] = data['CustomerID'].astype('str')
top_customers = data.groupby(['CustomerID']).sum()['Profit'].reset_index().sort_values(by = 'Profit', ascending = False).head(10)
top_customers['Profit'] = top_customers['Profit'].astype(float)
top_customers.sort_values(by='Profit',axis=0, ascending = True, inplace = True)
top_10_cust = px.bar(top_customers, x = 'Profit', y= 'CustomerID', orientation = 'h', title="<b>Top 10 Customers </b>")


#----------------------------------------------Top 10 most profitable items-------------------------------------------------------------------------
most_profitable = data.groupby(['Description']).sum()['Profit'].reset_index().sort_values(by = 'Profit', ascending = False).head(10)
most_profitable.sort_values(by='Profit',axis=0, ascending = True, inplace = True)
most_profit = px.bar(most_profitable, x = 'Profit', y= 'Description', orientation ='h', title="<b>Most Profitable Items</b>")


#-------------------------------------------------Top 10 most sold items-------------------------------------------------------------------------
most_sold = data.groupby(['Description']).sum()['Quantity'].reset_index().sort_values(by = 'Quantity', ascending = False).head(10)
most_sold.sort_values(by='Quantity',axis=0, ascending = True, inplace = True)
most_sold = px.bar(most_sold, x = 'Quantity', y= 'Description', title="<b>Most Sold Items</b>")




#--------------------------------------------Displaying the 3 Top 10 Charts----------------------------------------------------------------

st.markdown("##")
st.markdown("##")	

left_column, right_column = st.columns(2)

with left_column:
 
    st.write(most_profit)

with right_column:
    
    st.write(most_sold)
 
    st.write(top_10_cust)
#----------------------------------------------------Products purchased by top 10 customers + charts-----------------------------------------------------------------------

# Get the list of top 10 customers


customers_list = []
for id in top_customers['CustomerID'] :
    customers_list.append(id)
   		
# Get filtered dataframe for each customer ID

for i in customers_list:
	cust_prod = data[data['CustomerID'] == i]
	#cust_prod
	#fig = px.bar(cust_prod, x = 'Description', y= 'Profit', orientation = 'h', title="<b>Top 10 Customers Bought</b>")

#-------------------------------------------Displaying the subplots





#Unused code


# CustomerID ?

#data['CustomerID'] = data['CustomerID'].fillna(0, inplace = True)
#cust_unique = data['CustomerID'].unique()
#cust_slider =  [str(st.sidebar.select_slider('CustomerID', cust_unique))]
#data = data[data['CustomerID'].isin(cust_slider)]

# Price
#data['UnitPrice'] = data['UnitPrice'].astype(float)
#price_slider =  [str(st.sidebar.select_slider('Price', data['UnitPrice'].unique()))]
#data = data[data['UnitPrice'].isin(price_slider)]
