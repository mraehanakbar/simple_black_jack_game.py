import random as rd
player_card1 = int(rd.randint(0,11))
player_card2 = int(rd.randint(0,11))
p_total_card = player_card1 + player_card2
dealer_card1 = int(rd.randint(0,11))
dealer_card2 = int(rd.randint(0,11))
d_total_card = dealer_card1 + dealer_card2
choice = str
while choice != "s" and p_total_card < 21:
    print("player card: ", p_total_card)
    print("stand or hit? ")
    choice = str(input())
    if choice == "h":
        add = int(rd.randint(0,11))
        p_total_card = p_total_card + add
    if p_total_card > 21:
        print("dealer wins with dealer card = ", d_total_card, " and player total = ", p_total_card)
    if p_total_card == 21:
        print("player wins with player card = ", p_total_card, " and dealer total = ", d_total_card)

if choice == "s":
    while d_total_card <= 16:
        d_add = rd.randint(0, 11)
        d_total_card = d_total_card + d_add

    if (p_total_card > d_total_card and d_total_card < 21) or (p_total_card == 21):
        print("player wins with player card = ",p_total_card," and dealer total = ",d_total_card)

    elif (d_total_card > p_total_card and d_total_card < 21) or (d_total_card == 21):
        print("dealer wins with dealer card = ", d_total_card, " and player total = ", p_total_card)
