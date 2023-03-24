from database.db_connection import execute_query


# def get_hero_name():
#   get_name = execute_query("SELECT names FROM heroes").fetchone()
#   for name, in get_name:
#     print(name)
#   get_hero_name()

def get_hero_name():
  query = "SELECT id, name FROM heroes ORDER BY name ASC"
  hero_name = execute_query(query).fetchall()
  for id in hero_name:
    print(id) 