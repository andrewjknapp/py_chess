from stockfish import Stockfish
import os

def clear():
    os.system('clear')

def isGameOver():
    eval = engine.get_evaluation()
    return eval['type'] == "mate" and eval['value'] == 0

engine = Stockfish()
user_color = 'white'
move_number = 1
clear()

# Get level
while True:
    engine_level = int(input("Enter desired computer level (0-20): "))

    if engine_level < 0 or engine_level > 20:
        clear() 
        print("Invalid selection, try again\n")
    else:
        engine.set_skill_level(engine_level)
        break

# Get Color
while True:
    user_color = input("Choose which color to play as (white, black): ")

    if (not user_color == 'white') and (not user_color == 'black'):
        clear() 
        print("Invalid selection, try again")
    else:
        break

clear()


# If user is black have computer make first move
if (user_color == 'black'):
    engine_move = engine.get_best_move()

    engine.make_moves_from_current_position([engine_move])

    print(f"Computer move: {engine_move}\n")


while True:

    user_move = input("Enter move: ")

    if not engine.is_move_correct(user_move):
        print("Invalid move, try again")
        continue

    engine.make_moves_from_current_position([user_move])

    if (isGameOver()):
        print("Checkmate, congrats, you won!")
        break

    engine_move = engine.get_best_move()

    engine.make_moves_from_current_position([engine_move])

    print(f"Computer move: {engine_move}\n")

    if (isGameOver()):
        print("Checkmate, computer won")
        break

