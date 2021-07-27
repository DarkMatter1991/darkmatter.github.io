
import random
from enum import IntEnum

class Action(IntEnum):
    Daş = 0
    Kağız = 1
    Qayçı = 2
    Lizard = 3
    Spock = 4

victories = {
    Action.Qayçı: [Action.Lizard, Action.Kağız],
    Action.Kağız: [Action.Spock, Action.Daş],
    Action.Daş: [Action.Lizard, Action.Qayçı],
    Action.Lizard: [Action.Spock, Action.Kağız],
    Action.Spock: [Action.Qayçı, Action.Daş]
}

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Seçim et ({choices_str}): "))
    action = Action(selection)
    return action
def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action
def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Her iki oyunçunun seçimi {user_action.name}. Berabere!")
    elif user_action == Action.Daş:
        if computer_action == Action.Qayçı:
            print("Daş qayçını sındırdı! Qalib geldin!")
        else:
            print("Kağız daşı meğlub etdi! Sen meğlub oldun!.")
    elif user_action == Action.Kağız:
        if computer_action == Action.Daş:
            print("Kağız daşı meğlub etdi! Qalib geldin!")
        else:
            print("Qayçı kağızı meğlub etdi! Sen meğlub oldun.")
    elif user_action == Action.Qayçı:
        if computer_action == Action.Kağız:
            print("Qayçı kağızı meğlub etdi! Qalib geldin!")
        else:
            print("Daş qayçını sındırdı! Sen meğlub oldun.")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Yalnış seçim bu aralıqda seçim et {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Yeni oyun? (b/x): ")
    if play_again.lower() != "b":
        break
