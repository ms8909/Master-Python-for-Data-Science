print("enter the DNA ")
DNA = input()

# if there is any lowercase letter in string,it would be converted into uppercase

DNA_uppercase=DNA.upper()
#print("Uppercased DNA is", DNA_uppercase)

def reverse(DNA):

    DNA_reverse=DNA_uppercase[::-1]
    newone=DNA_reverse


reverse(DNA)

# def complement(s):
    
#     print("complemented dna is")
#     for i in DNA_reverse:
#         if (i=="A"):print("T" ,end = "")
#         if (i=="C"):print("G" ,end = "")
#         if (i=="G"):print("C" ,end = "")
#         if (i=="T"):print("A" ,end = "")
# complement(DNA)