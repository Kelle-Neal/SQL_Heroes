from database.db_connection import execute_query
get_hero = 2

def get_all_info():
  get_hero = execute_query("SELECT.id FROM heroes").fetchone()
  get_hero_info = execute_query("SELECT id, names, about_me, biography FROM heroes WHERE heroes.id = get_hero").fetchone()
  for id, names, about_me, biography in get_hero_info:
 
    print(names,"\n",about_me,"\n", biography)
  get_all_info()  


# def get_all_names():
#   get_names = execute_query("SELECT id, name FROM heroes ORDER BY name").fetchall()
#   for id, names in get_names:
#     print(id,"-",names)
# get_all_names()  