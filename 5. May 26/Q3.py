#Complement Function
def complement(dna): 
    Adenine_count = 0
    Cytosine_count = 0
    Guanine_count = 0
    Thymine_count = 0
    validity = "valid"
    C_dna = ""
    for i in dna: # complemneting

        
        if i == "A" or i == "C" or i == "G" or i == "T":


            if i == "A" : # For Adenine to Thymine
                Adenine_to_Thymine = "T"
                C_dna = C_dna + Adenine_to_Thymine

                
            if i == "C" : # For Cytosine to Guanine
                Cytosine_to_Guanine = "G"
                
                C_dna = C_dna + Cytosine_to_Guanine

            if i == "G" : # For Guanine to Cytosine
                Guanine_to_Cytosine = "C"
                
                C_dna = C_dna + Guanine_to_Cytosine 

            if i == "T" : # For Thymine to Adenine
                Thymine_to_Adenine = "A"
                
                C_dna = C_dna + Thymine_to_Adenine 
        

        elif i != "A" or i != "C" or i != "G" or i != "T":
            validity = "Invalid strings"
    

    if validity == "Invalid strings":

        validity = "Invalid strings"
        return(validity)
    elif validity == "valid":

        dna_string =   C_dna
        return(dna_string)

#Reverse Function
def reverse(reversing): 
    Rev_dna = reversing[::-1] # reversing
    return(Rev_dna)

#Taking input from user and calling of reverse and complement functions
dna_input = input("Enter the DNA string: ")

reversed = reverse(dna_input)
complemented = complement(reversed)

if complemented == "Invalid strings":
    print(complemented)
else:
    print("This is the reversed of input: ",reversed)
    
    print("This is the complemented output: ",complemented)