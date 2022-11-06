import streamlit

streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🍇''omega 3 Blueberrry Oatmeal')
streamlit.text('🍎''Kale, Spinach & Rocket Smothie')
streamlit.text('🍎''Hard-Boiled Free-Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
