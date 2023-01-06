import streamlit
import pandas
import requests

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

fruityce_response = requests.get("https://www.fruityvice.com/api/fruit/watermelon")

streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityce_response.json())
