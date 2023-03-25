
from database.db_connection import execute_query
import sys, subprocess
from header import header
from get_hero import get_all_names, get_hero_id
from get_info import get_hero_info, get_other_hero
from edit_hero import edit_hero_info
from add_hero import add_new_hero, set_new_hero
from delete_hero import delete_hero

##### START #################################
def start_menu():
  header()
  start = input("What would you like to do today?\n\n1: See information about current Superheroes.\n2: Edit, Add or Delete info about a Superhero.\n\nEnter your selection: ")
##### SEE INFO ###############################
  if start == "1":
    header()
    get_hero_info()
##### EDIT ADD DELETE ########################
  elif start == "2":
    header()
    ead_info = input("What would you like to do with the Superhero's information\n1: Edit\n2: Add\n3: Delete\n\nEnter your selection: ")
##### EDIT ###################################
    if ead_info == "1":
      edit_hero_info()
##### ADD ####################################
    elif ead_info == "2":
      set_new_hero()
##### DELETE #################################
    elif ead_info == "3":
      delete_hero()
##### ERROR ##################################
    else:
      header()
      print("\nMake a valid choice and try again.\n\n")
      ead_info()
##### ERROR ##################################
  else:
    header()
    print("\nMake a valid choice and try again.")
    start_menu()
##### START ###################################
start_menu()