import random

class card:
    def __init__(self, rank, suit):
        symbols = {
            "spade": chr(9824),
            "club": chr(9827),
            "heart": chr(9829),
            "diamond": chr(9830)
        }

        self.rank = rank
        self.suit = suit
        self.symbol = symbols[suit.lower()]
        self.status = None

    def say_name(self):
        rank_name = self.rank
        rank_name_adjust = {"X": "Ten", "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}
        if rank_name in rank_name_adjust:
            rank_name = rank_name_adjust[rank_name]
        print(rank_name + " of " + self.suit.title() + "s (" + self.rank + self.symbol + ")")

class deck:
    def __init__(self, number_of_cards=52):
        suits = ["spade","club","heart","diamond"]
        ranks = ["2","3","4","5","6","7","8","9","X","J","Q","K","A"]

        self.cards = {}
        if number_of_cards == 52:
            card_num = 1
            for suit in suits:
                for rank in ranks:
                    self.cards[card_num] = card(rank, suit)
                    self.cards[card_num].status = "in_deck"
                    card_num += 1

        self.top_card = 1

    def read_deck(self):
        for card in self.cards:
            self.cards[card].say_name()

    def shuffle(self):
        number_of_cards = len(self.cards)
        for x in range(number_of_cards):
            current_card_num = x + 1
            # pick a random card from the rest of the deck
            swap_card_num = random.randint(current_card_num, number_of_cards)
            # hold the random card
            swap_card = self.cards[swap_card_num]
            # swap the current card with the held card
            self.cards[swap_card_num] = self.cards[current_card_num]
            self.cards[current_card_num] = swap_card

    def read_top_cards(self, number_of_cards=1):
        for card in range(number_of_cards):
            card_num = self.top_card + card
            if card_num > len(self.cards):
                print("[End of deck.]")
                break
            self.cards[card_num].say_name()

    def deal_card_to(self, status):
        if self.top_card == len(self.cards):
            print("No more cards.")
            return None
        self.cards[self.top_card].status = status
        self.top_card += 1


