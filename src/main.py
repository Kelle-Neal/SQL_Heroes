from database.db_connection import execute_query
# from get_names import get_all_names
import sys, subprocess


def start_menu():
  subprocess.run('clear')
  print("******************** SUPERHERO'S UNITE ********************")
  start = input("\nWhat would you like to do today?\n\n1: See information about current Superheroes.\n2: Edit, Add or Delete info about a Superhero.\n\nEnter your selection: ")
  subprocess.run('clear')
  if start == "1":
    print("******************** SUPERHERO'S UNITE ********************\n")
    get_all_names()
    get_hero = input("\nWhich superhero would you like to see more information about?\n\nEnter your selection: ")
    print(get_hero)
    # subprocess.run('clear')
    get_all_info()

    
  elif start == "2":
    print("******************** SUPERHERO'S UNITE ********************\n")
    ead_info = input("What would you like to do with the Superhero's information\n1: Edit\n2: Add\n3: Delete\n\nEnter your selection: ")
    subprocess.run('clear')
    if ead_info == "1":
      get_all_names()
      get_hero = input("\nWhich Superhero would you like to edit information about?\n\nEnter your selection: ")
      subprocess.run('clear')

    elif ead_info == "2":
      print("******************** SUPERHERO'S UNITE ********************\n")
      get_all_names()
      get_hero = input("\nWhich Superhero would you like to add information about?\n\nEnter your selection: ")
      subprocess.run('clear')
      
    elif ead_info == "3":
      print("******************** SUPERHERO'S UNITE ********************\n")
      get_all_names()
      get_hero = input("\nWhich Superhero would you like to delete information about?\n\nEnter your selection: ")
      subprocess.run('clear')
    
    else:
      print("******************** SUPERHERO'S UNITE ********************\n")
      print("\nMake a valid choice and try again.\n\n")
      subprocess.run('clear')
      ead_info()

  else:
    print("******************** SUPERHERO'S UNITE ********************\n")
    print("\nMake a valid choice and try again.")
    subprocess.run('clear')

  # return start_menu()


def get_all_names():
  get_names = execute_query("SELECT id, name FROM heroes ORDER BY name").fetchall()
  for id, names in get_names:
    print(id,"-",names)
get_all_names()  



start_menu()



