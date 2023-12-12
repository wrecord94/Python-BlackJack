# BlackJack Project

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card


def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        print("Blackjack found.")
        return 0
    if 11 in hand and sum(hand) > 21:
        print("TEST CODE.... Changing an ace from 11 to 1..")
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(user_total, computer_total):
    print(f"User score is: {user_total}")
    print(f"Computer score is: {computer_total}")
    if user_total == computer_total:
        print("It's a draw!")
    elif user_total == 0:
        print("User wins!")
    elif user_total > 21 or computer_total == 0:
        print("Computer wins!")
    elif computer_total > 21:
        print("User wins!")
    elif user_total > computer_total:
        print("User wins!")
    elif user_total < computer_total:
        print("Computer wins!")


user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_total = calculate_score(user_cards)
computer_total = calculate_score(computer_cards)
is_game_over = False

if user_total == 0 or computer_total == 0 or user_total > 21:
    is_game_over = True

game_over = False
while is_game_over == False:
    print(f"User cards are: {user_cards}")
    user_total = calculate_score(hand=user_cards)
    print(f"TEST CODE.... User total is: {user_total}")
    if user_total > 21 or user_total == 0:
        is_game_over = True
    elif is_game_over == False:
        stick_or_twist = input("Would you like to withdraw a new card? Yes - type 'y or no type 'n': ")
        if stick_or_twist == 'n':
            is_game_over = True
        elif stick_or_twist == 'y':
            user_cards.append(deal_card())

computer_total = calculate_score(hand=computer_cards)

while computer_total < 17 and computer_total != 0:
    computer_cards.append(deal_card())
    computer_total = calculate_score(hand=computer_cards)

compare(user_total=user_total, computer_total=computer_total)