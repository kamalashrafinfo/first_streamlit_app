import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents New Healthy Diner')
	
streamlit.header('Breakfast Menu')
streamlit.text('🍇''omega 3 Blueberrry Oatmeal')
streamlit.text('🍎''Kale, Spinach & Rocket Smothie')
streamlit.text('🍎''Hard-Boiled Free-Range Egg')
	
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
	
# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
#streamlit.dataframe(fruits_to_show)
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['canteloup'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display the table on the page.
streamlit.dataframe(fruits_to_show)
	
#New Section to display fruitvice api response
#streamlit.header("Fruityvice Fruit Advice!")
	
#fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
#try:
#	fruit_choice = streamlit.text_input('What fruit would you like information about?')
#	if not fruit_choice:
#		streamlit.error("Please select a fruit to get information.")
#	else:
	
#streamlit.write('The user entered ', fruit_choice)
	
#import requests
#fruityvice_response = requests.get(https://fruityvice.com/api/fruit/watermelon)
#		fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +  fruit_choice)
#		fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
#		streamlit.dataframe(fruitvice_normalized)
	
#except URLError as e:
#create the repeatable code block (called a function)
def get_fruitvice_data(this_fruit_choice):
	fruitvice_response = requests.get("https://fruitvice.com/api/fruit/" + this_fruit_choice)
	fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
	return fruitvice_normalized
#New Section to display fruitvice api response
streamlit.header('Fruitvice Fruit Advice!')
try:
	Fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
	Streamlit.error("Please select a fruit to get information.")
else:
	back_from_function - get_fruitvice_data(fruit_choice)
	streamlit.dataframe(back_from function)
	streamlit.error()
	
#streamlit.text(fruityvice_response.json()) --Instruction to delete this line.
	
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
	
#import snowflake.connector
	
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("Th fruit load list contains:")
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_rows)
	
	
#streamlit.write('The user entered ', fruit_choice)
	
fruit_choice = streamlit.text_input('What fruit would you like to addt?','fruit_choice')
streamlit.write('Thanks for adding', fruit_choice)

#This will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

# Don't run anything past here while we troubleshoot
streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list ")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
