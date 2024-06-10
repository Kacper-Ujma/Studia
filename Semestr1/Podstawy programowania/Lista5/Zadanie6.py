
try:
    Lista = input("wpisz kolejne leementy listy odzielajac je spacja\n")
    Lista = Lista.split()
    for i  in range(len(Lista)):
        Lista[i] = int(Lista[i])
    print(Lista==list(sorted(Lista)))
except ValueError:
    print("lista nie zawiera tylko liczb") 

    
     
