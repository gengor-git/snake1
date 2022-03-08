from crypt import methods
from fnmatch import fnmatch
from lib2to3.pgen2.pgen import DFAState
from logging.config import DEFAULT_LOGGING_CONFIG_PORT
import random
from re import I
from typing import List, Dict
from xml.dom.pulldom import default_bufsize
from xmlrpc.client import boolean

"""
Movement logic for Snake1.
"""

def avoid_snakes(snakes: List[dict], possible_moves: List[dict]) -> List[dict]:
    """
    snakes: The list of snakes to remove.
    possible_moves: Dictionary of moves.
    return: The dictionary of moves, which have no snake bodies in the way.
    """
    to_remove = []

    for snake in snakes:
        for direction, location in possible_moves.items():
            if location in snake["body"]:
                print(f"Removing {direction}")
                to_remove.append(direction)

    for direction in to_remove:
        del possible_moves[direction]

    return possible_moves

def avoid_walls(board_width: int, board_height: int, possible_moves: List[dict]):
    """
    board_width: The width of the board.
    board_height: The height of the board.
    possible_moves: The dictionary of moves to check against.
    return: The dictionary of moves that are not moving into walls.
    """
    to_remove = []

    for direction, location in possible_moves.items():
        x_off_range = (location["x"] < 0 or location["x"] == board_width)
        y_off_range = (location["y"] < 0 or location["y"] == board_height)

        if x_off_range or y_off_range:
            print(f"Removing {direction}")
            to_remove.append(direction)

    for direction in to_remove:
        del possible_moves[direction]

    return possible_moves



def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    """
    my_head = data["you"]["head"]  # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]

    print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    print(f"All board data this turn: {data}")
    print(f"My Battlesnakes head this turn is: {my_head}")
    print(f"My Battlesnakes body this turn is: {my_body}")

    # possible_moves = ["up", "down", "left", "right"]
    possible_moves = {
        "up": {
            "x": my_head["x"], 
            "y": my_head["y"] + 1
        }, 
        "down": {
            "x": my_head["x"], 
            "y": my_head["y"] - 1
        }, 
        "left": {
            "x": my_head["x"] - 1, 
            "y": my_head["y"]
        }, 
        "right": {
            "x": my_head["x"] + 1, 
            "y": my_head["y"]
        }, 
    }

    snakes = data["board"]["snakes"]
    food = data["board"]["food"]

    board_height = data["board"]["height"]
    board_width = data["board"]["width"]

    possible_moves = avoid_snakes(snakes, possible_moves)
    possible_moves = avoid_walls(board_width, board_height, possible_moves)

    possible_moves = list(possible_moves.keys())
    move = random.choice(possible_moves)

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move
