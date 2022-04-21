import streamlit
import pandas as pd
import requests


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
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +"kiwi")
#streamlit.text(fruityvice_response)

#streamlit.text(fruityvice_response.json())

streamlit.header('Fruityvice Fruit Advice!')
fruityvice_normalize = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalize)
