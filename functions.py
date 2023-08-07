def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file_loc:
        todo_loc = file_loc.readlines()
    return todo_loc

def write_todos(todo_arg, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todo_arg)

if __name__ == "__main__":
    print("Hello")


