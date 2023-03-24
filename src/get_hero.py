from database.db_connection import execute_query


def get_all_info():
  all_info = execute_query("SELECT id, name, about_me, biography FROM heroes ORDER BY name").fetchall()
  for id, name, about_me, biography in all_info:
    print((color.BOLD + name + color.END),"\n",about_me,"\n\n", biography,"\n\n")
  get_all_info()  

