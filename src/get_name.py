from database.db_connection import execute_query

def get_hero_name(get_hero):
  get_name = execute_query("SELECT names FROM heroes").fetchone(get_hero)
  for names, in get_name:
    print(names)
  get_hero_name()

