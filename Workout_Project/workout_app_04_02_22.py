
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

cols =  []
for name in data.columns :
    cols.append(name) 

list_ex = ['Bicep Curls', 'Tricep Extensions', 'Military Raises', 'Push Ups', 'Squats']

charts = px.line(melted,
         y='value',
         facet_col='Exercise',
         facet_col_spacing=0.1)



# -- Sidebar configuration

st.sidebar.header("Navigation")
navigation = st.sidebar.radio( "Select Page",('Workout Log', 'Workout Analysis'))


# Get a selection list for the inputted number of exercises

if navigation =='Workout Log':
name= st.text_input (" Today's champion is : " )				
	date = st.date_input('Select the date :')
	ex_cols = st.slider ('Number of exercises', max_value = 10)
	if st.button(" Today's Workout ") :
		print(f" ..." )
                if st.button(" Bring it on! ") :
		w_data = pd.Dataframe()							
		for e in range (0, ex_cols) :  
			sel_ex	= st.selectbox (list_ex)
                        w_data[e] = sel_ex
			set_number = st.selectbox ('Number of sets')
			for reps in range (0, set_number) :
				rep_number = st.select_box ('Number of reps')
				new_workout = w_data.append(rep_number)
				print (new_workout)
                     		download_csv = new_workout.to_csv(f " {date} 's_Workout_{name}) 
				st.download_button ('Download your workout', download_csv) 


# Workout Analysis Page

if navigation =='Workout Analysis':
 if st.button('Total reps each day') :
 	grp = data.groupby('Date').sum()
	grp 
	melted = pd.melt(grp, var_name="Exercise", ignore_index=False)
	melted
 if st.button('Analytical View'):
 	data
 if st.button('Show me the charts!') :
	charts	




