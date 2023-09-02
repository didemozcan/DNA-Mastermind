def random():    #a function is defined to generate the random sequence
    import random   # the library "random" is installed

    nucleotide_list = ["A","T","C","G"]   #The random nucleotide sequence should include these letters
    random_letters = []
    count = 0
    while len(random_letters) < 5:  #a while loop is defined to get random five nucleotide
        a = random.choice(nucleotide_list)   #choice method returns the randomly selected element from the list
        random_letters.append(a)    #Randomly selected nucleotide is added to the list
        count +=1
        sequence = "".join(str(i) for i in random_letters) #Selected nucleotides are joined as a single word called "sequence"
    return(sequence) 



def sequence_inspection(sequence, guess): #a function with two arguments is defined to compare the entered guess and generated random sequence
    output = ""                           #the output is defined
    nucleotides = "AGCT"
    for i in range(len(sequence)):  #for every nucleotide in the sequence a "for loop" is defined.
        if sequence[i] == guess[i]: #if the nucleotides in the same index of the random sequence and guess are the same:
            output += "X"           #an "X" is added to the output to the same position
        elif (guess[i] in sequence) and (sequence[i] != guess[i]):  #if the guessed nucleotides are included in the sequence but not in the same position:
            output += "W"           #a "W" is added to the output to the same index
        elif (guess[i] not in sequence):   #If there is a nucleotide that is not in the sequence:
            output += "-"           #a "-" is added to the same position in the output
    return output                   


#3 empty lists are defined for the arguments of following table function
attempts = []
inputs = []
outputs = []   


def table(attempts, inputs, outputs):    #a function with three list arguments is defined to form the table with attempt number, input (the guess), output  
    print("\nAttempt\tInput\tOutput") 
    for a in range(len(attempts)):       #for every attempt, a table will be generated and printed
        print(f"{attempts[a]}\t{inputs[a]}\t{outputs[a]}")

        
               
#The necessary information about the game is given
print("Welcome to DNA Mastermind!\nThe purpose of this game is to guess a randomly generated DNA sequence.\nA DNA sequence consists of nucleotides with the following codes:\nA, T, C, and G\n")

print("A DNA sequence consisting of 5 nucleotides has now been generated.\nGuess the correct combination of nucleotides. The following letters are allowed:\nA, T, C, and G.\nIf you want to quit playing, please type 'Q'.\nThe sequence should be written as one word.\n\nIf the allowed letters are entered, a table will be generated after that attempt.\nIn the output column of the table it will be shown which positions were guessed correctly (denoted as an X),\nwhich nucleotides are included in the sequence but are not in the correct position (denoted as a W),\nand which are non-included nucleotides (denoted as a –).\n")

#Before the infinite while loop:
wrong_letters = []  #an empty list is defined for the entered wrong letters in the guess
possible_attempts = 12  #the possible attempt number is defined
attempt_number = 0      #the current attempt number is defined

sequence = random()     #the "random function" is called to generate the random sequence and the random sequence is assigned to "sequence"

while True:             #an infinite while loop is defined
    guess = str(input("Please enter your answer in CAPITAL LETTERS:"))  #the input is taken as a string and assigned to "guess"
    
    if (guess == "q" or guess == "Q"):       #If "q/Q" is entered at any time: 
        print("The game has been shut down.")  
        break                                #the loop will be broken, namely it will be halted.
    if (guess == "R" or guess == "r"):       #after the right answer, if the player wants to play the game again, "r/R" will be entered
        print("Restarting...")
        #all of the attempts, inputs, and outputs will be reset. A new sequence will be generated via "random" function
        possible_attempts = 12
        sequence = random()
        attempt_number = 0
        attempts = []
        inputs = []
        outputs = []
        continue        #the infinite while loop will continue
        
    elif (len(guess) != 5):  #if there is more or less than 5 nucleotides in the quess:
        print("\nThe provided input is not 5 characters in length.")
        possible_attempts -= 1   #one attempt is subtracted from the possible attempt number
        attempt_number += 1      #the current attempt number is updated
        print(f"\n{possible_attempts} attempts left.")  #the remaining attempt number is printed
        
    elif (len(guess) == 5) and (guess != sequence):   #if there are five nucleotides in the guess, but the guess is not the same with the random sequence:
        letters = [*guess]        #unpacking operator (*) is used to separate the letters in the string "guess"
        for i in letters:
            if (i != "A" and i != "G" and i != "C" and i != "T"):   #if the letters in guess are not equal to any of the correct nucleotides:
                wrong_letters.append(i)    #these wrong letters are added to the empty list "wrong_letters"
        
        wrong_letters = list(set(wrong_letters)) #If there is multiple entries of a wrong letter, to put just once into the list, "list(set())" operators are used
        
        
        if len(wrong_letters) == 1:   #after the attempt, if there is just one different letter from correct nucleotides:
            
            print(f"\nThe letter {wrong_letters} is not allowed. Please try again.") #the wrong letter is printed
            
        elif len(wrong_letters) == 0:  #If there is no wrong letter, namely if all letters are correct nucleotides:
            
            print("\nWrong Answer!") #It is mentioned that the guess is the wrong answer
            
        else:  #If there is more than one wrong letter entered:
            
            print(f"\nThe letters {','.join(wrong_letters)} are not allowed. Please try again.") #The wrong letters are printed and they are joined with commas
        
        
        attempt_number += 1   #current attempt number is updated
        attempts.append(attempt_number)    #the current attempt number is added to the attempts list 
        inputs.append(guess)     #the entered guess is added to the inputs list
        output = sequence_inspection(sequence,guess)  #the guess is inspected via the previously defined "sequence_inspection" function and assigned to output
        outputs.append(output)    #the output is added to the outputs list
        table(attempts, inputs, outputs)  #the table function is called to print the table including the current attempt number, input sequence, and output sequence    
        
        
        wrong_letters = [] #The wrong_letters list is reset for the next attempt
        possible_attempts -= 1 #The remaining possible attempt number is updated
        print(f"\n{possible_attempts} attempts left.")  #and printed
        
    elif (guess == sequence): #if the guess is the same with the sequence, namely if the answer is correct:
        attempt_number += 1  #current attempt number is updated 
        print(f"\nCongratulations, you have guessed the DNA sequence!\nYou needed {attempt_number} attempts to correctly guess the sequence.\nIf you wish to play again, press 'R'. Press 'Q' if you want to quit.")
        
    if possible_attempts == 0: #if there is no attempt left:
        print(f"\nThe correct sequence was {sequence}.\nUnfortunately, you have not guessed the DNA sequence.\nHowever, do not fear, more chances appear!\nPress 'R' to restart or 'Q' to quit the game.")
    
