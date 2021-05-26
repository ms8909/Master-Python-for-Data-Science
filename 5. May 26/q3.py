# ARHAM RUMI

# Program to perform DNA Reverse Complement

# Problem Statement

# --------------------------------------------------------------------------------------
# DNA is made up of 4 complex organic building blocks called “nucleotides”. The nucleotides are Adenine, Cytosine, Guanine, and Thymine (abbreviated as A, C, G, and T respectively). A typical DNA strand can be represented as a string that has some combination of these 4 letters. One example is:
# AAAACCCGGT

# There is a transformation that a biologist can perform on an arbitrary strand of DNA called the reverse complement. It involves two steps: reversing the string, and then “complementing” each character. “A” is complemented by “T” (and vice-versa) while “C” is complemented by “G” (and vice-versa). The reverse complement of the above example is: 
# ACCGGGTTTT

# As you can see, the string is reversed, and then all ‘A’s are transformed to ‘T’s, all ‘T’s to ‘A’s, all ‘C’s to ‘G’s, and all ‘G’s to ‘C’s.

# You need to write a script that can do the following:
# Read a DNA string input by the user (check it is a valid DNA string!)
# Reverse the string
# Go through the reversed string and complement each character
# Display the final result (the reverse complement string)

# You must define your own functions reverse(s) and complement(s) to perform and return the results of the reverse and complement operations. Use them in your program.

# This problem was adapted from http://rosalind.info/problems/revc/

# --------------------------------------------------------------------------------------

print("\r")
print("Enter a DNA strand to perform DNA Reverse Complement on it")
print("\r")

def dna_validity(dna):
    valid_dna = "ACGT"
    bool_flag = False
    if all(test_char in valid_dna for test_char in dna):
        bool_flag = True
    else:
        print("Invalid Input")
    return bool_flag


def dna_reverse_complement(dna):
    
    dna_reversed = dna[::-1]

    complemented_dna = ""

    for testChar in dna_reversed:
        if testChar == 'A':
            complemented_dna += 'T'
        if testChar == 'T':
            complemented_dna += 'A'
        if testChar == 'C':
            complemented_dna += 'G'
        if testChar == 'G':
            complemented_dna += 'C'
    
    return complemented_dna


dna_strand_input = input(f"Enter a DNA strand : ")
dna_strand_std = dna_strand_input.upper()

dna_valid_status = dna_validity(dna_strand_std)

if dna_valid_status == True:
    reversed_complemented_dna = dna_reverse_complement(dna_strand_std)
    print(f"Original DNA Strand             : {dna_strand_std}")
    print(f"Reverse Complemented DNA Strand : {reversed_complemented_dna}")

else:
    print("Enter the Valid Input")