import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt") as file:
        pass

todos = functions.get_todos()


def add_todo():
    todo_1 = st.session_state["new_todo"] + "\n"
    todos.append(todo_1)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
