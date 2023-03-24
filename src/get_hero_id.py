from database.db_connection import execute_query

def get_all_names():
  all_names = """
    SELECT name from heroes
  """
  get_names = execute_query(all_names).fetchall()
  for num, value in enumerate(get_names):
    print(f"{num +1}: {value[0]}")
  return get_names  
  

def edit_hero_info():
  get_all_names()
  edit_hero = input("\nWhich Hero?\n")
  edit_info = input("\nWhich info?\n1: Name\n2: Byline\n3: Backstory\n")
  if edit_info == "1":
    new_name = input("Enter new Name:")
    update_hero('heroes', new_name, edit_hero, 'id')
  elif edit_info == "2":
    new_byline = input("Enter new Byline:")
    update_hero('heroes', new_byline, edit_hero, 'id') 
  elif edit_info == "3":
    new_story = input("Enter new Back Story:")
    update_hero('heroes', new_story, edit_hero, 'id')
  else:
    print("\nMake a valid choice and try again.\n\n")
    











def delete_hero():
  get_all_names()
  dead_hero = input("\nWhich hero is no longer with us?\n") 
  delete_info = f"""
    DELETE FROM heroes
    WHERE id = {dead_hero}
  """
  execute_query(delete_info)
  print("\nRIP\n")
  print("\nThese are our remaining heroes:\n")
  get_all_names()

def add_new_hero(set_name, set_about, set_story):
  new_hero = f"""
    INSERT INTO heroes(name, about_me, biography)
    VALUES ('{set_name}', '{set_about}', '{set_story}')
  """
  execute_query(new_hero)
  

 
def set_hero_info():
  hero_info = f"""
    SELECT
      id,
      name,
      about_me,
      biography
    FROM heroes
    WHERE heroes.id = {num};  
  """
  info = execute_query(hero_info).fetchall()
  for count, value in enumerate(info):
    print(f"""
    {value[1]}\n
    {value[2]}\n
    {value[3]}\n
    """)




# def get_hero_info():
#   hero=hero_id
#   query = """
#     SELECT
#       heroes.name,
#       heroes.about_me,
#       heroes.biography
#     FROM heroes
#     JOIN abilities
#       ON heroes.id = abilities.hero_id
#     JOIN ability_types
#       ON ability_types.id = abilities.ability_type_id
#     WHERE heroes.id = hero
#   """       
#   returned_items = execute_query(query).fetchall()
#   for item in returned_items:
#     print(name,"\n",about_me,"\n\n",biography,"\n\n")
#   return hero_info  
# get_hero_info()







# def get_all_info(num):
#   all_info = execute_query("SELECT id, name, about_me, biography FROM heroes WHERE id = '{num}'").fetchall()
#   for id, name, about_me, biography in all_info:
#     print((color.BOLD + name + color.END),"\n",about_me,"\n\n", biography,"\n\n")
# get_all_info(num)




# def get_hero_info(num):
#   query = f"""
#     SELECT name, about_me, biography 
#     FROM heroes
#     WHERE id = '{num}'
#   """
#   returned_items = execute_query(query, (hero_id, )).fetchone()
#   for id, name, about_me, biography in returned_items:
#     print(f(color.BOLD + name + color.END),"\n",about_me,"\n\n",biography,"\n\n")
# get_hero_info(num)  
 

# def get_id():
#   query = """
#     SELECT id 
#     FROM heroes
#   """
#   returned_items = execute_query(query).fetchall()
#   for item in returned_items:
#     print(item[1])
#   return returned_items  
#   get_id()






# def which_hero():
#   hero = execute_query("Select id from heroes").fetchall()
#   get_hero_id = input("")
#   input("\nSelect Superhero by their number: ")

#   which_hero()


# def which_hero():
#   query = ("SELECT id FROM heroes")
#   get_hero_id = execute_query(query)
#   for id in get_hero_id:
#     print(id[1])
#   return get_hero_id
