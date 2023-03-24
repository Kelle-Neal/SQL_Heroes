from psycopg import cursor
from database.db_connection import execute_query 
from colors import color
import textwrap





















# def get_hero_info():
#   hero = """
#     SELECT id, name, about_me, biography 
#     FROM heroes 
#     """
#   hero_info = execute_query(hero).fetchone()
#   for id, name, about_me, biography in hero_info:
#     print((color.BOLD + name + color.END),"\n",about_me,"\n\n",biography,"\n\n")
# get_hero_info()  




# def get_all_info():
#   # get_hero = execute_query("SELECT.id FROM heroes").fetchall()
#   get_hero_info = execute_query("SELECT id, names, about_me, biography FROM heroes WHERE heroes.id = get_hero").fetchone()
#   for id, names, about_me, biography in get_hero_info:
#     print(names,"\n",about_me,"\n", biography)
#   get_all_info()


# def get_all_names():
#   get_names = execute_query("SELECT id, name FROM heroes ORDER BY name").fetchall()
#   for id, names in get_names:
#     print(id,"-",names)
# get_all_names()  

# wrapper = textwrap.TextWrapper(width=60)

def get_all_info():
  all_info = execute_query("SELECT id, name, about_me, biography FROM heroes ORDER BY name").fetchall()
  for id, name, about_me, biography in all_info:
    print((color.BOLD + name + color.END),"\n",about_me,"\n\n", biography,"\n\n")

get_all_info()  


# get_hero=int(7)

# def get_hero_info():

#   hero_info = execute_query("SELECT id, name, about_me, biography FROM heroes WHERE heroes.id = 'get_hero'").fetchall()

    
#   for id, name, about_me, biography in hero_info:
#     print((color.BOLD + name + color.END),"\n",about_me,"\n\n", biography,"\n\n")

# get_hero_info()  


