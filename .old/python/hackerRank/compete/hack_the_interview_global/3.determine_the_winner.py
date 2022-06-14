"""https://www.hackerrank.com/contests/hack-the-interview-global/challenges/playing-cards-1-1"""


def get_round_result(winning_suit, suit1, number1, suit2, number2):
    playerA = False
    playerB = False
    if suit1 == winning_suit:
        playerA = True
    if suit2 == winning_suit:
        playerB = True
    if playerA and playerB or ((not playerA) and (not playerB)) :
        if number1 > number2:
            playerA = True
            playerB = False
        elif number2 > number1:
            playerB = True
            playerA = False
        else:
            playerA = playerB =  False
            
    if playerA:
        return("Player 1 wins")
    elif playerB:
        return("Player 2 wins")
    else:
        return("Draw")
        
