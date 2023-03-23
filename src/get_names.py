from database.db_connection import execute_query


# def get_all_names():
#   query = "SELECT * FROM heroes"
#   get_names = execute_query(query).fetchall
#   for names in get_names:
#     print(id,"-",names)
#   return get_names  
# get_all_names()  


def get_all_names():
  get_names = execute_query("SELECT id, name FROM heroes ORDER BY name").fetchall()
  for id, names in get_names:
    print(id,"-",names)
get_all_names()  






# def get_names():
#   query = SELECT id, name FROM heroes ORDER by name
#   all_names = execute_query(query).fetchall
#   for name in all_names:
#     print(name[1])
#   return all_names
  
  