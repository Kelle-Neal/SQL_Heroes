from database.db_connection import execute_query

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
  
  more_info = input("\nDo you need to edit more info?\nEnter 1 - YES or 2 - NO : \n")
  if more_info == "1":
    edit_hero_info()
  elif more_info == "2":
    start_menu()
  else:
    print("\nMake a valid choice and try again.\n\n")