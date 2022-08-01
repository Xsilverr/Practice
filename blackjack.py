############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


# First step - player draws 2 cards and show the 2 cards
# Second step - computer draws 2 cards and show 1 card only
# Third step - ask if the player wants to draw or not
#     computer to draw another card if the total value is lesser than 17
# Fourth step - compare the total values - win, lose or draw
# Fifth step - ask if the player wants to play again?
import random

# drawing of cards
def draw_cards(deck):
    a = random.choice(deck)
    b = random.choice(deck)
    drawn_cards = [a, b]
    return drawn_cards

# Ask if player wants to draw another card
def draw_another_card(player_hand):
    want_draw = True
    player_total = sum(player_hand)
    while want_draw:
        player_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if player_choice == 'y':
            player_hand.append(random.choice(cards))
            # print(f"The new player cards are {player_cards}.")
            player_total = sum(player_hand)
            # print(f"The new player total is {player_total}.")
            if player_total > 21 and 11 in player_hand:
                player_hand[player_hand.index(11)] = 1
                player_total = sum(player_hand)
            # print(f"The newer player total is {player_total}.")
            print(f"Your new cards: {player_cards}.")
        else:
            want_draw = False

# to make the computer draw cards if the total is less than 17
def computer_draw(computer_hand):
    computer_total = sum(computer_hand)
    while computer_total <= 17:
        computer_hand.append(random.choice(cards))
        computer_total = sum(computer_hand)
        if computer_total > 21 and 11 in computer_hand:
                computer_hand[computer_hand.index(11)] = 1
                computer_total = sum(computer_hand)

# to check for the win/lose/tie condition
def condition(player_score, computer_score):
    if player_score > 21 or computer_score > player_score and computer_score < 21:
        print("You lose")
    elif computer_score > 21 or player_score > computer_score and player_score < 21:
        print("You win")
    elif player_score == computer_score:
        print("Draw")
    

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_total = 0
computer_total = 0

# To show the player cards
player_cards = draw_cards(cards)
print(f"Your cards: {player_cards}.")

# To show the computer cards, but only the second card
computer_cards = draw_cards(cards)
# computer_cards = [1,10]
# print(computer_cards)
print(f"Computer's first cards: {computer_cards[0]}.")

draw_another_card(player_hand=player_cards)
player_total = sum(player_cards)
computer_draw(computer_hand=computer_cards)
computer_total = sum(computer_cards)

print(f"Your final hand: {player_cards}")
print(f"Your total is {player_total}")
print(f"Computer's final hand: {computer_cards}")
print(f"Computer's total is {computer_total}")

condition(player_score=player_total, computer_score=computer_total)