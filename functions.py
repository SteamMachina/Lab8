def exercice_one(): #Soizic
    chain = open("chain.txt", "r")
    chain_list = []
    for line in chain.readlines():
        line = line.split('\n')
        chain_list.append(line[:-1][0].split(', '))
    chain_list = chain_list[1][0].split(' ')
    D1 = {}
    D2 = {}
    for i in range(len(chain_list)) :
        D1[chain_list[i]] = i
        D2[i] = chain_list[i]
    return D1, D2

def exo2():
    matrix = []
    with open("chain.txt", "r") as chain:
        lines = chain.readlines()
        for i in range(2, len(lines)):
            line = lines[i][:-1]
            line = line.split(" ")
            sous_list = []
            for nbr in line:
                sous_list.append(int(nbr))
            matrix.append(sous_list)
    return matrix

def exercice_three(D2, M):#Soizic
    food_chain_predator = {}
    for row in range(len(M)):
        l = []
        for column in range(len(M[0])):
            if M[row][column] == 1:
                l.append(D2[column])
        food_chain_predator[D2[row]] = l
    return food_chain_predator

def exercice_four(D2, M):#Soizic
    food_chain_prey = {}
    for row in range(len(M)):
        l = []
        for column in range(len(M[0])):
            if M[row][column] == -1:
                l.append(D2[column])
        food_chain_prey[D2[row]] = l
    return food_chain_prey

def exercice_three_bis(M, D2, elem):#Soizic 
    #Corresponds more too exercice 5 because "I used the strategy of my choice" to do the 3
    Sep = "-->"
    if exercice_three(D2, M)[elem] == []:
        return elem
    else:
        temp = randint(0, (len(exercice_three(D2, M)[elem]) - 1))
        print(elem, end=" ")
        print(Sep, end=" ")
        elem = exercice_three(D2, M)[elem][temp]
        return exercice_three_bis(M, D2, elem)

def exercice_four_bis(M, D2):#Soizic
    for i in range(9):
        elem = D2[i]
        print(exercice_three_bis(M, D2, elem))
