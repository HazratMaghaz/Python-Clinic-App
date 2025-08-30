print("Welcome to Maazo Clinic \n\n"
      "How may we help you, dear?\n"
      "1. Check Body Mass Index (BMI)\n"
      "2. Baby Blood Group Identification\n")

def BabyBloodGroupIdentifier():
    print("Welcome to Baby Blood Group Identifier \n")
    print('''
                                                            
                                                                                                                                                                                                                                                                                            
 mmmmm         #                    mmmmm  ""#                      #         mmmmm      #           m      "      m""    "                 
 #    #  mmm   #mmm   m   m         #    #   #     mmm    mmm    mmm#           #     mmm#   mmm   mm#mm  mmm    mm#mm  mmm     mmm    m mm 
 #mmmm" "   #  #" "#  "m m"         #mmmm"   #    #" "#  #" "#  #" "#           #    #" "#  #"  #    #      #      #      #    #"  #   #"  "
 #    # m"""#  #   #   #m#          #    #   #    #   #  #   #  #   #           #    #   #  #""""    #      #      #      #    #""""   #    
 #mmmm" "mm"#  ##m#"   "#           #mmmm"   "mm  "#m#"  "#m#"  "#m##         mm#mm  "#m##  "#mm"    "mm  mm#mm    #    mm#mm  "#mm"   #    
                       m"                                                                                                                   
                      ""                                                                                                                    
                                                  
                                                                                                                                                                                                                                                                                                   
                                                                                                                     

        
        ''')

    print("Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-\n")

    father = input("Enter Baby's Father Blood group: ").upper()
    mother = input("Enter Baby's Mother Blood group: ").upper()

    valid_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    if father not in valid_groups or mother not in valid_groups:
        print("Please  Try again by entering  valid values as directed above")
        return 

    # ---- Step 1: Separate ABO and Rh ----
    if father.endswith("+"):
        father_abo = father.replace("+", "")
        father_rh = "+"
    else:
        father_abo = father.replace("-", "")
        father_rh = "-"

    if mother.endswith("+"):
        mother_abo = mother.replace("+", "")
        mother_rh = "+"
    else:
        mother_abo = mother.replace("-", "")
        mother_rh = "-"

    # ---- Step 2: Possible ABO groups ----
    if (father_abo == "A" and mother_abo == "A"):
        possible_abo = ["A", "O"]
    elif (father_abo == "A" and mother_abo == "B") or (father_abo == "B" and mother_abo == "A"):
        possible_abo = ["A", "B", "AB", "O"]
    elif (father_abo == "A" and mother_abo == "AB") or (father_abo == "AB" and mother_abo == "A"):
        possible_abo = ["A", "B", "AB"]
    elif (father_abo == "A" and mother_abo == "O") or (father_abo == "O" and mother_abo == "A"):
        possible_abo = ["A", "O"]
    elif (father_abo == "B" and mother_abo == "B"):
        possible_abo = ["B", "O"]
    elif (father_abo == "B" and mother_abo == "AB") or (father_abo == "AB" and mother_abo == "B"):
        possible_abo = ["A", "B", "AB"]
    elif (father_abo == "B" and mother_abo == "O") or (father_abo == "O" and mother_abo == "B"):
        possible_abo = ["B", "O"]
    elif (father_abo == "AB" and mother_abo == "AB"):
        possible_abo = ["A", "B", "AB"]
    elif (father_abo == "AB" and mother_abo == "O") or (father_abo == "O" and mother_abo == "AB"):
        possible_abo = ["A", "B"]
    else:  # O + O
        possible_abo = ["O"]

    # ---- Step 3: Possible Rh ----
    if father_rh == "-" and mother_rh == "-":
        possible_rh = ["-"]
    else:
        possible_rh = ["+", "-"]

    # ---- Step 4: Combine with simple probabilities ----
    print("\nPossible baby blood groups (with rough chances):")

    # Split percentage equally
    total_combinations = len(possible_abo) * len(possible_rh)
    chance = round(100 / total_combinations, 2)

    for abo in possible_abo:
        for rh in possible_rh:
            print(f"{abo}{rh} : {chance}% chance")





