def complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    bases = list(seq) 
    bases = [complement[base] for base in bases] 
    return ''.join(bases)
    
def reverse_complement(s):
        return complement(s[::-1])
a=str(input("Enter the name of DNA : "))
print ("Reverse Complement:")
print(reverse_complement(a))