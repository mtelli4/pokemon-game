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
fp_attack_damage = int(input(fpname + " how much damage do you deal to " + spname + " ? "))
sphp -= fp_attack_damage
fp_attack_message = fpname + " attacks " + spname + " who loses " + str(fp_attack_damage) + " HP"
fp_attack_message_2 = spname + " has now " + str(sphp) + " HP"
width = max(len(fp_attack_message), len(fp_attack_message_2))
print()
print("+"*(width+4))
print("+", fp_attack_message + " " * (width - len(fp_attack_message)), "+")
print("+", fp_attack_message_2 + " " * (width - len(fp_attack_message_2)), "+")
print("+" * (width+4))

####################################################
#              Second player's attack              #
####################################################

print()
sp_attack_damage = int(input(spname + " how much damage do you deal to " + fpname + " ? "))
fphp -= sp_attack_damage
sp_attack_message = spname + " attacks " + fpname + " who loses " + str(sp_attack_damage) + " HP"
sp_attack_message_2 = fpname + " has now " + str(fphp) + " HP"
width = max(len(sp_attack_message), len(sp_attack_message_2))
print()
print("+"*(width+4))
print("+", sp_attack_message + " " * (width - len(sp_attack_message)), "+")
print("+", sp_attack_message_2 + " " * (width - len(sp_attack_message_2)), "+")
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
print()
print("+" * (w_summary + 4))
print("+ " + summary_msg + (" " * (w_summary - len(summary_msg))) + " +")
print("+ " + fphp_msg + (" " * (w_summary - len(fphp_msg))) + " +")
print("+ " + sphp_msg + (" " * (w_summary - len(sphp_msg))) + " +")
print("+" * (w_summary + 4))
