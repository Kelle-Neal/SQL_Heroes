from database.db_connection import execute_query
import sys, subprocess

def header():
  subprocess.run('clear')
  print("""
  ********************************************************************
  ************************* SUPERHEROES UNITE ************************
  ********************************************************************
  """)
