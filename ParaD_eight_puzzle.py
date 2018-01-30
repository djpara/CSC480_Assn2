# Starter code borrowed from 'eigth_puzzle_state'\
# CSC 380/480 Winter 2018 -Professor Lytinen

from random import shuffle    # to randomize the order in which successors are visited
import math

class eight_puzzle_state:
    def __init__(self, tiles):
        self.tiles = tiles.copy()

    def __str__(self):
        answer = ''
        for i in range(9):
            answer += '{} '.format(self.tiles[i])
            if (i+1)%3 == 0:
                answer += '\n'
        return answer
    
    def __repr__(self):
        return 'eight_puzzle_state({})'.format(self.tiles)

    def __eq__(self, other):
        return self.tiles == other.tiles

    def __hash__(self):
        return hash(self.tiles[0])

    _strategy = 'best'

    md = 0

    def get_strategy(self):
        return self._strategy
    
    def set_strategy(self, strategy):
        self._strategy = strategy
    
    def del_strategy(self):
        del self._strategy
    
    def successors(self):
        successor_states = [ ]
        neighbors = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[4,6,8],8:[5,7]}
        zero_loc = self.tiles.index(' ')
        for loc in neighbors[zero_loc]:
            state = eight_puzzle_state(self.tiles)
            state.tiles[zero_loc] = state.tiles[loc]
            state.tiles[loc] = ' '
            successor_states.append(state)
        return successor_states

    def evaluation(self):
        if self.get_strategy() == 'best_correct':
            return self.evaluate_using_correct()
        else:
            return self.evaluate_using_md()

    def evaluate_using_md(self):
        gs = goal_state()
        md = 0
        for t in self.tiles:
            state_x_coord = get_x_coord(t, self.tiles)
            state_y_coord = get_y_coord(t, self.tiles)
            goal_x_coord = get_x_coord(t, gs.tiles)
            goal_y_coord = get_y_coord(t, gs.tiles)
            md += abs(state_x_coord - goal_x_coord) + abs(state_y_coord - goal_y_coord)
        self.md = md
        return md

    def evaluate_using_correct(self ):
        correct = 9
        for i in range(8):
            if self.tiles[i] != ['1', '2', '3', '8', ' ', '4', '7', '6', '5'][i]:
                correct -= 1
        return correct
    
    def __lt__(self, other):
        return self.evaluation() < other.evaluation()

# Helper function. Returns x or y coordinate of a given tile            
def get_x_coord(tile, tiles):
    index = tiles.index(tile)
    return index  % 3

def get_y_coord(tile, tiles):
    index = tiles.index(tile)
    return math.floor(index / 3)

# 8-puzzle always has the same goal state, so "dummy" is there
# only because goal_state takes 1 parameter
def goal_state(dummy=0):
    return eight_puzzle_state(['1', '2', '3', '8', ' ', '4', '7', '6', '5'])

# from random import shuffle   random puzzle is too many moves from goal state
from random import randint

# make a start state which is n moves from goal state
def start_state(distance=1):
    already_visited = [ goal_state() ]
    state = goal_state()
    # max number of moves from start state to goal state
    for i in range(distance):
        successors = state.successors()
        for s in successors:
            if s in already_visited:
                successors.remove(s)
        shuffle(successors)
        state = successors[0]
        already_visited.append(state)
    return state

def random_eight_puzzle_state():
    tiles = ['1', '2', '3', '4', '5', '6', '7', '8', ' ']
    shuffle(tiles)
    return eight_puzzle_state(tiles)
