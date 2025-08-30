print("Welcome to Maazo Clinic!\n")
print("How may we help you today?")
print("1. Check Body Mass Index (BMI)")
print("2. Baby Blood Group Identification")

def baby_blood_group_identifier():
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

    valid_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    father = input("Enter Baby's Father Blood group (e.g. A+, O-): ").upper()
    mother = input("Enter Baby's Mother Blood group (e.g. B+, AB-): ").upper()

    if father not in valid_groups or mother not in valid_groups:
        print("Invalid blood group entered. Please try again.")
        return

    def split_group(bg):
        if bg.endswith('+'):
            return bg[:-1], '+'
        else:
            return bg[:-1], '-'

    father_abo, father_rh = split_group(father)
    mother_abo, mother_rh = split_group(mother)

    # ABO possibilities (simplified)
    combos = {
        ('A', 'A'): ['A', 'O'],
        ('A', 'B'): ['A', 'B', 'AB', 'O'],
        ('B', 'A'): ['A', 'B', 'AB', 'O'],
        ('A', 'AB'): ['A', 'B', 'AB'],
        ('AB', 'A'): ['A', 'B', 'AB'],
        ('A', 'O'): ['A', 'O'],
        ('O', 'A'): ['A', 'O'],
        ('B', 'B'): ['B', 'O'],
        ('B', 'AB'): ['A', 'B', 'AB'],
        ('AB', 'B'): ['A', 'B', 'AB'],
        ('B', 'O'): ['B', 'O'],
        ('O', 'B'): ['B', 'O'],
        ('AB', 'AB'): ['A', 'B', 'AB'],
        ('AB', 'O'): ['A', 'B'],
        ('O', 'AB'): ['A', 'B'],
        ('O', 'O'): ['O']
    }
    possible_abo = combos.get((father_abo, mother_abo), ['O'])
    possible_rh = ['+', '-'] if father_rh == '+' or mother_rh == '+' else ['-']

    print("\nPossible baby blood groups:")
    for abo in possible_abo:
        for rh in possible_rh:
            print(f"{abo}{rh}")





def bodyMassIndex():
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

    # ...existing code...

    while True:
        weight_input = input("Please enter your weight in Kg: ").strip()
        try:
            weight = float(weight_input)
            if weight > 0:
                break
            else:
                print("Weight must be positive.")
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 70.5).")

    valid = ["1", "2", "3"]
    if choice not in valid:
        print("Please try again by entering a valid choice (1, 2, or 3).")
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
    bodyMassIndex()
elif client == "2":
    baby_blood_group_identifier()
else:
    print("There is some technical issue, please email us your query \n"
          "Email: maaz28608@gmail.com")


def baby_care_name():
    print("Welcome to Baby Care center please tell us how may we can help you!")
    input('''Please choose from the following: 
                        
                        1. Baby Names choosing 
                        2. Baby Role in Future
                        3. 
                         ''')
    input("Please enter you father Names")

    input("Enter Letter you want that will first comes in your baby there: ")
    input("Enter your mother name if you want to keep it like family name there: ")
    Names = ["Hazrat " , "Maghaz"]


