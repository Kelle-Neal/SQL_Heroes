from database.db_connection import execute_query

#execute_query("SELECT * FROM heroes WHERE id = %s", (1,))

#execute_query("SELECT * FROM heroes WHERE id = %s OR id = %s", (1,2))

execute_query("SELECT * FROM heroes WHERE id = %s", (1,)).fetchone()
print(hero)
