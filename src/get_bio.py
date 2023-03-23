from database.db_connection import execute_query

def get_bio_info():
  get_bios = execute_query("SELECT id, name, biography FROM heroes ORDER BY name").fetchall()
  for id, names, biography in get_bios:
    print(id,"-",names,"\n",biography,"\n")
  get_bio_info()

