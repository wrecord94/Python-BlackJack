# BlackJack Project

import random


class BlackjackGame:
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.user_cards = []
        self.computer_cards = []

    def deal_card(self):
        """Returns a random card from the deck"""
        card = random.choice(self.cards)
        return card

    def calculate_score(self, hand):
        """Returns the score BlackJack is represented by a score of zero."""
        if sum(hand) == 21 and len(hand) == 2:
            print("Blackjack found.")
            return 0
        # Logic surrounding finding of an ace
        if 11 in hand and sum(hand) > 21:
            print("TEST CODE.... Changing an ace from 11 to 1..")
            hand.remove(11)
            hand.append(1)
        return sum(hand)

    def compare(self, user_total, computer_total):
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

    def game_play(self):
        for _ in range(2):
            self.user_cards.append(self.deal_card())
            self.computer_cards.append(self.deal_card())

        user_total = self.calculate_score(self.user_cards)
        computer_total = self.calculate_score(self.computer_cards)

        is_game_over = False

        if user_total == 0 or computer_total == 0 or user_total > 21:
            is_game_over = True

        game_over = False
        while is_game_over == False:
            print(f"User cards are: {self.user_cards}")
            user_total = self.calculate_score(hand=self.user_cards)
            print(f"TEST CODE.... User total is: {user_total}")
            if user_total > 21 or user_total == 0:
                is_game_over = True
            elif is_game_over == False:
                stick_or_twist = input("Would you like to withdraw a new card? Yes - type 'y or no type 'n': ")
                if stick_or_twist == 'n':
                    is_game_over = True
                elif stick_or_twist == 'y':
                    self.user_cards.append(self.deal_card())

        computer_total = self.calculate_score(hand=self.computer_cards)

        while computer_total < 17 and computer_total != 0:
            self.computer_cards.append(self.deal_card())
            computer_total = self.calculate_score(hand=self.computer_cards)

        self.compare(user_total=user_total, computer_total=computer_total)


def main():
    blackjack_game = BlackjackGame()
    blackjack_game.game_play()


if __name__ == "__main__":
    main()
