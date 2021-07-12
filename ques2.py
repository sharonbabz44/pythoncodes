Weight=int(input("Enter your weight"))
choose= input("(L)bs or (K)g")
if choose.upper()=="L":       
    converted=weight*0.45
    print(f"You are {converted} kilos")
else:
    converted=weight/0.45
    print(f"You are {converted} pounds")
