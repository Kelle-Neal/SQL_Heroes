from database.db_connection import execute_query
from get_hero import get_all_names
from main import start_menu


def set_new_hero():
  get_all_names()

  set_name = str(input("\nEnter new Superhero's name: "))
  set_byline = str(input("\nEnter new Superhero's Byline: "))
  set_story = str(input("\nEnter new Superhero's back story: "))
  add_new_hero(set_name, set_byline, set_story)

def add_new_hero(set_name, set_byline, set_story):
  new_hero = f"""
    INSERT INTO heroes(name, about_me, biography)
    VALUES ('{set_name}', '{set_byline}', '{set_story}')
  """
  execute_query(new_hero)

  other_hero = input("\nDo you want to add another hero?\n1-YES or 2-NO : \n")
  if other_hero == "1":
    set_new_hero()
  elif other_hero == "2":
    start_menu()
  else:
    print("\nMake a valid choice and try again.\n\n")

set_new_hero()