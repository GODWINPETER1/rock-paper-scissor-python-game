import random;

def play():
    
    
    user = input("Choose the one here , (r = rock , p = paper , and s = scissors): ").lower()
    
    computer = random.choice(["r" , "p" , "s" ])
    print(computer)
    
    if user == computer:
        
        return "You have choose the same choice , so its a TIE"
    
    if is_win(user , computer):
        
        return "You have choose and the computer have choose , you have win"
    
    return "You have choose and the computer have choose , you have lost"


def is_win(player , oppenent):
    
    if (player == 'r' and oppenent == 's') or (player == 'p' and oppenent == 'r') or (player == 's' and oppenent == 'p'):
        
        return True
    
    return False

if __name__ == "__main__":
    print(play())

