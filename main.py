aliens = ['thanos', 'superman', 'batman', 'hulk']
score = 0

def display_aliens(aliens):
    print("Available aliens to shoot:")
    for index, alien in enumerate(aliens):
        print(f"{index}: {alien}")

def warGame(selected_alien):
    global score
    print(f'{selected_alien} was killed')
    score += 1
    return 'aliens was shot'

while True:
    display_aliens(aliens)
    try:
        player_choice = int(input("Choose an alien to shoot (enter the number): "))
        if player_choice < 0 or player_choice >= len(aliens):
            print("Invalid choice. Please try again.")
            continue
        removed_alien = aliens.pop(player_choice)
        outcome = warGame(removed_alien)
        print(f'The final outcome was {outcome}. Your score is now {score}.')
    except ValueError:
        print("Please enter a valid number.")
    
    gamerInput = input("Do you want to continue? y/n: ")
    if gamerInput.lower() != 'y':
        print('Game Over')
        print('You are dead!!!')
        break
