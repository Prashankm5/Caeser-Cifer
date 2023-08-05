import os
import random
from art import logo

def deal_card():
    """Return a random card from dick"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list and Calculate the (sum) score of cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score,computer_score):       
    """Take user score and computer score and comparer them"""
    if user_score == computer_score:
        return "Draw 🙃"
    elif user_score==0:
        return "You Win with a Blackjack 😎"
    elif computer_score==0:
        return 'Lose, opponent has Blackjack 😱'
    elif user_score>21:
        return 'You went over. You lose 😭'
    elif computer_score>21:
        return 'Opponent went over. You win 😁'
    elif user_score>computer_score:
        return 'You win 😃'
    elif computer_score>user_score:
        return 'You lose 😤'
    


def play_game():
    print(logo)
    user_card = []
    computer_card = []
    is_game_over = False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"    Your cards : {user_card}    Your score : {user_score}")
        print(f"    Opponent's First card : {computer_card[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal = input("Type 'y' to get another card and 'n' to pass : ")
            if user_should_deal=='y':
                user_card.append(deal_card())
            else:
                is_game_over=True
    
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    
    print(f"    Your final hand : {user_card},  Your score final Score : {user_score}")
    print(f"    Opponent Final hand : {computer_card},  Opponent Final score : {computer_score}")
    print(compare(user_score,computer_score))

y='y'
while y=='y':
    os.system('cls')
    play_game()
    y=input("Do you want to play again? Type 'y' to play or any other key for exit : ")



