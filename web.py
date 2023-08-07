import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    print(todo)
    functions.write_todos(todos)

st.title("My ToDo App")
st.subheader("This is my todo App")
st.write("This App is to increase my productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder='Add a new Todo...',
              on_change=add_todo,key='new_todo')

print("Hello")

st.session_state
