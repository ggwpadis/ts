from game_logic import is_valid_choice, get_winner, update_score


def test_valid_choice():
    assert is_valid_choice("камень") is True
    assert is_valid_choice("ножницы") is True
    assert is_valid_choice("бумага") is True


def test_rock_beats_scissors():
    assert get_winner("камень", "ножницы") == "win"


def test_scissors_beats_paper():
    assert get_winner("ножницы", "бумага") == "win"


def test_paper_beats_rock():
    assert get_winner("бумага", "камень") == "win"


def test_same_choice_is_draw():
    assert get_winner("камень", "камень") == "draw"


def test_player_loses():
    assert get_winner("камень", "бумага") == "lose"


def test_invalid_choice():
    assert is_valid_choice("машина") is False


def test_empty_choice():
    assert is_valid_choice("") is False


def test_number_as_choice():
    assert is_valid_choice("123") is False


def test_update_score_win():
    player, computer = update_score("win", 0, 0)
    assert player == 1
    assert computer == 0


def test_update_score_lose():
    player, computer = update_score("lose", 0, 0)
    assert player == 0
    assert computer == 1


def test_update_score_draw():
    player, computer = update_score("draw", 2, 3)
    assert player == 2
    assert computer == 3