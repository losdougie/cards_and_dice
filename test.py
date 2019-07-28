import dice
import cards

def test_dice():
    d1 = dice.die()
    d2 = dice.die(number_of_sides=20)
    d3 = dice.die(values=["a","b","c","d","e","f"])
    for x in range(100):
        d2.roll()
    d3.roll()
    print("\n".join(["d1: " + d1.roll(),"d2: " + d2.roll(),"d3: " + d3.roll()]))
    print("stats:", d1.stats, "\n", d2.stats, "\n", d3.stats,"\n")

def test_cards():
    deck = cards.deck()
    deck.shuffle()
    deck.read_deck()
    print("Dealing ... ")
    deck.deal_card_to("player1")
    deck.deal_card_to("player2")
    print("Done Dealing ...")
    deck.read_top_cards(5)

def main():
    # test_dice()
    test_cards()


if __name__ == "__main__":
    main()