#!/usr/bin/env python
# coding: utf-8

#------- -------------------------------------------Packages--------------------------------------------------------------------------------------------------------------------

import ezsheets
import streamlit as st 	
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import plotly.express as px
from itertools import

sheet_id = '16-KIiQP_CCCrOgGK8hY18CeYVYBYG9mbV0I_3_Fu3bg'
sheet_name = 'Test'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

 
@st.cache(allow_output_mutation=True)	
def get_data():
	path = r'wout_data.csv'
	return pd.read_csv(path)
data = get_data()

session_state = SessionState.get(df=data)







#------------------------Calculations-----------------------------------------------------------------------------------------------------------






list_ex = ['Bicep Curls', 'Tricep Extensions', 'Military Raises', 'Push Ups', 'Squats']														# Create a list of exercises

grp = data.groupby('Date').sum()																				# Group exercises in default dataframe by date												
melted = pd.melt(grp, var_name="Exercise", ignore_index=False)																	# Melt the dataframe						
	
charts = px.line(melted,																					# Create subplots	
         y='value',
         facet_col='Exercise',
         facet_col_spacing=0.1)



# -- ------------------------------------------------Sidebar configuration----------------------------------------------------------------------

st.sidebar.header("Navigation")
navigation = st.sidebar.radio( "Select Page",('Workout Log', 'Workout Analysis'))


# This function creates a new dataframe and appends to it a number of empty rows (currently) equal to the max selected number of sets. 

if navigation =='Workout Log':
    
    @st.cache(allow_output_mutation=True)	
    def new_wout() : 
		date = st.date_input('Select the date :')
  		@st.cache(allow_output_mutation=True)																		
		def name_ex() :																					# This function caches the user name and exercise number
		name= st.text_input (" Today's champion is : " ) 																## This block gets the general details of the workout and the number of exercises/columns																
		ex_cols = st.slider ('Number of exercises', max_value = 10) 
		name_ex()	
		
		if st.button(" Today's Workout ") :                          														
			return(f" Alright {name}, today's workout consists of { ex_cols} exercises. Think you can make it ?" )
			if st_button("Nope"!) : 
				ex_cols = st.slider ('Number of exercises', max_value = 10) 	
				return(f" Alright {name}, today's workout consists of { ex_cols} exercises. Think you can make it ?" )
		elif st.button(" Bring it on! ") : 																		## This block starts the workout 
			w_data = pd.Dataframe()																			# Create new  workout dataframe 
			for ex in range (0, ex_cols) :  		  															# Number of loops = previouly inputted ex number
				sel_ex	= st.selectbox (list_ex)   																# For each exercise get its name
				w_data[ex] = w_data[ex].rename('Ex' : sel_ex)                													# Rename columns according to the inputted names
				set_number = st.selectbox ('Number of sets') 															# For each exercise get number of sets
					for sets in range (0, set_number.max()) : 
						@st.cache(allow_output_mutation=True)	
						def fill_reps(df, name):															# This function fills each exercise column with the selected number of reps / Gets number of reps for each set for each exercise
	    					for row in range (df.shape[0]):															# Number of loops = count of rows (shape[0])
	        					rep_number = st.select_box ('Number of reps')												# Input number of reps
	        					df.at[row,name]= rep_number 	        												# Go to selected cell -> fill it with rep number
	        			fill_reps(w_data, w_data[ex])
	        			w_data[date] = date   																	# Create a date column, with the specified date for each row
						session_state.df = session_state.df.append(set_number, ignore_index=True)									# Lock changes/persistent dataframe -> NFX7)
						new_workout = w_data.append(set_number)									
						if st_button("Finished"!) :
							data.append(new_workout)
							return (new_workout)															# Show new workout dataframe			
							download_csv = new_workout.to_csv(f " {date} 's_Workout_{name}) 									# Get csv						
							st.download_button ('Download your workout', download_csv) 										# Download button for csv
new_wout()
			
# Workout Analysis Page
# NFX8)

if navigation =='Workout Analysis':																				# Navigate to "page" Workout Analysis
 if st.button('Total reps each day') :							
	grp 																							# Sum of reps for each exercise each day
	melted								
 if st.button('Analytical View'):																				# Original dataframe
 	data
 if st.button('Show me the charts!') :																				# Show trend-line subplots (y axis = reps for each exercise,x axis = date) 												
	charts	







