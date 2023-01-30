import streamlit
streamlit.title('my parents new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach and Rocket Smoothie')
streamlit.text('🍥Hard boiled Free Range eggs')
streamlit.text('🍞🥝Avacado Toast')
streamlit.header('🍇🥝🍋🍊🍉🍏🍐Build Your Own Fruite Smoothie🍑🍒🍅🍓🥑🥭🍍🍌')
import pandas
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
my_fruit_list=my_fruit_list.set_index('Fruit')
# lets put a picklist for the customerts so they can pick the fruit of their choice in the smoothie.
streamlit.multiselect('pick some fruit from this list:', list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
Fruit_Selected=streamlit.multiselect('pick some fruit from this list:', list(my_fruit_list.index),['Avocado','Strawberries'])
Fruit_To_Show=my_fruit_list.loc[Fruit_Selected]
streamlit.dataframe(Fruit_To_Show)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")
# streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
