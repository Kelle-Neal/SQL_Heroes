
from database.db_connection import execute_query
# from get_names import get_all_names
import sys, subprocess



def start_menu():
  header()
  start = input("What would you like to do today?\n\n1: See information about current Superheroes.\n2: Edit, Add or Delete info about a Superhero.\n\nEnter your selection: ")
  
  if start == "1":
    header()
    get_hero_id()
 
  elif start == "2":
    header()
    ead_info = input("What would you like to do with the Superhero's information\n1: Edit\n2: Add\n3: Delete\n\nEnter your selection: ")

    if ead_info == "1":
      edit_hero_info()

    elif ead_info == "2":
      set_new_hero()
      
    elif ead_info == "3":
      delete_hero()
    
    else:
      header()
      print("\nMake a valid choice and try again.\n\n")
      ead_info()

  else:
    header()
    print("\nMake a valid choice and try again.")

  # return start_menu()


def get_all_names():
  header()
  all_names = """
    SELECT name from heroes
  """
  get_names = execute_query(all_names).fetchall()
  for num, value in enumerate(get_names):
    print(f"{num +1}: {value[0]}")
  return get_names  
  

def get_hero_id():
  get_all_names()
  hero_id = (input("\nSelect Superhero by their number: "))
  header()
  get_hero_info(hero_id)

 
def get_hero_info(hero_id):
  hero_info = f"""
    SELECT
      id,
      name,
      about_me,
      biography
    FROM heroes
    WHERE heroes.id = %s
  """
  info = execute_query(hero_info, (hero_id,)).fetchall()
  for count, value in enumerate(info):
    print(f"""
    {value[1]}\n
    {value[2]}\n
    {value[3]}\n
    """)
    get_other_hero()

def get_other_hero():
  other_hero = input("\nDo you want to see information about a different hero?\nEnter YES or NO: \n")
  if other_hero == "YES":
    header()
    get_hero_id()
  else: 
    start_menu()

############## ADD ##############

def set_new_hero():
  set_name = input("\nEnter new Superhero's name: ")
  set_about = input("\nEnter new Superhero's Byline: ")
  set_story = input("\nEnter new Superhero's back story: ")
  add_new_hero(set_name, set_about, set_story)

def add_new_hero(set_name, set_about, set_story):
  new_hero = f"""
    INSERT INTO heroes(name, about_me, biography)
    VALUES ('{set_name}', '{set_about}', '{set_story}')
  """
  execute_query(new_hero)

  other_hero = input("\nDo you want to add another hero?\nEnter YES or NO: \n")
  if other_hero == "YES":
    set_new_hero()
  else: 
    start_menu()

############## DELETE ##############
def delete_hero():
  get_all_names()
  dead_hero = input("\nWhich hero is no longer with us?\n") 
  delete_info = f"""
    DELETE FROM heroes
    WHERE id = {dead_hero}
  """
  deleted = execute_query(delete_info)
  print("\nRIP\n")

  more_dead = input("\nDo you need to delete any other heroes?\nEnter YES or NO: \n")
  if more_dead == "YES":
    delete_hero()
  else: 
    start_menu()

############## EDIT ##############
def edit_hero_info():
  get_all_names()
  edit_hero = input("\nWhich Hero?\n")
  edit_info = input("\nWhich info?\n1: Name\n2: Byline\n3: Backstory\n")
  if edit_info == "1":
    new_name = input("Enter new Name: ")
    update_hero('heroes', 'name', new_name, edit_hero, 'id')
  elif edit_info == "2":
    new_byline = input("Enter new Byline: ")
    update_hero('heroes', 'about_me', new_byline, edit_hero, 'id') 
  elif edit_info == "3":
    new_story = input("Enter new Back Story: ")
    update_hero('heroes', 'biography', new_story, edit_hero, 'id')
  else:
    print("\nMake a valid choice and try again.\n\n")
  
  more_info = input("\nDo you need to edit more info?\nEnter YES or NO: \n")
  if more_info == "YES":
    edit_hero_info()
  else: 
    start_menu()










def header():
  subprocess.run('clear')
  print("""
  ********************************************************************
  ************************* SUPERHEROES UNITE ************************
  ********************************************************************
  """)




start_menu()

