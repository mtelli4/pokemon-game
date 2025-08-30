####################################################
#                  INITIALIZATION                  #
####################################################

fpname = input("Enter the name of the 1st player : ").capitalize()
fphp = int(input("And his number of HP : "))
spname = input("Enter the name of the 2nd player : ").capitalize()
sphp = int(input("And his number of HP : "))
initmsg = "+ " + str(fpname) + " (" + str(fphp) + " HP) faces " + str(spname) + " (" + str(sphp) + " HP) +"
print("\n\n" , "+" * len(initmsg), "\n", initmsg, "\n", "+" * len(initmsg))

####################################################
#              First player's attack               #
####################################################

print()
attack = input(fpname + " which attack would you like to use ?\n1. Charge (-20 PV)\n2. Tonnerre (-50 PV)\n> ")
if attack == "1" or attack == "Charge":
  attack_damage = 20 
elif attack == "2" or attack == "Tonnerre":
  attack_damage = 50
else:
  print("Invalid value")
  attack_damage = 0
sphp -= attack_damage
attack_message = fpname + " attacks " + spname + " who loses " + str(attack_damage) + " HP"
attack_message_2 = spname + " has now " + str(sphp) + " HP"
width = max(len(attack_message), len(attack_message_2))
print()
print("+"*(width+4))
print("+", attack_message + " " * (width - len(attack_message)), "+")
print("+", attack_message_2 + " " * (width - len(attack_message_2)), "+")
print("+" * (width+4))

####################################################
#              Second player's attack              #
####################################################

print()
attack = input(spname + " which attack would you like to use ?\n1. Charge (-20 PV)\n2. Tonnerre (-50 PV)\n> ")
if attack == "1" or attack == "Charge":
  attack_damage = 20 
elif attack == "2" or attack == "Tonnerre":
  attack_damage = 50
else:
  print("Invalid value")
  attack_damage = 0
fphp -= attack_damage
attack_message = spname + " attacks " + fpname + " who loses " + str(attack_damage) + " HP"
attack_message_2 = fpname + " has now " + str(fphp) + " HP"
width = max(len(attack_message), len(attack_message_2))
print()
print("+"*(width+4))
print("+", attack_message + " " * (width - len(attack_message)), "+")
print("+", attack_message_2 + " " * (width - len(attack_message_2)), "+")
print("+" * (width+4))
print()

####################################################
#                   GAME SUMMARY                   #
####################################################

summary_msg = "Game's summary :"
fphp_msg = fpname + " has " + str(fphp) + " HP"
sphp_msg = spname + " has " + str(sphp) + " HP"
w_summary = max(len(fphp_msg), len(sphp_msg))
w_summary = max(w_summary, len(summary_msg))
if fphp == sphp : result = "Draw"
else:
  if fphp > sphp :
    winner = fpname
  elif fphp < sphp :
    winner = spname
  result = winner + " win the fight"

w_summary = max(w_summary, len(result))
print()
print("+" * (w_summary + 4))
print("+ " + summary_msg + (" " * (w_summary - len(summary_msg))) + " +")
print("+ " + fphp_msg + (" " * (w_summary - len(fphp_msg))) + " +")
print("+ " + sphp_msg + (" " * (w_summary - len(sphp_msg))) + " +")
print("+ " + result + (" " * (w_summary - len(result))) + " +")
print("+" * (w_summary + 4))

