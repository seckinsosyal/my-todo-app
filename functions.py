FILEPATH = "todos.txt"

def get_todos():
    with open(FILEPATH, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos, filepath = FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos)
    return None