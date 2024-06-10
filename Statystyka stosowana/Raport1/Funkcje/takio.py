import random
def remove_duplicates(list1,list2):
    indexes = []
    i = 0
    while i < len(list1) - 1:
        if list1[i] == list1[i + 1]:
            start_index = i
            while i < len(list1) - 1 and list1[i] == list1[i + 1]:
                i += 1
            end_index = i
            indexes.append([start_index, end_index])
        i += 1

    # Usuwamy elementy o podanych indeksach
    for start, end in reversed(indexes):
        del list1[start + 1:end + 1]
        del list2[start + 1:end + 1]

    return indexes

# Przykładowa lista
lista = [1, 3, 3, 3, 4, 6, 7, 8,8]
lista2 = [random.randint(0,10) for i in range(len(lista))]
lista.sort()
print(lista,'\n',lista2)
# Usuwamy duplikaty i elementy o podanych indeksach
wynik= remove_duplicates(lista,lista2)

print("Oryginalna lista:", lista)
print(lista2)

print("Usunięte indeksy:", wynik)
