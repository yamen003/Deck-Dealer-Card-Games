import random
class card:
    suit=["clubs","diamonds","hearts","spades"]
    number=[1,2,3,4,5,6,7,8,9,10,11,12];
    color=["red","black"]
#---------RANDOM DEALER--------------------
def randomcarddealer():
    random1=random.randint(0,len(card.suit)-1)
    randomsuit=card.suit[random1]
    random2=random.randint(0,len(card.number)-1)
    randomnumber=card.number[random2]
    random3=random.randint(0,len(card.color)-1)
    randomcolor=card.number[random3]
    if randomnumber==11:
        randomnumber="J"
    elif randomnumber==12:
        randomnumber="Q"
    elif randomnumber==13:
        randomnumber="K"
    elif randomnumber==1:
        randomnumber="ACE"
    randomcard=str(randomnumber)+" of "+randomsuit
    if ("hearts" in randomcard) or ("diamonds" in randomcard):
        randomcard=str(randomnumber)+" of "+randomsuit+ " RED "
    else:
        randomcard=str(randomnumber)+" of "+randomsuit+ " BLACK "
    return randomcard
#-----------------------------
def saharaAce():
    global payout
    cardrawed=randomcarddealer()
    #print(cardrawed)
    if "ACE" in cardrawed:
        #print(" Congrats YOU won 10 Tunisian Dinars");
        payout += 50    
    else :
        #print("You lost , Try Again?")
        payout=0
#---------------------------------------
def TunisianTwins():
    global payout
    cardrawed1=randomcarddealer()
    cardrawed2=randomcarddealer()
    #print(cardrawed1 + " AND " +cardrawed2 )
    if (cardrawed1==cardrawed2):
        #print("Congrats u won 50")
        payout += 50
    else:
        #print("U LOST")
        payout =0
#-----------------------------
def MedinaBiggie():
    global payout
    rankings = {
    'numbers': {'AC':1,'2 ': 2,'3 ': 3,'4 ': 4,'5 ': 5,'6 ': 6,'7 ': 7,'8 ': 8,'9 ': 9,'10': 10,'J ': 11,'Q ': 12,'K ': 13,}}
    cardrawed1=randomcarddealer()
    cardrawed2=randomcarddealer()
    #print(cardrawed1 + " AND " +cardrawed2 )
    if (rankings['numbers'][cardrawed2[:2]] >rankings['numbers'][cardrawed1[:2]]):
        #print("U WON 2 DINARS");
        payout+=2
    else:
        #print("U lost")
        payout+=0
#-----------------------------
def DesertHearts():
    global payout
    rankings = {
    'numbers': {'AC':1,'2 ': 2,'3 ': 3,'4 ': 4,'5 ': 5,'6 ': 6,'7 ': 7,'8 ': 8,'9 ': 9,'10': 10,'J ': 11,'Q ': 12,'K ': 13,}}
    card1=randomcarddealer()
    card2=randomcarddealer()
    card3=randomcarddealer()
    #print(card1 + " AND " +card2 + " AND " + card3)
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
        #print("Congrats u won   "+str(sumValue))
        payout+=sumValue
    else:
        #print("U LOST")
        payout+=0
#-----------------------------
def OasisRunny():
    global payout
    rankings = {
    'numbers': {'AC':1,'2 ': 2,'3 ': 3,'4 ': 4,'5 ': 5,'6 ': 6,'7 ': 7,'8 ': 8,'9 ': 9,'10': 10,'J ': 11,'Q ': 12,'K ': 13,}}
    setoffiver=[card]*5
    onlynums=[int]*5
    for i in range(0,5):
        setoffiver[i]=randomcarddealer()
        onlynums[i]=rankings['numbers'][setoffiver[i][:2]]
    #print(onlynums)
    for i in range(len(onlynums) - 2):
        subset = onlynums[i:i+3]
        if all(subset[j] == subset[j-1] + 1 for j in range(1, 3)):
            payout+=5
            #print("You Won")
            return True
    #print("You Lost")
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
        setof4[i]=randomcarddealer()
        onlynums[i]=rankings['numbers'][setof4[i][:2]]
    for i in range(0,len(onlynums)):
        sum=sum+onlynums[i]
    if sum<=12:
        #print("U Won")
        payout+=10
    else:
        #print("U lost")
        payout+=0
#-----------------------------
#payout=0
#saharaAce()
#TunisianTwins()
#MedinaBiggie()
#DesertHearts()
#OasisRunny()
#TwelveAngryMen()
#print(payout)
#----------------------------
def MonteCarlo(game):
    total = 10
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
