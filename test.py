GOAL = 100


def main():
    is_always_roll(always_roll_5)


def is_always_roll(strategy, goal=GOAL):
    num_rolls_list = []

    def strategy(num_rolls, score, opponent_score):
        while score < goal and opponent_score < goal:
            num_rolls_list.append(num_rolls)
        test_digit = num_rolls_list[0]
        for num in num_rolls_list:
            if test_digit != num:
                return False

    return strategy

def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5

main()
