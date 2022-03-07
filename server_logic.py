import random
from typing import List, Dict
from xmlrpc.client import boolean

"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""


def avoid_my_neck(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
    """
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
            e.g. {"x": 0, "y": 0}
    my_body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'neck' direction removed
    """
    my_neck = my_body[1]  # The segment of body right after the head is the 'neck'

    if my_neck["x"] < my_head["x"]:  # my neck is left of my head
        possible_moves.remove("left")
    elif my_neck["x"] > my_head["x"]:  # my neck is right of my head
        possible_moves.remove("right")
    elif my_neck["y"] < my_head["y"]:  # my neck is below my head
        possible_moves.remove("down")
    elif my_neck["y"] > my_head["y"]:  # my neck is above my head
        possible_moves.remove("up")

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

    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    print(f"All board data this turn: {data}")
    print(f"My Battlesnakes head this turn is: {my_head}")
    print(f"My Battlesnakes body this turn is: {my_body}")

    possible_moves = ["up", "down", "left", "right"]

    snakes = data["board"]["snakes"]

    # Don't allow your Battlesnake to move back in on it's own neck
    #possible_moves = avoid_my_neck(my_head, my_body, possible_moves)

    board_height = data["board"]["height"]
    board_width = data["board"]["width"]

    # TODO: Using information from 'data', make your Battlesnake move towards a piece of food on the board
    # TODO: Explore new strategies for picking a move that are better than random

    if not is_up_safe(my_head, my_body, board_height, board_width, snakes):
        print(f"Removing up, it's dangerous!")
        possible_moves.remove("up")
    if not is_down_safe(my_head, my_body, board_height, board_width, snakes):
        print(f"Removing down, it's dangerous!")
        possible_moves.remove("down")
    if not is_left_safe(my_head, my_body, board_height, board_width, snakes):
        print(f"Removing left, it's dangerous!")
        possible_moves.remove("left")
    if not is_right_safe(my_head, my_body, board_height, board_width, snakes):
        print(f"Removing right, it's dangerous!")
        possible_moves.remove("right")

    # move = possible_moves[0] # random.choice(possible_moves)

    move = possible_moves[-1]

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move

def is_up_safe(my_head: Dict[str, int], my_body: List[dict], board_height: int, board_width: int, snakes) -> boolean:
    safeness = True
    if my_head["y"] == board_height-1:
        safeness = False

    new_coords = {"x": my_head["x"], "y": my_head["y"]+1}
    if new_coords in my_body:
            safeness = False

    for snake in snakes:
        if new_coords in snake["body"]:
            safeness = False
    return safeness

def is_down_safe(my_head: Dict[str, int], my_body: List[dict], board_height: int, board_width: int, snakes) -> boolean:
    safeness = True
    if my_head["y"] == 0:
        safeness = False

    new_coords = {"x": my_head["x"], "y": my_head["y"]-1}
    if new_coords in my_body:
            safeness = False
    
    for snake in snakes:
        if new_coords in snake["body"]:
            safeness = False

    return safeness

def is_left_safe(my_head: Dict[str, int], my_body: List[dict], board_height: int, board_width: int, snakes) -> boolean:
    safeness = True
    if my_head["x"] == 0:
        safeness = False

    new_coords = {"x": my_head["x"]-1, "y": my_head["y"]}
    if new_coords in my_body:
            safeness = False

    for snake in snakes:
        if new_coords in snake["body"]:
            safeness = False

    return safeness

def is_right_safe(my_head: Dict[str, int], my_body: List[dict], board_height: int, board_width: int, snakes) -> boolean:
    safeness = True
    if my_head["x"] == board_width-1:
        safeness = False

    new_coords = {"x": my_head["x"]+1, "y": my_head["y"]}
    if new_coords in my_body:
            safeness = False

    for snake in snakes:
        if new_coords in snake["body"]:
            safeness = False

    return safeness
