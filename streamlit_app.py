streamlit.stop()

import streamlit
#import pandas as pd
#import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Mom\'S New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

#lets pick up multiselect fruits
fruits_selected = streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show  = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +"kiwi")
#streamlit.text(fruityvice_response)

#streamlit.text(fruityvice_response.json())

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruitwould you like information about?', "kiwi") 
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalize = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalize)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

#Query Some Data, Instead
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


fruit_choice_ = streamlit.text_input('What fruit would you like to add?') 
streamlit.write('Thanks for adding ', fruit_choice_)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#fruityvice_normalize = pd.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalize)
