# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

# while loop for managing todos
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip() # in case the user accidentally enters a space before or after the input
    user_action = user_action.lower() # in case the user enters an uppercase letter

    if user_action.startswith("add"):
        todo = user_action[4:]

        # open the txt file to save its contents using get_todos() function
        todos = functions.get_todos()


        # add new todo
        todos.append(todo + "\n")

        # overwrite txt file with the added todo
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        # open txt file and save contents in todos (returns list)
        todos = functions.get_todos()

        # remove extra \n using list comprehension
        # new_todos = [item.strip("\n") for item in todos]

        # loop through the list and print the concatenated index-item name
        for index, item in enumerate(todos):
            item = item.strip("\n") # remove extra \n
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        # handle the error in case user enters a string
        try:
            # get user input
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("What would you like to change it to? ")

            # open file in read mode
            todos = functions.get_todos()

            todos[number] = new_todo + "\n"

            # open file in write mode and edit todo
            functions.write_todos(todos)

        except ValueError:
            print("Please enter the todo number")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            removed_todo = todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"{removed_todo.strip("\n")} was removed from the list."
            print(message)
        except IndexError:
            print("The number you entered is out of range")
            continue
        except ValueError:
            print("Please enter the todo number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")
