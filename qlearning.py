import copy
import random


def move(direction):
    playerIndex = game.index('P')
    # right
    if direction == 1:
        if playerIndex < len(game):
            if game[playerIndex + 1] == 'x':
                game[playerIndex + 1] = 'P'
                game[playerIndex] = 'x'
                return 0
            elif game[playerIndex + 1] == 'o':
                game[playerIndex] = 'x'
                game[playerIndex + 1] = 'O'
                return -1
            elif game[playerIndex + 1] == 'c':
                game[playerIndex] = 'x'
                game[playerIndex + 1] = 'C'
                return 1
    # left
    elif direction == 0:
        if playerIndex != 0:
            if game[playerIndex - 1] == 'x':
                game[playerIndex - 1] = 'P'
                game[playerIndex] = 'x'
                return 0
            elif game[playerIndex - 1] == 'o':
                game[playerIndex] = 'x'
                game[playerIndex - 1] = 'O'
                return -1
            elif game[playerIndex - 1] == 'c':
                game[playerIndex] = 'x'
                game[playerIndex - 1] = 'C'
                return 1


def initQ(rows, columns):
    return [[random.random() / 10 for x in range(columns)] for y in range(rows)]


states = 14
actions = 2

learningRate = 0.2
discount = 0.6
epsilon = 0.8

initialState = 4
currentState = initialState
nextState = initialState

q = initQ(states, actions)
firstQ = copy.deepcopy(q)

for i in range(200):
    game = ['x', 'x', 'o', 'x', 'P', 'x', 'x', 'x', 'x', 'x', 'x', 'c', 'x', 'x']
    moves = 0
    initialState = 4
    currentState = initialState
    nextState = initialState
    while True:
        moves += 1
        # maybe epsilon 0-10 instead of 1< to avoid division?
        if (random.random() > epsilon):
            action = random.randint(0, 1)
        else:
            action = q[currentState].index(max(q[currentState]))

        reward = move(action)

        if (action == 0):
            nextState -= 1
        else:
            nextState += 1

        q[currentState][action] = q[currentState][action] + learningRate * (
        reward + discount * max(q[nextState]) - q[currentState][action])

        currentState = nextState
        if reward == 1 or reward == -1:
            print('Attempt:' + str(i) + ' Move:' + str(moves))
            print(''.join(game) + '\n')
            break
print('Initial state:')
game = ['x', 'x', 'o', 'x', 'P', 'x', 'x', 'x', 'x', 'x', 'x', 'c', 'x', 'x']
print(''.join(game))
for i in range(states):
    print("{0:.2f}".format(firstQ[i][0]) + ' ' + "{0:.2f}".format(firstQ[i][1]) + ' =>>> ' + "{0:.2f}".format(
        q[i][0]) + ' ' + "{0:.2f}".format(q[i][1]))
