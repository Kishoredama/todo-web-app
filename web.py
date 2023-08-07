import streamlit as st
import functions

todos = functions.get_todos()

st.title("My ToDo App")
st.subheader("This is my todo App")
st.write("This App is to increase my productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='',placeholder='Add a new Todo')

print("Hello")
