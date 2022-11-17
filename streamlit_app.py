import streamlit
	
streamlit.title('My parents New Healthy Diner')
	
streamlit.header('Breakfast Menu')
streamlit.text('🍇''omega 3 Blueberrry Oatmeal')
streamlit.text('🍎''Kale, Spinach & Rocket Smothie')
streamlit.text('🍎''Hard-Boiled Free-Range Egg')
	
import pandas
my_fruit_list = pandas.read_csv(https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt)

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
streamlit.header("Fruityvice Fruit Advice!")
	
fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered ', fruit_choice)
	
import requests
#fruityvice_response = requests.get(https://fruityvice.com/api/fruit/watermelon)

fruityvice_response = requests.get(https://fruityvice.com/api/fruit/ +  fruit_choice)
#streamlit.text(fruityvice_response.json()) --Instruction to delete this line.
	
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
	
import snowflake.connector
	
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
def insert_row_snowflake(new_fruit):
with my_cnx.cursor() as my_cur:
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")
my_cur.execute("insert into fruit_load_list values ('" + new_fruit +"')")   
return "Thanks for adding " + new_fruit
	        
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
back_from_function = insert_row_snowflake(add_my_fruit)
my_cnx.close()
streamlit.text(back_from_function)
	

