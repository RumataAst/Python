import random, sys

#loops until i receive valid feedback from user
def getPlayerMove():
    inputOptions = ['r','p','s']

    while True: # Player input loop
        print('Enter you move: (r)ock (p)aper or (s)cissors ... you can always (q)uit as well')
        playerMove = input().lower().strip()
        if playerMove == 'q':
            print("Bye bye")
            sys.exit()
        elif playerMove in inputOptions :
            return playerMove
        else:
            print("Try again")

# using transition table. looking at the most popular move following current response
# For example user tends to use Rock after Paper a lot so coutner move to paper will be scissors
# if not enough information uses random from library
def getComputerMove(transition_table, currMove, prevMove):
    if not prevMove:
        return random.choice(['r', 'p', 's'])

    next_moves = transition_table[prevMove]
    if all(v == 0 for v in next_moves.values()):
        return random.choice(['r', 'p', 's'])
    predicted_player_move = max(next_moves, key=next_moves.get)

    counter_map = {'r': 'p', 'p': 's', 's': 'r'}
    return counter_map[predicted_player_move]

#looking for winning combination in dictionary if found then player won, same input tie , remaining lose
def getOutcome(playerMove, computerMove, score):
    print(f"\nYou chose {playerMove} and then AI responded with {computerMove}")
    winning_combos = {('r', 's'), ('p', 'r'), ('s', 'p')}
    if playerMove == computerMove :
        score["ties"] += 1
    elif (playerMove, computerMove) in winning_combos:
        score["wins"] += 1
        print("Lets gooo you beat his ass")
    else:
        score["losses"] += 1
        print("I mean... it happens, just try again")

#main function runs loop until players write Q or q
def rpsGame():
    score = {"wins": 0, "losses": 0, "ties": 0}
    transition_table = {
        'r': {'r': 0, 'p': 0, 's': 0},
        'p': {'r': 0, 'p': 0, 's': 0},
        's': {'r': 0, 'p': 0, 's': 0}
    }
    currMove = ""
    prevMove = ""
    computerMove = ""

    print ('Welcome to Rock, Paper, Scissors game with smart AI 3000\n')

    while True:
        print(f"{score['wins']} Wins, {score['losses']} Losses and {score['ties']} Ties")
        prevMove = currMove;
        currMove = getPlayerMove()
        
        if prevMove:
            transition_table[prevMove][currMove] += 1
        computerMove = getComputerMove(transition_table, currMove, prevMove)
        getOutcome(currMove, computerMove, score)

if __name__ == '__main__':
    rpsGame()
