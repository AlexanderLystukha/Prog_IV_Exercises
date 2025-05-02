# Predicate : a method that returns true or false

def Is_Good_Game(game: tuple[int, str]) -> bool:
    return game[0] >= 25


my_games = [
    (27, "Great game"),
    (20, "average game"),
    (10, "Bad game :("),
    (12, "Bad game 2: Electric Boogaloo"),
    (7, "Brandon"),
    (25, "Average Game 2"),
    (49, "Best game evor oh my gawwwd")
]

print(list(filter(Is_Good_Game, my_games)))
