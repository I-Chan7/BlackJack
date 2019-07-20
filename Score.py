# calculate score of current hand


def fetch_score(hand):
    """Return the score of a card"""
    if hand == "Jack" or hand == "Queen" or hand == "King":
        score = 10
    elif hand == "Ace":
        score = 1
    else:
        score = hand
    return score


def check_hand(hand):
    """Return the total score of the cards in the hand"""
    score = 0
    score2 = 0
    for i in range(len(hand)):
        if "Ace" in hand:
            if hand[i] == "Ace":
                score += 1
                score2 = score + 10
            else:
                score += fetch_score(hand[i])
                score2 += fetch_score(hand[i])
        else:
            score += fetch_score(hand[i])

    for i in range(len(hand)):
        print("{:^7}".format(hand[i]), end='')

    # return score1 only if score2 is 0(no Ace in hand) or over 21
    if score2 == 0 or score2 > 21:
        print("\nScore: ", score)
        return score
    # return score2 only if score2 is 21
    elif score2 == 21:
        print("\nScore: ", score)
        return score2
    # return both scores if score2 is between 1 and 21 inclusive
    else:
        print("\nScore: {} or {}".format(score, score2))
        return score2


def check_blackjack(hand):
    """Check if hand is a blackjack"""
    if ("Ace" in hand and 10 in hand) or ("Ace" in hand and "Jack" in hand) \
            or ("Ace" in hand and "Queen" in hand) or ("Ace" in hand and "King" in hand):
        return True
    else:
        return False


def compare_score(player_score, dealer_score):
    """Return the result after comparing the two hands"""
    if player_score > dealer_score:
        print("\nYou Win")
        return "Win"
    elif player_score == dealer_score:
        print("\nDraw")
        return "Draw"
    else:
        print("\nDealer Wins")
        return "Loss"
