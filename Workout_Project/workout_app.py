
#!/usr/bin/env python
# coding: utf-8

#------- -------------------------------------------Packages--------------------------------------------------------------------------------------------------------------------

import ezsheets
import streamlit as st 	
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import plotly.express as px

sheet_id = '16-KIiQP_CCCrOgGK8hY18CeYVYBYG9mbV0I_3_Fu3bg'
sheet_name = 'Test'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

 
@st.cache(allow_output_mutation=True)	
def get_data():
	path = r'wout_data.csv'
	return pd.read_csv(path)
data = get_data()






# -- Sidebar configuration

st.sidebar.header("Navigation")
navigation = st.sidebar.radio( "Select Page",('Workout Log', 'Workout Analysis'))

cols =  []
for name in data.columns :
    cols.append(name) 

list_ex = ['Bicep Curls', 'Tricep Extensions', 'Military Raises', 'Push Ups', 'Squats']

# Get a selection list for the inputted number of exercises

if navigation =='Workout Log':
	date = st.date_input('Select the date :')
	ex_cols = st.slider ('Number of exercises', max_value = 10)
	if st.button(" Today's Workout ") :
		print(ex_cols)
		for e in range (0, ex_cols) :  
			sel_ex	= st.selectbox (list_ex)
			set_number = st.selectbox ('Number of sets')
				for reps in set_number :
					rep_number = st.select_box ('Number of reps')






#num_new_rows = st.sidebar.number_input("Add Rows",1,50)
	#with st.form(key='add_record_form',clear_on_submit= True):
	#	st.subheader('Number of sets')
	#	num_col = len(data.columns)
	#	int_col = st.columns(int(ncol))	
	#	st.form_submit_button(data)

	#filled = data.append({'Date': str(date)}, ignore_index=True)
	#filled
	#st.add_rows
	#ex = st.multiselect(data)



# List of variables :
# Date
# Ex_ncols
# Set_number
# Sel_ex
# 

#for n in range (1, number) :
	#	today_data.insert (0, ex, date)
	#	today_data
	




# Workout Analysis Page

#if navigation =='Workout Analysis':
 #if st.button('Total reps each day') :
 #		grouped_data = data.groupby('Date').sum().sort_values(by = 'Date', ascending = True)
 #		grouped_data
 #if st.button('Analytical View') :
 #		data








#Unused code :
#def get_data():
	#data = pd.read_csv(url)
	#data = get_data()
#left_column, middle_column, right_column = st.columns(3)
#with left_column:
#	if st.button('Total reps each day') :
# 		grouped_data = data.groupby('Date').sum().sort_values(by = 'Date', ascending = True)
# 		grouped_data
#with middle_column:
#	if st.button('Analytical View') :
# 		data
#with right_column:
#    st.subheader("Best Seller:")
# st.form('log', clear_on_submit=False)
#data.add_rows(today_data)





#from gsheetsdb import connect
# Create a connection object.
#conn = connect()
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
#@st.cache(ttl=600)
#def run_query(query):
#    rows = conn.execute(query, headers=1)
#    return rows
#sheet_url = "https://docs.google.com/spreadsheets/d/16-KIiQP_CCCrOgGK8hY18CeYVYBYG9mbV0I_3_Fu3bg/edit#gid=1251154754"
#rows = run_query(f'SELECT * FROM "{sheet_url}"')
# Print results.
#for row in rows:
#    st.write(f"{row.name} has a :{row.pet}:")
