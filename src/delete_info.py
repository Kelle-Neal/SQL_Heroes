import psycopg
from database.db_connection import execute_query
# from get_name import get_hero_name

# def delete_hero_info():
#   del_info = execute_query("DELETE FROM heroes WHERE id = (get_hero)").fetchall()
# delete_hero_info()  

#       print("******************** SUPERHERO'S UNITE ********************\n")
#       get_all_names()
#       get_hero = input("\nWhich Superhero would you like to delete information about?\n\nEnter your selection: ")
#       subprocess.run('clear')

# get_hero = "7"

# def delete_hero_info():
#   for char in get_hero:
#     hero = input()
#     query = "DELETE FROM heroes WHere id = %s"
#     execute_query(query, (hero,))
#     print("All information for {hero} has been deleted")
#   delete_hero_info()  


cur = conn.cursor
DELETE FROM heroes WHERE id = %s
cur.execute(delete_sql, (get_hero))
conn commit()