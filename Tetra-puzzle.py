### Tetra Puzzle ver.210727.04 rough draft, shortened the length of the code by using indices


import copy # to use deepcopy()

## Variables
SIZE = 9
frame = []
history = []
cnt = [0 for _ in range(16)]

## Class & Functions

'''
class Node() :
    def __init__(self):
        self.frame = None # frame state
        self.blockData = [] # blocks filled in initial frame
        self.type = [None for _ in range(16)] #1S2Z3J3L4T2I1O:16cases
        self.cnt = [0 for _ in range(16)]
'''

def findNext(frame):
    for i in range(3, SIZE + 3):
        for j in range(3, SIZE + 3):
            if (frame[i][j] == 0):
                return i, j # return (i, j) of tuple type

def isEmpty(i, j) :
    return (frame[i][j] == 0)


# typeNo : 0:S  / 1:Z1 /  2:Z2 /  3:J1 /  4:J2 /  5:J3 /  6:L1 /  7:L2
#          8:L3 / 9:T1 / 10:T2 / 11:T3 / 12:T4 / 13:I1 / 14:I2 / 15:O
def canAdd(typeNo, i, j, frame) :
    if typeNo == 0 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+1][j+1] + frame[i+2][j+1] == 0)                
    elif typeNo == 1 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i+1][j+1] + frame[i+1][j+2] == 0)
    elif typeNo == 2 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+1][j-1] + frame[i+2][j-1] == 0)    
    elif typeNo == 3 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i][j+2] + frame[i+1][j+2] == 0)
    elif typeNo == 4 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+2][j] + frame[i+2][j-1] == 0)    
    elif typeNo == 5 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+1][j+1] + frame[i+1][j+2] == 0)    
    elif typeNo == 6 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+2][j] + frame[i+2][j+1] == 0)   
    elif typeNo == 7 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i+1][j+1] + frame[i+2][j+1] == 0)
    elif typeNo == 8 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+1][j-1] + frame[i+1][j-2] == 0)
    elif typeNo == 9 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i][j+2] + frame[i+1][j+1] == 0)
    elif typeNo == 10 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+2][j] + frame[i+1][j+1] == 0)
    elif typeNo == 11 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+2][j] + frame[i+1][j-1] == 0)
    elif typeNo == 12 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+1][j+1] + frame[i+1][j-1] == 0)
    elif typeNo == 13 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i][j+2] + frame[i][j+3] == 0)
    elif typeNo == 14 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+2][j] + frame[i+3][j] == 0)    
    elif typeNo == 15 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i+1][j+1] + frame[i+1][j] == 0)


def blockSwitch(typeNo, i, j, frame) : #add or remove a block
    # temp_frame = copy.deepcopy(frame)
    if typeNo == 0 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+2][j+1] ^= 1
    elif typeNo == 1 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+1][j+2] ^= 1
    elif typeNo == 2 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j-1] ^= 1
        frame[i+2][j-1] ^= 1
    elif typeNo == 3 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i][j+2] ^= 1
        frame[i+1][j+2] ^= 1
    elif typeNo == 4 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
        frame[i+2][j-1] ^= 1
    elif typeNo == 5 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+1][j+2] ^= 1
    elif typeNo == 6 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
        frame[i+2][j+1] ^= 1
    elif typeNo == 7 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+2][j+1] ^= 1
    elif typeNo == 8 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j-1] ^= 1
        frame[i+1][j-2] ^= 1
    elif typeNo == 9 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i][j+2] ^= 1
        frame[i+1][j+1] ^= 1
    elif typeNo == 10 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
        frame[i+1][j+1] ^= 1
    elif typeNo == 11 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
        frame[i+1][j-1] ^= 1
    elif typeNo == 12 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+1][j-1] ^= 1
    elif typeNo == 13 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i][j+2] ^= 1
        frame[i][j+3] ^= 1
    elif typeNo == 14 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
        frame[i+3][j] ^= 1
    elif typeNo == 15 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+1][j] ^= 1
    else :
        print("error : unknown typeNo")

'''
def nowFrame(history, frame): # history = [(typeNo, i, j), ... ]
    for blockData in history:
        blockSwitch(*blockData, frame)
'''



def isComplete(frame) :
    for i, j in range(SIZE + 3):
        if (frame[i][j] == 0) :
            return False
    return True



# sample frame(for test)
def load_frame() :
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
    return frame


# frame of puzzle, size of FoP == SIZE + 3 + 3 (including borderlines)


def currentFrame() :
    global history, frame
    current_frame = copy.deepcopy(frame)
    for blockData in history : # history = [(typeNo, i, j), ...]
        blockSwitch(*blockData, current_frame)
    return current_frame

def findCases() :
    global history, frame    
    for typeNo in range(16) :
        current_frame = currentFrame()
        i, j = findNext(current_frame)
        if canAdd(typeNo, i, j, current_frame) :
            blockSwitch(typeNo, i, j, current_frame)
            history.append((typeNo, i, j))
            cnt[typeNo] += 1
            findCases()
        else :
            cnt[history.pop()[0]] -= 1
            break


## Main
def main():
    global history, frame
    frame = load_frame()

    findCases()
    
    


if __name__ == "__main__" :
    main()