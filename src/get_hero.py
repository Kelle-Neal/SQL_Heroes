from database.db_connection import execute_query

def get_hero_id():
  get_hero = execute_query("SELECT id FROM heroes").fetchone(1)
  for id in get_hero:
    print(id[1],)
  get_hero_id()   
