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
