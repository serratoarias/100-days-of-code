import random
from art import black

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has a blackjack"
    elif u_score == 0:
        return "User wins"
    elif u_score > 21:
        return "You went over, you lose"
    elif c_score > 21:
        return "Opponent went over, you win"
    elif u_score > c_score:
        return "User wins"
    else:
        return "You lose"

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are: {user_cards}, and your current score: {user_score}.")
        print(f"Computer's first card is: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to get another card? Type 'y' or 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards}, and the final score is: {user_score}")
    print(f"Computer's final hand is: {computer_cards}, and the final score is: {computer_score}")
    compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print(black)
    play_game()