def BodyMassIndex():
    print('''

                                                                                                                                                        
 mmmmmm    mmm  mmm   mmmmmm                mmmm             mmmm                          mmmm                                             
 ##""""##  ###  ###   ""##""              ##""""#            ""##                          ""##                  ##                         
 ##    ##  ########     ##               ##"        m#####m    ##       m#####m  ##    ##    ##       m#####m  #######    m####m    ##m#### 
 #######   ## ## ##     ##               ##         " mmm##    ##      ##"    "  ##    ##    ##       " mmm##    ##      ##"  "##   ##"     
 ##    ##  ## "" ##     ##               ##m       m##"""##    ##      ##        ##    ##    ##      m##"""##    ##      ##    ##   ##      
 ##mmmm##  ##    ##   mm##mm              ##mmmm#  ##mmm###    ##mmm   "##mmmm#  ##mmm###    ##mmm   ##mmm###    ##mmm   "##mm##"   ##      
 """""""   ""    ""   """"""                """"    """" ""     """"     """""    """" ""     """"    """" ""     """"     """"     ""      
         ''')


    print("Welcome to Body Mass Index (BMI) Calculator \n")

    choice = input("How would you like to enter your height?\n"
                   "1. Meters\n"
                   "2. Inches\n"
                   "3. Feet & Inches\n"
                   "Choose (1/2/3): ").strip()

    # weight = float(input("Please enter your weight in Kg: "))

       # Keep asking until user gives a valid number
    while True:
        weight_input = input("Please enter your weight in Kg: ").strip()
        if weight_input.replace(".", "", 1).isdigit():   # check if it's a number (with one dot allowed)
            weight = float(weight_input)
            break
        else:
            print(" Invalid input! Please enter a valid number (e.g., 70.5).")

    valid = ["1", "2", "3"]
    if choice not in valid:
        print("Please  Try again by entering  valid values as directed above")
        return 

    if choice == "1":
        height = float(input("Please enter your height in meters: "))
    elif choice == "2":
        height_in_inches = float(input("Please enter your height in inches: "))
        height = height_in_inches * 0.0254
    elif choice == "3":
        feet = int(input("Enter feet: "))
        inches = int(input("Enter inches: "))
        total_inches = (feet * 12) + inches
        height = total_inches * 0.0254
    else:
        print("Invalid choice, defaulting to meters.")
        height = float(input("Please enter your height in meters: "))

    BMI = round(weight / (height ** 2), 2)

    if BMI < 18.5:
        print(f"Your BMI is {BMI}, you are underweight.")
    elif 18.5 <= BMI < 25:
        print(f"Your BMI is {BMI}, you have a normal weight.")
        print("You can eat samosa parathas + handi's , tute mute with chai")
    elif 25 <= BMI < 30:
        print(f"Your BMI is {BMI}, you are overweight.")
        print("Wow Bro you are at the boundary line now line of control keep eye while you are busy battle between your body and life, I suggests make friend how always give you tensions there , espacilly from Biochemistry domain.")
    elif 30 <= BMI < 35:
        print(f"Your BMI is {BMI}, you are obese (consider a treatment plan).")
        print("Lol ! enjoy your little time in world! keep moving once you stop then you will appear in next world")
    else:
        print(f"Your BMI is {BMI}, you are clinically obese. Please consult a healthcare professional.")

    print("\nThank you for using the BMI Calculator!")

client = input("Please choose from 1 or 2: ").strip()

if client == "1":
    BodyMassIndex()
elif client == "2":
    BabyBloodGroupIdentifier()
else:
    print("There is some technical issue, please email us your query \n"
          "Email: maaz28608@gmail.com")
