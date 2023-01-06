import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Smoothie')
streamlit.text('🐔 Hard Boiled Free Range Eggs')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

fruit_list = fruit_list.set_index('Fruit')

selected = streamlit.multiselect('Pick some Fruits:',list(fruit_list.index),['Avocado','Strawberries'])

show = fruit_list.loc[selected]

streamlit.dataframe(show)

def get_fruit_data(fruit_choice):
   fruityce_response = requests.get("https://www.fruityvice.com/api/fruit/"+fruit_choice)
   return pandas.json_normalize(fruityce_response.json())

   

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_req = streamlit.text_input('What fruit would you like to know about?')
  if not fruit_req:
    streamlit.error('please select a fruit')
  else:
    fruityce_response = requests.get("https://www.fruityvice.com/api/fruit/"+fruit_req)
    streamlit.dataframe(get_fruit_data(fruit_req))
    #streamlit.write('The user entered::',fruit_req)
except URLError as e:
  streamlit.error()
  


#connect to snowflake

streamlit.header('Fruit load list:')

def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from fruit_load_list")
      return my_cur.fetchall()
   
   
   
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = get_fruit_load_list()
streamlit.dataframe(my_data_rows)

streamlit.stop()
fruit_add= streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding',fruit_add)

my_cur.execute("insert into fruit_load_list values('from streamlit')")
