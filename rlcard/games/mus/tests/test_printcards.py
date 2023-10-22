from rlcard.games.mus.card import MusCard as Card

def print_spanish_cards():

    try:
        Card.print_cards(["o-4", "b-7"])
    except:
        assert False, "Not possible to print Unicode"

if __name__ == '__main__':
    print_spanish_cards()