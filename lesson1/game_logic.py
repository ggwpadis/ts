CHOICES = ["камень", "ножницы", "бумага"]


def is_valid_choice(choice):
    return choice in CHOICES


def get_winner(player, computer):
    if player == computer:
        return "draw"

    if (
        (player == "камень" and computer == "ножницы")
        or
        (player == "ножницы" and computer == "бумага")
        or
        (player == "бумага" and computer == "камень")
    ):
        return "win"

    return "lose"


def update_score(result, player_score, computer_score):
    if result == "win":
        player_score += 1
    elif result == "lose":
        computer_score += 1

    return player_score, computer_score