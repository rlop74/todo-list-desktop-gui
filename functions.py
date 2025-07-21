FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of todo

    Parameters:
        filepath (string): the filepath of the TXT file including the filename

    Returns:
        All items in the todo list file in a list format
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines() # returns list value, store in todos

    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the todo items list in the TXT file

    Parameters:
        todos_arg (list): the todos list
        filepath (string): the filepath of the TXT file including the filename

    Return:
        None, just overwrites the file in the filepath to what's in the todos_arg
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())