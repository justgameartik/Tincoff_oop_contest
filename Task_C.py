class Deck:
    def __init__(self):
        self.cards = []
        self.error = False
        
    def read_from_file(self, file_name):
        with open(file_name) as file:
            line = file.readline().strip()
            while line and not self.error:
                if line[0] == "+":
                    self.__add_card(line[1:])
                elif line[0] == "^":
                    self.__remove_upper_card()
                elif line[0] == "#":
                    self.__add_to_bottom(line[1:])
                elif line[0] == "/":
                    self.__remove_bottom_card()
                else:
                    self.error = True
                line = file.readline().strip()

    def __add_card(self, card_name):
        if Card(card_name) in self.cards:
            self.error = True
        else:
            self.cards.append(Card(card_name))
                

    def __add_to_bottom(self, card_name):
        if Card(card_name) in self.cards:
            self.error = True
        else:
            self.cards.insert(0, Card(card_name))

    def __remove_upper_card(self):
        if self.cards:
            self.cards.pop()
        else:
            self.error = True

    def __remove_bottom_card(self):
        if self.cards:
            self.cards.pop(0)
        else:
            self.error = True

    def show(self, file_name=None):
        if self.error:
            self.cards = ["ERROR"]
        if file_name:
            with open(file_name, "w") as file:
                if len(self.cards) != 0:
                    out_list = [str(card) for card in self.cards[::-1]]
                    file.write(" ".join(out_list))
                else:
                    file.write("EMPTY")
        else:
            if self.cards != []:
                print(*self.cards[::-1])
            else:
                print("EMPTY") 


class Card:
    def __init__(self, name):
        self.suit = name[0]
        self.rank = name[1]

    def __eq__(self, another):
        if isinstance(another, Card):
            return str(self) == str(another)
        elif isinstance(another, str):
            return str(self) == another
        else:
            return False

    def __str__(self):
        return self.suit + self.rank


a = Deck()
a.read_from_file('input.txt')
a.show("output.txt")
