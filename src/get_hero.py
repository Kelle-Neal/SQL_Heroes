from database.db_connection import execute_query
from header import header


def get_all_names():
  header()
  all_names = """
    SELECT id, name 
    FROM heroes 
    ORDER BY NAME
  """
  get_names = execute_query(all_names).fetchall()
  for id, names in get_names:
    print(id,"-",names)

##### HERO ID #################################
def get_hero_id():
  get_all_names()
  hero_id = (input("\nSelect Superhero by their number: "))
  return hero_id

