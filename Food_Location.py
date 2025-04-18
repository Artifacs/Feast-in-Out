#HELLO THERE WELCOME TO YOUR FOOD HAVEN! Looking For good places to eat out? here is options depending on your location


location = input("Where are you?(CAVITE OR MANILA): ")
if location == "CAVITE":
    options = input("BREAKFAST/LUNCH/DINNER?: ")
    if options == "BREAKFAST":
        food = input("what do you want?(COFFEE OR PANCAKES): ")
        if food == "COFFEE":
            print("COFFEE OPTION NEAR CAVITE:\nSTARBUCKS\nSMDC_COFFEE")
        elif food == "PANCAKES":
         print("PANCAKE BREAKFAST OPTIONS IN CAVITE:\nPANCAKE HOUSE(La salle)\nPANCAKE HOUSE(Vermosa)")
    elif options == "LUNCH":
        food = input("what food do you want?(CHICKEN OR PORK): ")
        if food == "CHICKEN":
            print("WINGS OR CHICKEN OPTIONS:\nDOC WINGS\nTOSS WINGS\n3 JOINS")
        elif food == "PORK":
         print("PORK OR SAMG OPTIONS:\nSAMGYUPSALAMAT\nYAKIMIX")
    elif options == "DINNER":
        food = input("what food do you want?(CHICKEN OR PORK): ")
        if food == "CHICKEN":
            print("WINGS OR CHICKEN OPTIONS:\nDOC WINGS\nTOSS WINGS\n3 JOINS")
        elif food == "PORK":
         print("PORK OR SAMG OPTIONS:\nSAMGYUPSALAMAT\nYAKIMIX")
elif location == "MANILA":
    options == input("BREAK FAST/LUNCH/DINNER?")
    food = input("what food do you want?(CHICKEN OR PORK): ")
    if food == "CHICKEN":
        print("WINGS OR CHICKEN OPTIONS:\nDOC WINGS\nTOSS WINGS\n3 JOINS")
    elif food == "PORK":
         print("PORK OR SAMG OPTIONS:\nSAMGYUPSALAMAT\nYAKIMIX")