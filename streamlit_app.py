import streamlit
import pandas
streamlit.title ("My new healthy Dinner")

streamlit.header("Breakfast Favorites")

streamlit.text("🥣 Omega 3 and Blueberry oatmeal")
streamlit.text("🥗 kale,Spinach and Rocket smoothie")
streamlit.text("🐔 Hard-Boiled Free range egg")
streamlit.text("🥑🍞 Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
