one = 9
two = 9
three = 9
player = 1

print("Welcome to Nim! In this game, you and a friend take rocks from three different piles. The player who takes the "
      "last rock loses!")

# Create my while loop and write code to display the amount of stones in each pile.
while (one != 0 or two != 0 or three != 0):
    print("\nPile 1: %d \nPile 2: %d \nPile 3: %d" % (one, two, three,))
    print("\nPlayer %d:" % player)

    # Now I display which player is going and ask the user their next move.
    pile = int(input("From which pile would you like to take from?"))
    take = int(input("How many stones would you like to take?"))

    if pile == 1:
        one -= take
    elif pile == 2:
        two -= take
    elif pile == 3:
        three -= take

    # Lines of code to constantly switch players
    if player == 1:
        player = 2
    elif player == 2:
        player = 1

# Now the program recognizes which player took and the last stone and then displays the corresponding message.
if player != 1 and one == 0 and two == 0 and three == 0:
    print("\nPlayer 1 pulled the last stone! Player 2 wins!")
else:
    print("\nPlayer 2 pulled the last stone! Player 1 wins!")

