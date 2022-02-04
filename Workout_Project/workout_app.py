
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

#------------------------Calculations------------------------------------------


list_ex = ['Bicep Curls', 'Tricep Extensions', 'Military Raises', 'Push Ups', 'Squats']							# Current list of exercises

grp = data.groupby('Date').sum()													# Grouped by date total reps for each exercise

melted = pd.melt(grp, var_name="Exercise", ignore_index=False)										# Melted exercise groups
	
charts = px.line(melted,														# Trend line subplots for each exercise -> Show reps per date
         y='value',
         facet_col='Exercise',
         facet_col_spacing=0.1)



# -- Sidebar configuration

st.sidebar.header("Navigation")
navigation = st.sidebar.radio( "Select Page",('Workout Log', 'Workout Analysis'))


# Get a selection list for the inputted number of exercises

if navigation =='Workout Log':
	name= st.text_input (" Today's champion is : " ) 										# Get user's name/ NFX1 		
	date = st.date_input('Select the date :')											#  Get the date
	ex_cols = st.slider ('Number of exercises', max_value = 10) 									# Get number of exercsises -> Create equal number of columns
	if st.button(" Today's Workout ") :                          									# Button
		print(f" Alright {name}, today's workout consists of { ex_cols) exercises. Think you can make it ?" )			# Confirm number of exercises/NFX2 		      
		if st.button(" Bring it on! ") : 											# Start the workout
			w_data = pd.Dataframe()                   									# Create new  workout dataframe							
			for e in range (0, ex_cols) :  		  									# Get names of exercises (number of exercises = slider)
				sel_ex	= st.selectbox (list_ex)   
				w_data[e] = sel_ex                									# Rename columns according to the inputted names
				set_number = st.selectbox ('Number of sets') 								# Get number of sets
				for reps in range (0, set_number) :									# Get number of reps for each set
					rep_number = st.select_box ('Number of reps')							# Get number of reps
					new_workout = w_data.append(rep_number)								# Add rep entries to new dataframe
					if st_button("Finished"!) :
						print (new_workout)									# Show new workout dataframe			
						download_csv = new_workout.to_csv(f " {date} 's_Workout_{name}) 			# Get csv
						st.download_button ('Download your workout', download_csv) 				# Download button for csv


# Workout Analysis Page

if navigation =='Workout Analysis':													# Navigate to "page" Workout Analysis
 if st.button('Total reps each day') :							
	grp 																# Sum of reps for each exercise each day
	melted								
 if st.button('Analytical View'):													# Original dataframe
 	data
 if st.button('Show me the charts!') :													# Show trend-line subplots (y axis = reps for each exercise,x axis = date) 												
	charts	

# Notes (NFX = Need to Fix)
#NFX1 ->  In the future add a selectbox with previously entered user names	
#NFX2 -> In the future add a 'Hold your horses, I made a mistake" button -> edit the selected number of exercises
#NFX3 -> Use product from itertools for double loop

