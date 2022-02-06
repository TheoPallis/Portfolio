
# Notes (NFX = Need to Fix)

#NXX1- > Does 'nope!' loop back to original choice?
#NFX2 -> Is using the max number of sets to calculate the needed rows the optimal solution?
#NFX3 -> If it is, is this the proper syntax ? (0, set_number.max()) 
#NFX4 -> new_workout = w_data.append(set_number) ->  (do not append)
#NFX5 -> Is this the proper syntax? -> fill_reps(w_data, w_data[e]) ->
#NFX6 -> Are the ifs/elifs properly used? (nested, alternate syntax -> multiple ifs)
#NFX7 -> Is df the correct dataframe to lock changes?
#NFX8 -> Is this the proper syntax? (0, ex_cols)

#NFXLast1) -> View buttons as columns
#NFXLast2  -> In the future add a selectbox with previously entered user names	

# Sources
#* https://stackoverflow.com/questions/62835169/how-to-insert-a-value-from-an-input-in-a-specific-row-and-column-in-a-pandas-dat




# Original double loop  before product

				
	# for ex in range (0, ex_cols) :  		  																			# Number of loops = previouly inputted ex number
	# 	sel_ex	= st.selectbox (list_ex)   																				# For each exercise get its name
	# 	w_data[ex] = sel_ex                																				# Rename columns according to the inputted names
	# 	set_number = st.selectbox ('Number of sets') 																	# For each exercise get number of sets
	# 	for sets in range (0, set_number.max()) : 
	# 		def fill_reps(df, name):																					# This function fills each exercise column with the selected number of reps / Gets number of reps for each set for each exercise
	#     		for row in range (df.shape[0]): 																    	# Number of loops = count of rows (shape[0])
	#         		rep_number = st.select_box ('Number of reps')  														# Input number of reps
	#         		df.at[row,name]= rep_number 


# Intermediary code/ Defien function for first loop
# def ex_func() :
# 			for ex in range (0, ex_cols) :  		  																	# Number of loops = previouly inputted ex number
# 				sel_ex	= st.selectbox (list_ex)   																		# For each exercise get its name
# 				w_data[ex] = sel_ex                																		# Rename columns according to the inputted names
# 				set_number = st.selectbox ('Number of sets') 															# For each exercise get number of sets
# 					def set_func() :
# 						for sets in range (0, set_number.max()) : 
							

# Final code attempt/ There is an extra function in the second loop function 
	def ex_func() :
		sel_ex	= st.selectbox (list_ex)   																				# For each exercise get its name
		w_data[e] = sel_ex                																				# Rename columns according to the inputted names
		set_number = st.selectbox ('Number of sets') 																	# For each exercise get number of sets
		exfunc()					
		def set_func() :
				#???? for sets in range (0, set_number.max()) : 
								
					def fill_reps(df, name):																			# This function fills each exercise column with the selected number of reps / Gets number of reps for each set for each exercise
		    			for row in range (df.shape[0]):																	# Number of loops = count of rows (shape[0])
		        		rep_number = st.select_box ('Number of reps')													# Input number of reps
		        		df.at[row,name]= rep_number 	        														# Go to selected cell -> fill it with rep number
		        		fill_reps(w_data, w_data[e])
						session_state.df = session_state.df.append(set_number, ignore_index=True)						# Lock changes/persistent dataframe -> NFX7)
for ex,sets in product(range(0, ex_cols), range(0, set_number.max())													# Product loop
    function(ex_func,set_func)		