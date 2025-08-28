fpname = input("Enter the name of the 1st player : ").capitalize()
fphp = int(input("And his number of HP : "))
spname = input("Enter the name of the 2nd player : ").capitalize()
sphp = int(input("And his number of HP : "))
initmsg = "+ " + str(fpname) + " (" + str(fphp) + " HP) faces " + str(spname) + " (" + str(sphp) + " HP) +"
print("\n\n" , "+" * len(initmsg), "\n", initmsg, "\n", "+" * len(initmsg))