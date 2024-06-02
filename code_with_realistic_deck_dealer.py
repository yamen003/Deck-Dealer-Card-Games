import random

class card:
    suits = ["clubs", "diamonds", "hearts", "spades"]
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 
    colors = ["red", "black"]

class Deck:
    def __init__(self):
        self.cards = [(number, suit) for number in card.numbers for suit in card.suits]

    def draw_card(self):
        if not self.cards:
            raise ValueError("The deck is empty.")
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
def randomcarddealer(deck):
    number, suit = deck.draw_card()
    color = "red" if suit in ["hearts", "diamonds"] else "black"
    
    if number == 11:
        number = "J"
    elif number == 12:
        number = "Q"
    elif number == 13:
        number = "K"
    elif number == 14:
        number = "ACE"

    return f"{number} of {suit} {color}"

#-----------------------------
def saharaAce():
    global payout
    cardrawed=randomcarddealer(deck)
    print(cardrawed)
    if "ACE" in cardrawed:
        print(" Congrats YOU won 10 Tunisian Dinars");
        payout =+ 50    
    else :
        print("You lost , Try Again?")
#---------------------------------------
def TunisianTwins():
    global payout
    cardrawed1=randomcarddealer(deck)
    cardrawed2=randomcarddealer(deck)
    print(cardrawed1 + " AND " +cardrawed2 )
    if (cardrawed1==cardrawed2):
        print("Congrats u won 50")
        payout =+ 50
    else:
        print("U LOST")
#-----------------------------
def MedinaBiggie():
    global payout
    rankings = {
    'numbers': {'AC':1,'2 ': 2,'3 ': 3,'4 ': 4,'5 ': 5,'6 ': 6,'7 ': 7,'8 ': 8,'9 ': 9,'10': 10,'J ': 11,'Q ': 12,'K ': 13,}}
    cardrawed1=randomcarddealer(deck)
    cardrawed2=randomcarddealer(deck)
    print(cardrawed1 + " AND " +cardrawed2 )
    if (rankings['numbers'][cardrawed2[:2]] >rankings['numbers'][cardrawed1[:2]]):
        print("U WON 2 DINARS");
        payout=+2
    else:
        print("U lost")
#-----------------------------
def DesertHearts():
    global payout
    rankings = {
    'numbers': {'AC':1,'2 ': 2,'3 ': 3,'4 ': 4,'5 ': 5,'6 ': 6,'7 ': 7,'8 ': 8,'9 ': 9,'10': 10,'J ': 11,'Q ': 12,'K ': 13,}}
    card1=randomcarddealer(deck)
    card2=randomcarddealer(deck)
    card3=randomcarddealer(deck)
    print(card1 + " AND " +card2 + " AND " + card3)
    counter=0
    valueCard1=0
    valueCard2=0
    valueCard3=0
    if "hearts" in card1:
        counter=counter+1
        valueCard1=+rankings['numbers'][card1[:2]]
    if "hearts" in card2:
        counter=counter+1
        valueCard2=+rankings['numbers'][card2[:2]]
    if "hearts" in card3:
        counter=counter+1
        valueCard3=+rankings['numbers'][card3[:2]]
    if counter>=1:
        sumValue=valueCard1+valueCard2+valueCard3
        print("Congrats u won   "+str(sumValue))
        payout+=sumValue
    else:
        print("U LOST")
#-----------------------------
def OasisRunny():
    global payout
    rankings = {
    'numbers': {'AC':1,'2 ': 2,'3 ': 3,'4 ': 4,'5 ': 5,'6 ': 6,'7 ': 7,'8 ': 8,'9 ': 9,'10': 10,'J ': 11,'Q ': 12,'K ': 13,}}
    setoffiver=[card]*5
    onlynums=[int]*5
    for i in range(0,5):
        setoffiver[i]=randomcarddealer(deck)
        onlynums[i]=rankings['numbers'][setoffiver[i][:2]]
    print(onlynums)
    for i in range(len(onlynums) - 2):
        subset = onlynums[i:i+3]
        if all(subset[j] == subset[j-1] + 1 for j in range(1, 3)):
            payout=+5
            print("You Won")
            return True
    print("You Lost")
    return False
#-----------------------------
def TwelveAngryMen():
    global payout
    rankings = {
    'numbers': {'AC':1,'2 ': 2,'3 ': 3,'4 ': 4,'5 ': 5,'6 ': 6,'7 ': 7,'8 ': 8,'9 ': 9,'10': 10,'J ': 11,'Q ': 12,'K ': 13,}}
    setof4=[card]*3
    onlynums=[int]*3
    sum=0
    for i in range(0,3):
        setof4[i]=randomcarddealer(deck)
        onlynums[i]=rankings['numbers'][setof4[i][:2]]
    for i in range(0,len(onlynums)):
        sum=sum+onlynums[i]
    if sum<=12:
        print("U Won")
        payout+=10
    else:
        print("U lost")
#-----------------------------
deck = Deck()
for _ in range(5):
    print(randomcarddealer(deck))
#---------------------------------
def MonteCarlo(game):
    total = 2
    totalp = 0
    for _ in range(total):
        global payout
        payout = 0
        game()
        totalp += payout

    average_payout = totalp / total
    print(f"Average Payout for {game.__name__}: {average_payout}")

MonteCarlo(saharaAce)
MonteCarlo(TunisianTwins)
MonteCarlo(MedinaBiggie)
MonteCarlo(DesertHearts)
MonteCarlo(OasisRunny)
MonteCarlo(TwelveAngryMen)