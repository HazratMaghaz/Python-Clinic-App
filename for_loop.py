# fruits = ("apple", "banana", "cherry", "date")

# for fruit in fruits:
#     print(fruit)

# print("The for Loop for fruits has ended here \n ")    

    # Numbers

# for m in range(5):
#         print(m)



# fruits = ["apple", "banana", "cherry"]

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# for index, fruit in enumerate(fruits):
#       print(index,fruit)

# Names = ["Hazrat", "Maghaz", "Sahal", "Ahmad", "Muhammad", "Hamza"]
# for index, name in enumerate(Names):
#       print(index, name)     
# print("The For Loop is ended here \n")

# DNA =  "AAACCCTTAG AAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAG AAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAGAAACCCTTAG"

# for index, dna in enumerate(DNA):
#       print( index,dna)


# names = ["Alice", "Bob", "Charlie"]
# scores = [90, 85, 88]

# for name, score in zip(names, scores):
#     print(f"{name} scored {score}")


# for name, score in zip(names,scores):
    # print(name, score)


# challange_01:
"""
Write a Python for loop that:
Loops through all numbers from 1 to 100.
Finds only the even numbers.
Calculates their total sum.
Prints the result as: The sum of even numbers from 1 to 100 is: <sum_here>

"""  
# reasult = 0

# for number in range(0,101,2):
#     reasult += number

# print(f"The sum of even numbers from 1 to 100 is: {reasult} ")

# # Other way:

# ans = sum(range(0,101,2))


'''
Chanlage # 02
Loops through all numbers from 1 to 50.
Prints:
"Fizz" if the number is divisible by 3
"Buzz" if the number is divisible by 5
"FizzBuzz" if the number is divisible by both 3 and 5
The number itself if it’s divisible by neither
'''

# for number in range(1, 51):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


'''
Chalange_No: 03 

dna = "ATGCGTATCGTAGCTAGCGTAGCTAGCTAGGCTAA"
Loops through it and counts how many times each nucleotide (A, T, G, C) appears.
Prints the result like:
A: <count>
T: <count>
G: <count>
C: <count>
'''

dna = "ATGCGTATCGTAGCTAGCGTAGCTAGCTAGGCTAA"


length_A = dna.count('A') * 100 / len(dna)
length_A_T = round(length_A,2)
# print(f"{length_A_T}%" )

length_T = dna.count('T') * 100 / len(dna)
length_TT = round(length_T, 2)
# print(length_A_TT, "%")

length_C = dna.count('C') * 100 / len(dna)
length_c = round(length_T, 2)
# print(length_A_c, "%")

length_G = dna.count('G') * 100 / len(dna)
length_g = round(length_G, 2)
# print(length_G, "%")


dna = "ATGCGTATCGTAGCTAGCGTAGCTAGCTAGGCTAA"

count_A = count_T = count_C = count_G = 0


for DNA in dna:
    if DNA == 'A':
        count_A += 1
    elif DNA == 'C':
        count_C += 1
    elif DNA == "T":
        count_T += 1
    elif DNA == 'G':
        count_G += 1
    else:
        print("Hello")  

print(f"Count A: {count_A}")          
print(f"Count T: {count_T}")          
print(f"Count G: {count_G}")          
print(f"Count C: {count_C}")
print(len(dna))

gc_content = count_G + count_C 
per_gc = gc_content *  100 / len(dna)
reasult_gc = round(per_gc,2)
print(f"GC-content will be : {reasult_gc} %")











# Percentage of 'A' characters in the DNA string
# A_percent = dna.count('A') * 100 / len(dna)

# Two common ways to round to 2 decimal places:
# 1. Using round(number, 2)
# rounded_via_round = round(A_percent, 2)
# 2. Using an f-string format specifier :.2f (recommended for direct printing)

# print(f"A% (formatted with f-string): {A_percent:.2f}%")
# print(f"A% (using round()):{rounded_via_round }%")

# If you only want one line, just do:
# print(f"A: {A_percent:.2f}%")

# for DNA in dna:
    