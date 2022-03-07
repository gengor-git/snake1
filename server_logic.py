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
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""


def avoid_my_body(my_body: List[dict], possible_moves: List[dict]) -> List[dict]:
    """
    my_body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    possible_moves: Dictionary of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'false' direction removed
    """
    to_remove =  []

    for direction, location in possible_moves.items():
        if location in my_body:
            to_remove.append(direction)

    for direction in to_remove:
        del possible_moves[direction]

    return possible_moves

def avoid_snakes(snakes, possible_moves: List[dict]) -> List[dict]:
    """
    snakes: The list of snakes to remove.
    possible_moves: Dictionary of moves.
    return: The dictionary of moves, which have no snake bodies in the way.
    """
    to_remove = []

    for snake in snakes:
        for direction, location in possible_moves.items():
            if location in snake["body"]:
                to_remove.append(direction)

    for direction in to_remove:
        del possible_moves[direction]

    return possible_moves

def avoid_walls(board_width, board_height, possible_moves: List[dict]) -> List[dict]:
    to_remove = []

    for direction, location in possible_moves.items():
        x_off_range = (location["x"] < 0 or location["x"] == board_width)
        y_off_range = (location["y"] < 0 or location["y"] == board_height)

    if x_off_range or y_off_range:
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

    # Don't allow your Battlesnake to move back in on it's own neck
    #possible_moves = avoid_my_neck(my_head, my_body, possible_moves)

    board_height = data["board"]["height"]
    board_width = data["board"]["width"]

    possible_moves = avoid_my_body(my_body, possible_moves)
    possible_moves = avoid_snakes(snakes, possible_moves)
    possible_moves = avoid_walls(board_width, board_height, possible_moves)

    possible_moves = list(possible_moves.keys())
    move = random.choice(possible_moves)

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move
