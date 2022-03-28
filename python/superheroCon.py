# https://www.codewars.com/kata/6202149e89771200306428f0

# This was solved using graph theory.
# if a node's neighbors have connections to each other, it is not solvable
def is_possible(database: dict) -> bool:
    for key in database:
        for value in database[key]:
            if key == value: return False   # Superheroes can hate themselves and then they don't want to attend :(
            if value == []: break           # if empty, it is disconnected and can be ignored
            for hero in database[value]:
                if hero in database[key]: return False
    return True