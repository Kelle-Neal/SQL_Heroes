from database.db_connection import execute_query

def get_friends():
  get_allies = execute_query("SELECT hero1_id, hero2_id, relationship_type_id FROM relationships").fetchall()
  for hero1_id, hero2_id, relationship_type_id in get_allies:
    print(hero1_id,"is allies with ","\n")
  get_friends()

hero1_id, hero2_id, relationship_type_id