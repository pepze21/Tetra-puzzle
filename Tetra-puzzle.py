### Tetra Puzzle ver.210731.05, add 3 missing cases

import copy

## Variables
SIZE = 9
frame = []
history = []
solutions = []

## Functions
def findNext(frame):
    for i in range(3, SIZE + 3):
        for j in range(3, SIZE + 3):
            if (frame[i][j] == 0):
                return i, j

# typeNo : 0:S1 /  1:S2 /  2:Z1 /  3:Z2 /  4:J1 /  5:J2 /  6:J3 /
#          7:J4 /  8:L1 /  9:L2 / 10:L3 / 11:L4 / 12:T1 / 13:T2 /
#         14:T3 / 15:T4 / 16:I1 / 17:I2 / 18:O
def canAdd(typeNo, i, j, frame) :
    if typeNo == 0 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+1][j+1] + frame[i+2][j+1] == 0)
    elif typeNo == 1 : # new1
        return (frame[i][j] + frame[i][j+1] + \
                frame[i+1][j] + frame[i+1][j-1] == 0)
    elif typeNo == 2 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i+1][j+1] + frame[i+1][j+2] == 0)
    elif typeNo == 3 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+1][j-1] + frame[i+2][j-1] == 0)    
    elif typeNo == 4 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i][j+2] + frame[i+1][j+2] == 0)
    elif typeNo == 5 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+2][j] + frame[i+2][j-1] == 0)    
    elif typeNo == 6 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+1][j+1] + frame[i+1][j+2] == 0)
    elif typeNo == 7 : # new 7
        return (frame[i][j] + frame[i][j+1] + \
                frame[i+1][j] + frame[i+2][j] == 0)    
    elif typeNo == 8 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+2][j] + frame[i+2][j+1] == 0)   
    elif typeNo == 9 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i+1][j+1] + frame[i+2][j+1] == 0)
    elif typeNo == 10 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+1][j-1] + frame[i+1][j-2] == 0)
    elif typeNo == 11 : # new 11
        return (frame[i][j] + frame[i][j+1] + \
                frame[i][j+2] + frame[i+1][j] == 0)
    elif typeNo == 12 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i][j+2] + frame[i+1][j+1] == 0)
    elif typeNo == 13 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+2][j] + frame[i+1][j+1] == 0)
    elif typeNo == 14 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+2][j] + frame[i+1][j-1] == 0)
    elif typeNo == 15 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+1][j+1] + frame[i+1][j-1] == 0)
    elif typeNo == 16 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i][j+2] + frame[i][j+3] == 0)
    elif typeNo == 17 :
        return (frame[i][j] + frame[i+1][j] + \
                frame[i+2][j] + frame[i+3][j] == 0)    
    elif typeNo == 18 :
        return (frame[i][j] + frame[i][j+1] + \
                frame[i+1][j+1] + frame[i+1][j] == 0)

def blockSwitch(typeNo, i, j, frame) :
    if typeNo == 0 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+2][j+1] ^= 1
    elif typeNo == 1 : # new1
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j-1] ^= 1
    elif typeNo == 2 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+1][j+2] ^= 1
    elif typeNo == 3 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j-1] ^= 1
        frame[i+2][j-1] ^= 1
    elif typeNo == 4 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i][j+2] ^= 1
        frame[i+1][j+2] ^= 1
    elif typeNo == 5 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
        frame[i+2][j-1] ^= 1
    elif typeNo == 6 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+1][j+2] ^= 1
    elif typeNo == 7 : # new7
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
    elif typeNo == 8 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
        frame[i+2][j+1] ^= 1
    elif typeNo == 9 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+2][j+1] ^= 1
    elif typeNo == 10 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j-1] ^= 1
        frame[i+1][j-2] ^= 1
    elif typeNo == 11 : # new11
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i][j+2] ^= 1
        frame[i+1][j] ^= 1
    elif typeNo == 12 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i][j+2] ^= 1
        frame[i+1][j+1] ^= 1
    elif typeNo == 13 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
        frame[i+1][j+1] ^= 1
    elif typeNo == 14 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
        frame[i+1][j-1] ^= 1
    elif typeNo == 15 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+1][j-1] ^= 1
    elif typeNo == 16 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i][j+2] ^= 1
        frame[i][j+3] ^= 1
    elif typeNo == 17 :
        frame[i][j] ^= 1
        frame[i+1][j] ^= 1
        frame[i+2][j] ^= 1
        frame[i+3][j] ^= 1
    elif typeNo == 18 :
        frame[i][j] ^= 1
        frame[i][j+1] ^= 1
        frame[i+1][j+1] ^= 1
        frame[i+1][j] ^= 1
    else :
        print("error : unknown typeNo")

def isComplete(frame) :
    for i in range(3, SIZE + 3):
        for j in range(3, SIZE +3):
            if (frame[i][j] == 0) :
                return False
    return True

def cnt_ClassifiedBlockType(history) :
    cnt = [0 for _ in range(16)]
    for blockData in history :
        cnt[blockData[0]] += 1
    cnt_classified = [0 for _ in range(7)]
    cnt_classified[0] = cnt[0]
    cnt_classified[1] = cnt[1]  + cnt[2]
    cnt_classified[2] = cnt[3]  + cnt[4]  + cnt[5]
    cnt_classified[3] = cnt[6]  + cnt[7]  + cnt[8]
    cnt_classified[4] = cnt[9]  + cnt[10] + cnt[11] + cnt[12]
    cnt_classified[5] = cnt[13] + cnt[14]
    cnt_classified[6] = cnt[15]
    return cnt_classified
    
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
    return frame

def findCases() :
    global history, frame, solutions
    for typeNo in range(16) :
        if isComplete(frame) :
            solutions.append(copy.deepcopy(history))
            blockSwitch(*history.pop(), frame)
            break
        i, j = findNext(frame)
        if canAdd(typeNo, i, j, frame) :
            blockSwitch(typeNo, i, j, frame)
            history.append((typeNo, i, j))
            findCases()
        elif typeNo == 15 :
            blockSwitch(*history.pop(), frame)

def main():
    global history, frame, solutions
    initial_frame = loadFrame()
    frame = copy.deepcopy(initial_frame)

    findCases()
    
    for history in solutions :
        print(history)
        print("S Z J L T I O 갯수")
        print(cnt_ClassifiedBlockType(history))

## Main
if __name__ == "__main__" :
    main()
