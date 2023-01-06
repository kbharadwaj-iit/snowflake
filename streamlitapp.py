import streamlit
import pandas
import requests
import snowflake.connector

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



streamlit.header("Fruityvice Fruit Advice!")

fruit_req = streamlit.text_input('What fruit would you like to know about?')
streamlit.write('The user entered::',fruit_req)

fruityce_response = requests.get("https://www.fruityvice.com/api/fruit/"+fruit_req)
streamlit.dataframe(pandas.json_normalize(fruityce_response.json()))

#connect to snowflake

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

