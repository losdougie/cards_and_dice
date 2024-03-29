import dice
import cards
import os

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

def read_folder(folder_name):
    list_of_files = []
    for file in os.listdir(folder_name):
        file = os.path.join(folder_name, file)
        if os.path.isfile(file):
            filename = os.path.splitext(os.path.basename(file))[0]
            list_of_files.append(filename)
    return list_of_files

def walk_folder(folder_name):
    for items in os.walk(folder_name):
        parent_folder = items[0]
        folders = items[1]
        files = items[2]
        for file in files:
            filename = os.path.splitext(file)[0]
            print(filename)

def main():
    # test_dice()
    # test_cards()
    print(read_folder("./test_folder"))
    walk_folder("./test_folder")

if __name__ == "__main__":
    main()