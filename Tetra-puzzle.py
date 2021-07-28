### Tetra Puzzle ver.210727.02 rough draft, add T1~4 cases

import copy # to use deepcopy()

## Variables
SIZE = 9
frame = []


## Class & Functions
class Node() :
    def __init__(self):
        self.frame = None # remaining space in the frame
        self.data = None # puzzles filled in initial frame
        self.S = None
        self.Z1 = None
        self.Z2 = None
        self.J1 = None
        self.J2 = None
        self.J3 = None
        self.L1 = None
        self.L2 = None
        self.L3 = None
        self.T1 = None
        self.T2 = None
        self.T3 = None
        self.T4 = None
        self.I1 = None
        self.I2 = None
        self.O = None

        self.cnt_S = None # num of S shape blocks
        self.cnt_Z = None
        self.cnt_J = None
        self.cnt_L = None
        self.cnt_T = None
        self.cnt_I = None
        self.cnt_O = None

def inEmpty(i, j) :
    return (frame[i][j] == 0)

def can_S(i, j, frame) :
    return (frame[i][j] + frame[i+1][j] + frame[i+1][j+1] + frame[i+2][j+1] == 0)

def can_Z1(i, j) :
    return (frame[i][j] + frame[i][j+1] + frame[i+1][j+1] + frame[i+1][j+2] == 0)
    
def can_Z2(i, j) :
    return (frame[i][j] + frame[i+1][j] + frame[i+1][j-1] + frame[i+2][j-1] == 0)
    
def can_J1(i, j) :
    return (frame[i][j] + frame[i][j+1] + frame[i][j+2] + frame[i+1][j+2] == 0)

def can_J2(i, j) :
    return (frame[i][j] + frame[i+1][j] + frame[i+2][j] + frame[i+2][j-1] == 0)
    
def can_J3(i, j) :
    return (frame[i][j] + frame[i+1][j] + frame[i+1][j+1] + frame[i+1][j+2] == 0)
    
def can_L1(i, j) :
    return (frame[i][j] + frame[i+1][j] + frame[i+2][j] + frame[i+2][j+1] == 0)
   
def can_L2(i, j) :
    return (frame[i][j] + frame[i][j+1] + frame[i+1][j+1] + frame[i+2][j+1] == 0)

def can_L3(i, j) :
    return (frame[i][j] + frame[i+1][j] + frame[i+1][j-1] + frame[i+1][j-2] == 0)

def can_T1(i, j) :
    return (frame[i][j] + frame[i][j+1] + frame[i][j+2] + frame[i+1][j+1] == 0)

def can_T2(i, j) :
    return (frame[i][j] + frame[i+1][j] + frame[i+2][j] + frame[i+1][j+1] == 0)

def can_T3(i, j) :
    return (frame[i][j] + frame[i+1][j] + frame[i+2][j] + frame[i+1][j-1] == 0)

def can_T4(i, j) :
    return (frame[i][j] + frame[i+1][j] + frame[i+1][j+1] + frame[i+1][j-1] == 0)

def can_I1(i, j) :
    return (frame[i][j] + frame[i][j+1] + frame[i][j+2] + frame[i][j+3] == 0)

def can_I2(i, j) :
    return (frame[i][j] + frame[i+1][j] + frame[i+2][j] + frame[i+3][j] == 0)
    
def can_O(i, j) :
    return (frame[i][j] + frame[i][j+1] + frame[i+1][j+1] + frame[i+1][j] == 0)


root = Node()
current = root

def do_S(i,j,frame):
    global current
    current.S = copy.deepcopy(current)
    current.data.append([i,j,'S'])
    current.cnt_S += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1

'''
def do_Z1 :
def do_Z2 :
def do_J1 :
def do_J2 :
def do_J3 :
def do_L1 :
def do_L2 :
def do_L3 :
def do_I1 :
def do_I2 :
def do_O :
'''




def isComplete(frame) :
    for i, j in range(SIZE + 3):
        if (frame[i][j] == 0) :
            return False
    return True




def find_Cases(puzzle_frame):
    global SIZE
    for i, j in range(3, SIZE + 3):
        pass

# sample frame(for test)
def loadFrame() :
    frame = \
    [
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    ]    



# frame of puzzle, size of FoP == SIZE + 3 + 3 (including borderlines)




## Main

    