from database.db_connection import execute_query

def delete_hero():
  get_all_names()
  dead_hero = input("\nWhich hero is no longer with us?\n")
  cause_of_death = input("\nEnter cause of death: ") 
  delete_info = f"""
    DELETE FROM heroes
    WHERE id = {dead_hero}
  """
  deleted = execute_query(delete_info)
  print("\nRIP\n")

  more_dead = input("\nHave any other hero's died today?\nEnter 1 - YES or 2 - NO : \n")
  if more_dead == "1":
    delete_hero()
  elif more_dead == "2":
    start_menu()
  else:
    print("\nMake a valid choice and try again.\n\n")
