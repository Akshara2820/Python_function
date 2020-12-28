def win():
    while True:
        player_choice = input('What do you pick? (rock, paper, scissors :)')
        player_choice.strip()
        moves = ['rock', 'paper', 'scissors']
        computer_choice=input('what yo want ?')
        computer_choice.strip()

        if player_choice ==computer_choice:
            print ('Draw!')
        elif  player_choice== 'rock' and computer_choice== 'scissors':
            return('you win')
        elif  player_choice== 'scissors' and computer_choice == 'rock':
            return('you lose')
        elif player_choice == 'scissors' and computer_choice == 'paper':
            return('you win')
        elif player_choice == 'paper' and computer_choice == 'rock':
            return('you win')
        elif player_choice =='rock'  and computer_choice == 'paper':
            return ('you win')
        elif player_choice=='paper' and computer_choice=='scissors':
            return ('you lose')

print(win())
new=input("if you want play again press-- Y :")
if new=="Y":
    print(win())