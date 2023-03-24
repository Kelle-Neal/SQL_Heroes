from database.db_connection import execute_query, query


# postgres =# insert into HEROES (name, about_me, biography)
#   values('Koo Koo Kangaroo', 'A superhero duo who fight evil through song', 'Best friends since kindergarten Koo Koo Kangaroo no longer have their own identities and prefer to only be referred to as Koo Koo Kangaroo collectively. Not much is known about the song singing duo except they often wear disguises while singing their songs to blend in.  This song singing duo has fought sadness and strife for years and continues to do so.');
# INSERT 0 1
# postgres=#


# INSERT INTO Heroes VALUES ('Koo Koo Kangaroo', 'A superhero duo who fight evil through song', 'Best friends since kindergarten Koo Koo Kangaroo no longer have their own identities and prefer to only be referred to as Koo Koo Kangaroo collectively. Not much is known about the song singing duo except they often wear disguises while singing their songs to blend in. Koo Koo Kangaroo has fought sadness and strife for years and continues to do so.')

def create_new_hero(name, about_me, biography):
  new_hero = (INSERT INTO heroes (name, about_me, biography)
    VALUES ('Koo Koo Kangaroo', 'A superhero duo who fight evil through song', 'Best friends since kindergarten Koo Koo Kangaroo no longer have their own identities and prefer to only be referred to as Koo Koo Kangaroo collectively. Not much is known about the song singing duo except they often wear disguises while singing their songs to blend in and create drama. Koo Koo Kangaroo has fought sadness and strife for years and continues to do so.')
  execute_query(query, (%s, %s, %s))
  create_new_hero()

  