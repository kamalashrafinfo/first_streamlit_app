import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError




#import streamlit

streamlit.header ('Breakfast favorites')
streamlit.text ('🥣 Omega3 & blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard- boiled Free-Range Egg')
streamlit.text('🥑Avacado Toast')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
#mport requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#treamlit.text(fruityvice_response)


#New section to display fruityviceapi response
#streamlit.header('fruityvice fruit advice!')
#try:
  #fruit_choice = stremalit.text_input('what fruit would you like information about?')
  #if not fruit_choice:
    
   # else:
     # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      #streamlit.dataframe(fruityvice_normalized)
                                         
      #except URLError as e:
      #streamlit.error()
                                      
# New section to dispaly  fruitvice api response
#streamlit.header('Fruityvice Fruit Advise!')
#try:
 # fruit_choice = streamlit.text_input('What fruit would you like information about?')
  #if not fruit_choice:
   #  streamlit.error("Please select a fruit to get information.")
  #else:
   #   back_from_function = get_fruityvice_data(fruit_choice)
    #  streamlit.dataframe(back_from_function)
      
#except URLError as e:
 #   streamlit.error()




#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response)

#New Section to display fruitvice api response
#streamlit.header("Fruityvice Fruit Advice!")

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
                                   
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)





# Don't run anything past here while we troubleshoot
#streamlit.stop
#streamlit.stop()
	
#streamlit.header("The fruit load list contains:")
		 #snowflake-related functions
		 #def get_fruit_load_list():
		 #with my_cnx.cursor() as my_cur:
		 #return my_cur.fetchall()
#import snowflake.connector		
#Streamlit.header("The Fruit load list contains:")
#snowflake-related functions
#def get_fruit_load_list():
#with my_cnx.cursor() as my_cur:
	#my_cur.execute("select* from fruit_load_list")
#return my_cur.fetchall()

streamlit.header("View Our Fruit Lsit - Add Your Favorites!")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

#add_my_fruit = streamlit.text_input('What fruit would you like to add?')
#if streamlit.button('Add a fruit to the list'):
	#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]
	#back_from_function = insert_row_snowflake(add_my_fruit)
	#streamlit.text(back_from_function)
	
     #my_cnx.close()
     #streamlit.text(back_from_function)

	
#  Add a Second Text Entry Box: 
#  Allow the end user to add a fruit to  the list:
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

#import snowflake.connector
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list ")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

 # Add a button to load the fruit
	#if streamlit.button('Get fruit load list'):
	#my_cnx = Snowflake.connctor.connect(**streamlit.secrets["snowflake"])
					  #my_data_rows = get_fruit_load_list()
					  #streamlit.dataframe(my_data_rows)


  
  # Add a button to load the fruit
# if streamlit.button('Get fruit load list'):
 #  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  #  my_data_rows = get_fruit_load_list()
   # streamlit.dataframe(my_data_rows)

  
#Allow the end user to add a fruit to the list

#import pandas
#add_my_fruit = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#add_my_fruit = add_my_fruit.set_index('Fruit')

#Let's put a pick ist here so they can pick the fruit they want to include
#streamlit.multiselect("Pick somefruits:",list(add_my_fruit.index))

#streamlit.write ('Thanks for adding ', add_my_fruit)

#This will not work correctly, but just go with it for now
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")


