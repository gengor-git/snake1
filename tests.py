"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

    python tests.py -v

"""
import unittest
from server_logic import avoid_snakes

class AvoidSnakesTest(unittest.TestCase):
    def test_avoid_snakes_up(self):
        my_head = {"x": 2, "y": 3}
        expected_moves = {
            "up": {
                "x": my_head["x"], 
                "y": my_head["y"] + 1
            }
        }
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
        snakes = [
            {
            "id": "test1",
            "name": "Test Snake 1",
            "health": 54,
            "body": [
                {"x": 2, "y": 3}, 
                {"x": 1, "y": 3}, 
                {"x": 0, "y": 3}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                        "color":"#26CF04",
                        "head":"smile",
                        "tail":"bolt"
                        }
            },
            {
            "id": "test2",
            "name": "Test Snake 2",
            "health": 54,
            "body": [
                {"x": 3, "y": 3}, 
                {"x": 3, "y": 2}, 
                {"x": 2, "y": 2}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                        "color":"#26CF04",
                        "head":"smile",
                        "tail":"bolt"
                        }
            },

        ]

        result_moves = avoid_snakes(snakes, possible_moves)
        self.assertEqual(len(result_moves), 1)
        self.assertDictEqual(expected_moves, result_moves)

    def test_avoid_snakes_down(self):
        my_head = {"x": 2, "y": 3}
        expected_moves = {
            "down": {
                "x": my_head["x"], 
                "y": my_head["y"] - 1
            }
        }
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
        snakes = [
            {
            "id": "test1",
            "name": "Test Snake 1",
            "health": 54,
            "body": [
                {"x": 2, "y": 3}, 
                {"x": 1, "y": 3}, 
                {"x": 0, "y": 3}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                        "color":"#26CF04",
                        "head":"smile",
                        "tail":"bolt"
                        }
            },
            {
            "id": "test2",
            "name": "Test Snake 2",
            "health": 54,
            "body": [
                {"x": 3, "y": 3}, 
                {"x": 3, "y": 4}, 
                {"x": 2, "y": 4}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                        "color":"#26CF04",
                        "head":"smile",
                        "tail":"bolt"
                        }
            },

        ]

        result_moves = avoid_snakes(snakes, possible_moves)
        self.assertEqual(len(result_moves), 1)
        self.assertDictEqual(expected_moves, result_moves)


    def test_avoid_snakes_left(self):
        my_head = {"x": 2, "y": 2}
        expected_moves = {
            "left": {
                "x": my_head["x"] - 1, 
                "y": my_head["y"]
            }
        }
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
        snakes = [
            {
            "id": "test1",
            "name": "Test Snake 1",
            "health": 54,
            "body": [
                {"x": 2, "y": 2}, 
                {"x": 2, "y": 1}, 
                {"x": 2, "y": 0}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                        "color":"#26CF04",
                        "head":"smile",
                        "tail":"bolt"
                        }
            },
            {
            "id": "test2",
            "name": "Test Snake 2",
            "health": 54,
            "body": [
                {"x": 2, "y": 3}, 
                {"x": 3, "y": 3}, 
                {"x": 3, "y": 2}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                        "color":"#26CF04",
                        "head":"smile",
                        "tail":"bolt"
                        }
            },

        ]

        result_moves = avoid_snakes(snakes, possible_moves)
        self.assertEqual(len(result_moves), 1)
        self.assertDictEqual(expected_moves, result_moves)


    def test_avoid_snakes_right(self):
        my_head = {"x": 2, "y": 2}
        expected_moves = {
            "right": {
                "x": my_head["x"] + 1, 
                "y": my_head["y"]
            }
        }
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
        snakes = [
            {
            "id": "test1",
            "name": "Test Snake 1",
            "health": 54,
            "body": [
                {"x": 2, "y": 2}, 
                {"x": 2, "y": 1}, 
                {"x": 2, "y": 0}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                        "color":"#26CF04",
                        "head":"smile",
                        "tail":"bolt"
                        }
            },
            {
            "id": "test2",
            "name": "Test Snake 2",
            "health": 54,
            "body": [
                {"x": 2, "y": 3}, 
                {"x": 1, "y": 3}, 
                {"x": 1, "y": 2}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                        "color":"#26CF04",
                        "head":"smile",
                        "tail":"bolt"
                        }
            },

        ]

        result_moves = avoid_snakes(snakes, possible_moves)
        self.assertEqual(len(result_moves), 1)
        self.assertDictEqual(expected_moves, result_moves)

if __name__ == "__main__":
    unittest.main()
