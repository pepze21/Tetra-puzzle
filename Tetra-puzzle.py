### Tetra Puzzle ver.210727.04 rough draft, shortened the length of the code by using indices


import copy # to use deepcopy()

## Variables
SIZE = 9
frame = []


## Class & Functions
class Node() :
    def __init__(self):
        self.frame = None # frame state
        self.blockData = [] # blocks filled in initial frame
        self.case = [None for _ in range(16)] #1S2Z3J3L4T2I1O:16cases
        self.cnt = [0 for _ in range(16)]

def findNext(frame):
    for i in range(3, SIZE + 3):
        for j in range(3, SIZE + 3):
            if (frame[i][j] == 0):
                return i, j # return (i, j) of tuple type

def isEmpty(i, j) :
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


def do_Z1 :
    global current
    current.Z1 = copy.deepcopy(current)
    current.data.append([i,j,'Z1'])
    current.cnt_Z1 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_Z2 :
    global current
    current.Z2 = copy.deepcopy(current)
    current.data.append([i,j,'Z2'])
    current.cnt_Z2 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_J1 :
    global current
    current.J1 = copy.deepcopy(current)
    current.data.append([i,j,'J1'])
    current.cnt_J1 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_J2 :
    global current
    current.J2 = copy.deepcopy(current)
    current.data.append([i,j,'J2'])
    current.cnt_J2 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_J3 :
    global current
    current.J3 = copy.deepcopy(current)
    current.data.append([i,j,'J3'])
    current.cnt_J3 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_L1 :
    global current
    current.L1 = copy.deepcopy(current)
    current.data.append([i,j,'L1'])
    current.cnt_S += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_L2 :
    global current
    current.L2 = copy.deepcopy(current)
    current.data.append([i,j,'L2'])
    current.cnt_L2 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_L3 :
    global current
    current.L3 = copy.deepcopy(current)
    current.data.append([i,j,'L3'])
    current.cnt_L3 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_T1 :
    global current
    current.T1 = copy.deepcopy(current)
    current.data.append([i,j,'T1'])
    current.cnt_T1 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_T2 :
    global current
    current.T2 = copy.deepcopy(current)
    current.data.append([i,j,'T2'])
    current.cnt_T2 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_T3 :
    global current
    current.T3 = copy.deepcopy(current)
    current.data.append([i,j,'T3'])
    current.cnt_T3 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_T4 :
    global current
    current.T4 = copy.deepcopy(current)
    current.data.append([i,j,'T4'])
    current.cnt_T4 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1    
def do_I1 :
    global current
    current.I1 = copy.deepcopy(current)
    current.data.append([i,j,'I1'])
    current.cnt_I1 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_I2 :
    global current
    current.I2 = copy.deepcopy(current)
    current.data.append([i,j,'I2'])
    current.cnt_I2 += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1
def do_O :
    global current
    current.O = copy.deepcopy(current)
    current.data.append([i,j,'O'])
    current.cnt_O += 1
    current.frame = copy.deepcopy(frame)
    current.frame[i][j] = 1
    current.frame[i+1][j] = 1
    current.frame[i+1][j+1] = 1
    current.frame[i+2][i+1] = 1




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

    