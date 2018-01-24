# The following initialization/starter/architecture code is borrowed from the 'Peg Jump Game'
# CSC 380/480 Winter 2018 - Professor Lytinen
from ParaD_stack import *
from random import shuffle

class block_world:
        def __init__(self, blocks):
                self.block_columns = blocks.copy()

        def __str__(self):
                return str(self.block_columns)

        def __eq__(self, other):
                return self.block_columns == other.block_columns

        def __hash__(self):
                return hash(str(self.block_columns))

        # Functions written by David Para
        def successors(self):
                new_state = []
                successor_states = []
                s = stack()

##                shuffle(self.block_columns)
                for i in self.block_columns:
                        index_i = self.block_columns.index(i)
                        if len(i) > 1:
                                # Unstack the blocks
                                unstacked = self.unstack_blocks(self.block_columns[index_i])
                                # Set the table
                                for u in unstacked:
                                        new_state.append(u)
                                for l in self.block_columns:
                                        
                                        if l == i:
                                                continue
                                        new_state.append(l)
                                successor_states.append(block_world(new_state))
                                # Reset for new state
                                new_state = []
                                s.clear()
                        else:
                                for j in self.block_columns:
                                        if j == i:
                                                continue
                                        # Stacks the blocks
                                        index_j = self.block_columns.index(j)
                                        bottom = self.block_columns[index_j]
                                        top = self.block_columns[index_i]
                                        stacked = self.stack_blocks(bottom, top)
                                        # Stores the stack in a list
                                        new_state.append(stacked)
                                        # Set the table
                                        for l in self.block_columns:
                                                if l == j or l == i:
                                                        continue
                                                new_state.append(l)
                                        successor_states.append(block_world(new_state))
                                        # Reset for next state
                                        new_state = []
                                        s.clear()
                return successor_states

        def stack_blocks(self, bottom, top):
                s = stack()
                s.push(bottom)
                s.push(top)
                return str(s)

        def unstack_blocks(self, blocks):
                bottom = blocks[1:]
                top = blocks[:1]
                return [bottom, top]


##bw = block_world(['a','b','c'])
##bw = block_world(['ab','c'])
##bw = block_world(['bac'])
##bw = block_world(['bd', 'c', 'a', 'ef'])
##print(bw)
##bw_s = bw.successors()
##for b in bw_s:
##        print(b)
