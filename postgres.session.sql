CREATE VIEW [Friend or Foe] AS
SELECT hero1_id, hero2_id, relationship_type_id FROM relationships 
  WHERE EXISTS
  (SELECT name from relationship_types
  WHERE relationships.relationship_type_id = relationship_type.id)
  (SELECT name from heroes
  WHERE relationships.hero1_id = heroes.name)
  (SELECT name from heroes
  WHERE relationships.hero2_id = heroes.name)
