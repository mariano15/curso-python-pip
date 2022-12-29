import random

name_user = input("nombre: ")

def choose_options():
  options = ["piedra", "papel", "tijera"]
  user_options = input("elije piedra , papel o tijera :")
  user_options = user_options.lower()

  if not user_options in options:
    print("**NO ES VALIDO**")
    return None, None

  computer_options = random.choice(options)

  print("elegiste ", user_options)
  print("pc elige", computer_options)
  return user_options, computer_options

def check_rules(user_options, computer_options, user_wins, computer_wins):
  if user_options == computer_options :
    print("**EMPATE**")
  elif user_options == "piedra":
    if computer_options == "tijera":
      print("**piedra gana a tijera**")
      print("**GANASTE**")
      user_wins += 1 

    else:
      print("**papel gana a piedra**")
      print("**PC GANA**")
      computer_wins += 1

  elif user_options == "papel":
    if computer_options == "piedra":
      print("**papel gana a piedra**")
      print("**GANASTE**")
      user_wins += 1

    else:
      print("**tijera gana a papel**")
      print("**PC GANA**")
      computer_wins += 1

  elif user_options == "tijera":
      if computer_options == "papel":
        print("**tijera gana a papel**")
        print("**GANASTE**")
        user_wins += 1
    
      else:
        print("**piedra gana a tijera**")
        print("**PC GANA**")
        computer_wins += 1
  return user_wins, computer_wins

def check_winer(user_wins, computer_wins):

  if user_wins == 2:
    print("**GANASTE LA PARTIDA**")
    exit()
    
    
       
  if computer_wins == 2:
    print("**PC GANÓ LA PARTIDA**")
    exit()
    
def run_game():
  round = 1
  user_wins = 0
  computer_wins = 0
  while True:
    print("*"*7)
    print("ROUND", round)
    print("*"*7)
    
    print(name_user, user_wins)
    print("pc", computer_wins)
    round += 1
  
    user_options, computer_options = choose_options()
    user_wins, computer_wins = check_rules(user_options, computer_options, user_wins, computer_wins)
    check_winer(user_wins, computer_wins)
    

  
run_game()    
    

  

 