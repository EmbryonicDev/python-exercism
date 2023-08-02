def distance(strand_a, strand_b):
    check_letter = "CAGT"
    difference = 0
    
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    for i in range(len(strand_a)):
        if (
            strand_a[i] in check_letter
            and strand_a[i] != strand_b[i]
            ):
            difference += 1
        
    return difference
            
print(distance("GGACTGAAATCTG", "GGACTGAAATCTG")) # answer = 0
print(distance("GGACGGATTCTG", "AGGACGGATTCT")) # answer = 9
print(distance("A", "A")) # answer = 0

