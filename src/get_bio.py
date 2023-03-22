from db_connection import execute_query

get_bio = execute_query("SELECT id, name, biography FROM heroes ORDER BY name").fetchall()
for id, names, biography in get_bio:
  print(id,"-",names,"\n",biography,"\n")
