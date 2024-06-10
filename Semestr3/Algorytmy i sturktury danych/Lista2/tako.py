def find_max_recursive(sequence):
    if len(sequence) == 1:
        return sequence[0]
    else:
        # Znajdź maksimum w reszcie sekwencji (poza pierwszym elementem)
        max_in_rest = find_max_recursive(sequence[1:])
        
        # Porównaj znalezione maksimum z pierwszym elementem
        if sequence[0] > max_in_rest:
            return sequence[0]
        else:
            return max_in_rest
        
S = [0,-1,5,4]

print(find_max_recursive(S))