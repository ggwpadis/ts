import random

from game_logic import CHOICES, is_valid_choice, get_winner, update_score


player_score = 0
computer_score = 0

print("================================")
print("   КАМЕНЬ, НОЖНИЦЫ, БУМАГА")
print("================================")
print("Игра состоит из 10 раундов.\n")


for round_number in range(1, 11):

    print(f"--- Раунд {round_number} из 10 ---")

    player = input(
        "Выберите: камень, ножницы или бумага: "
    ).lower()

    if not is_valid_choice(player):
        print("Ошибка! Неверный выбор.\n")
        continue

    computer = random.choice(CHOICES)

    print(f"Вы выбрали: {player}")
    print(f"Компьютер выбрал: {computer}")

    result = get_winner(player, computer)

    if result == "draw":
        print("Ничья!")
    elif result == "win":
        print("Вы победили!")
    else:
        print("Компьютер победил!")

    player_score, computer_score = update_score(
        result,
        player_score,
        computer_score
    )

    print(
        f"Счёт: Вы {player_score} : "
        f"{computer_score} Компьютер\n"
    )


print("================================")
print("          ИГРА ОКОНЧЕНА")
print("================================")

print(f"Ваш счёт: {player_score}")
print(f"Счёт компьютера: {computer_score}")

if player_score > computer_score:
    print("Итог: Вы победили!")
elif player_score < computer_score:
    print("Итог: Компьютер победил!")
else:
    print("Итог: Ничья!")