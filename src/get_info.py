from database.db_connection import execute_query
from header import header
from get_hero import get_all_names

##### HERO ID #################################
def get_hero_info():
  get_all_names()
  hero_id = (input("\nSelect Superhero by their number: "))
  hero_info = """
    SELECT
      id,
      name,
      about_me,
      biography
    FROM heroes
    WHERE heroes.id = %s
  """
  info = execute_query(hero_info, (hero_id,)).fetchall()
  for id, name, about_me, biography in hero_info:
    print (f"""
      name

      about_me

      biography

    """)
  get_other_hero()

def get_other_hero():
  other_hero = input("\nDo you want to see information about a different hero?\nEnter 1 - YES or 2 - NO : \n")
  if other_hero == "1":
    get_hero_info()
  elif other_hero == "2":
    start_menu()
  else:
    print("\nMake a valid choice and try again.\n\n")

# def get_all_info():
#   all_info = execute_query("SELECT id, name, about_me, biography FROM heroes ORDER BY name").fetchall()
#   for id, name, about_me, biography in all_info:
#     print((color.BOLD + name + color.END),"\n",about_me,"\n\n", biography,"\n\n")
#   get_all_info()      