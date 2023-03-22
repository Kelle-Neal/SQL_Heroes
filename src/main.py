from database.db_connection import execute_query
from get_names import get_all_names

def start_menu():
  print("******************** SUPERHERO'S UNITE ********************")
  start = input("\nWhat would you like to do today?\n\n1: See information about current Superheroes.\n2: Edit, Add or Delete info about a Superhero.\n\nEnter your selection: ")
  if start == "1":
    all_info = input("Which superhero would you like to see more information about?\n\nEnter your selection: ")
    get_all_names()
  elif start == "2":
    ead_info = input("Would you like to\n1: Edit\n2: Add\n3: Delete\ninformation about a superhero?")
    if ead_info == "1":
      get_all_names()
      input("Which Superhero would you like to edit information about?")
    elif ead_info == "2":
      input("Which Superhero would you like to add information about?")
      get_all_names()
    elif ead_info == "3":
      get_all_names()
      input("Which Superhero would you like to delete information about?")
    else:
      print("Make a valid choice and try again.\n\n")

  else:
    print("Make a valid choice and try again.")
  # return start_menu()

start_menu()
 